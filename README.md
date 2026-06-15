# 🚀 DevOps Lab - Personal Portfolio + Todo App

> **Course**: DevOps Development & Operations Practice
> **Lab Topic**: Docker Containerization & CI/CD Automated Deployment
> **Date**: June 2026

---

## 👥 Team Members

| Name | Student ID | Contribution | Responsibilities |
|------|-----------|-------------|-----------------|
| Wang Shaobo | 20242206 | 100% | Website development, Dockerfile, Docker Compose, CI/CD, Documentation |

---

## 📸 Profile Photo

![Profile Photo](web/images/avatar.jpg)

---

## 🌐 Application URLs

| Application | URL |
|-------------|-----|
| Personal Portfolio | http://54.147.40.189:8080 |
| Todo App | http://54.147.40.189:8081 |

---

## 📋 Project Overview

### Project Structure

```
devops-lab-project/
├── .github/
│   └── workflows/
│       └── deploy.yml          # GitHub Actions CI/CD pipeline
├── web/                        # Personal portfolio website
│   ├── index.html              # Main page
│   ├── css/
│   │   └── style.css           # Stylesheet
│   ├── js/
│   │   └── main.js             # Interactive scripts
│   ├── images/
│   │   └── avatar.jpg          # Profile photo
│   └── Dockerfile              # Nginx image build file
├── todo-app/                   # Todo application (Flask + SQLite)
│   ├── app.py                  # Flask backend
│   ├── requirements.txt        # Python dependencies
│   ├── templates/
│   │   └── index.html          # Todo frontend page
│   └── Dockerfile              # Python image build file
├── docker-compose.yml          # Multi-container orchestration
├── .gitignore
└── README.md                   # Project documentation
```

### Tech Stack

| Component | Technology |
|-----------|------------|
| Portfolio Website | HTML5 / CSS3 / JavaScript (pure static) |
| Todo App | Python Flask + SQLite |
| Containerization | Docker + Docker Compose |
| Web Server | Nginx (Alpine) |
| CI/CD | GitHub Actions |
| Image Registry | Docker Hub |

### Todo App Description

The Todo app is a lightweight task management tool:
- **Tech**: Python Flask + SQLite
- **Features**: Add / Complete / Delete tasks
- **Data Persistence**: SQLite database persisted via Docker Volume
- **No External DB**: SQLite is embedded, works out of the box

> 💡 To use a different open-source Todo app (e.g. [todomvc](https://github.com/tastejs/todomvc)), simply replace the `todo-app/` directory and update the build configuration in `docker-compose.yml` accordingly.

---

## 🛠️ Deployment Guide

### Prerequisites

- Docker Engine 20.10+
- Docker Compose v2+
- Git

### Local Development & Testing

```bash
# 1. Clone the project
git clone https://github.com/wangshaobo0904-hub/devops-lab-project.git
cd devops-lab-project

# 2. Add your profile photo (already done)
# Place your photo at web/images/avatar.jpg

# 3. Start services
docker compose up -d

# 4. Verify services
# Portfolio website: http://localhost:8080
# Todo app:         http://localhost:8081

# 5. Check logs
docker compose logs -f

# 6. Stop services
docker compose down
```

### Production Deployment (via CI/CD)

1. Push code to the GitHub `main` branch
2. GitHub Actions automatically triggers the deployment pipeline
3. Pipeline: Build image → Push to Docker Hub → SSH deploy to server

### Server Environment Setup

```bash
# Install Docker
curl -fsSL https://get.docker.com | sh
sudo usermod -aG docker $USER

# Create project directory
sudo mkdir -p /opt/devops-lab-project
sudo chown $USER:$USER /opt/devops-lab-project

# Clone the project
cd /opt
git clone https://github.com/wangshaobo0904-hub/devops-lab-project.git
```

---

## 🔑 Environment Variables & Secrets

| Secret Name | Description | How to Obtain |
|-------------|-------------|---------------|
| `DOCKERHUB_USERNAME` | Docker Hub username | Register at hub.docker.com |
| `DOCKERHUB_TOKEN` | Docker Hub Access Token | Docker Hub → Settings → Security → New Access Token |
| `SERVER_HOST` | Server IP address | Your cloud server's public IP |
| `SERVER_USER` | SSH username | Usually `root` or `ubuntu` |
| `SERVER_SSH_KEY` | SSH private key (full content) | Generate with `ssh-keygen -t ed25519`, paste the private key |

---

## 📝 Lab Checklist

- [ ] Portfolio website is accessible
- [ ] Todo app is functional
- [ ] Docker Compose starts both services with one command
- [ ] GitHub Actions auto-deployment succeeds
- [ ] Full demo recorded on video
