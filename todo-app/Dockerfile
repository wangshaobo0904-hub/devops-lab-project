# ============================================
# Todo 应用 - Dockerfile
# 基于 python:3.11-alpine 构建 Flask 应用
# ============================================

FROM python:3.11-alpine

LABEL maintainer="wangshaobo-20242206"
LABEL description="DevOps Lab - 轻量级 Todo 应用"

# 设置工作目录
WORKDIR /app

# 安装依赖
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 复制应用代码
COPY app.py .
COPY templates/ templates/

# 创建数据目录（用于 SQLite 持久化）
RUN mkdir -p /app/data

# 暴露端口
EXPOSE 5000

# 启动应用
CMD ["python", "app.py"]
