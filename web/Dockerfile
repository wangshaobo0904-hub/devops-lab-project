# ============================================
# 个人介绍网站 - Dockerfile
# 基于 nginx:alpine 构建静态网站镜像
# ============================================

# --- 阶段 1: 构建阶段（可选，此处静态文件直接使用） ---
# 如果你的网站需要构建步骤（如 npm build），在此阶段完成
# FROM node:18-alpine AS builder
# WORKDIR /app
# COPY . .
# RUN npm install && npm run build

# --- 阶段 2: 运行阶段 ---
FROM nginx:alpine

# 设置维护者信息
LABEL maintainer="wangshaobo-20242206"
LABEL description="DevOps Lab - 个人介绍网站"

# 删除 Nginx 默认页面
RUN rm -rf /usr/share/nginx/html/*

# 将静态网站文件复制到 Nginx 默认目录
COPY index.html /usr/share/nginx/html/
COPY css/ /usr/share/nginx/html/css/
COPY js/ /usr/share/nginx/html/js/
COPY images/ /usr/share/nginx/html/images/

# 自定义 Nginx 配置（可选）
# 如果你需要自定义配置，取消下面注释并创建 nginx.conf 文件
# COPY nginx.conf /etc/nginx/conf.d/default.conf

# 暴露 80 端口
EXPOSE 80

# Nginx 前台运行（镜像默认 CMD 已包含，此处显式声明）
CMD ["nginx", "-g", "daemon off;"]
