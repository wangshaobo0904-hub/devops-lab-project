"""
轻量级 Todo 应用 - Flask + SQLite
DevOps Lab Project - 用于 Docker Compose 演示
"""

import os
import sqlite3
from datetime import datetime

from flask import Flask, render_template, request, redirect, url_for, jsonify

# --- 初始化 Flask ---
app = Flask(__name__)

# 数据库文件路径（使用卷挂载持久化）
DB_DIR = os.environ.get("DATA_DIR", "/app/data")
DB_PATH = os.path.join(DB_DIR, "todos.db")


def get_db():
    """获取数据库连接"""
    os.makedirs(DB_DIR, exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    """初始化数据库表"""
    conn = get_db()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS todos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            completed INTEGER DEFAULT 0,
            created_at TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()


# --- 路由 ---

@app.route("/")
def index():
    """首页 - 显示所有 Todo"""
    conn = get_db()
    todos = conn.execute(
        "SELECT * FROM todos ORDER BY completed ASC, created_at DESC"
    ).fetchall()
    conn.close()
    return render_template("index.html", todos=todos)


@app.route("/add", methods=["POST"])
def add():
    """添加新 Todo"""
    title = request.form.get("title", "").strip()
    if title:
        conn = get_db()
        conn.execute(
            "INSERT INTO todos (title, created_at) VALUES (?, ?)",
            (title, datetime.now().strftime("%Y-%m-%d %H:%M:%S")),
        )
        conn.commit()
        conn.close()
    return redirect(url_for("index"))


@app.route("/toggle/<int:todo_id>", methods=["POST"])
def toggle(todo_id):
    """切换 Todo 完成状态"""
    conn = get_db()
    todo = conn.execute("SELECT completed FROM todos WHERE id = ?", (todo_id,)).fetchone()
    if todo:
        new_status = 0 if todo["completed"] else 1
        conn.execute("UPDATE todos SET completed = ? WHERE id = ?", (new_status, todo_id))
        conn.commit()
    conn.close()
    return redirect(url_for("index"))


@app.route("/delete/<int:todo_id>", methods=["POST"])
def delete(todo_id):
    """删除 Todo"""
    conn = get_db()
    conn.execute("DELETE FROM todos WHERE id = ?", (todo_id,))
    conn.commit()
    conn.close()
    return redirect(url_for("index"))


@app.route("/health")
def health():
    """健康检查端点"""
    return jsonify({"status": "ok", "timestamp": datetime.now().isoformat()})


# --- 启动 ---
if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=5000, debug=False)
