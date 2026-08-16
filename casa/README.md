# CasaOS (Docker)

## Description

CasaOS is a simple, easy-to-use, open-source home cloud system. It provides a clean web interface to manage your personal files, apps, and Docker containers. CasaOS turns any device into a home cloud server, making it easy to self-host applications and manage your data.

## Features

- Clean and intuitive web-based dashboard
- Built-in file manager with media preview
- One-click Docker app installation from an app store
- Full Docker container management on the host
- Storage and network management
- Multi-user support

## Quick Start

1. Copy `.env.example` to `.env` (optional):
   ```bash
   cp .env.example .env
   ```

2. Start the service:
   ```bash
   docker compose up -d
   ```

3. Access the web interface at `http://localhost:8080`

## Requirements

- **Docker Socket**: The container mounts `/var/run/docker.sock` to manage host Docker containers.
- **Storage**: Data is stored in `./data` (mapped to `/DATA` inside the container).

## Docker Socket Access

CasaOS requires access to the host Docker daemon. This allows it to:
- Install and manage Docker-based applications from its app store
- Monitor running containers
- Manage container lifecycle (start, stop, restart)

**Security Note**: Granting Docker socket access is equivalent to giving root access to the host. Only use on trusted networks.

## Environment Variables

No environment variables are required for basic setup.

## Ports

| Port  | Protocol | Description      |
|-------|----------|------------------|
| `8080`| HTTP     | CasaOS web UI    |

---

# CasaOS (Docker)

## 描述

CasaOS 是一个简单易用的开源家庭云系统。它提供了一个简洁的 Web 界面来管理个人文件、应用和 Docker 容器。CasaOS 可以将任何设备变成家庭云服务器，轻松实现应用自托管和数据管理。

## 功能

- 简洁直观的 Web 管理仪表板
- 内置文件管理器，支持媒体预览
- 应用商店一键安装 Docker 应用
- 完整的主机 Docker 容器管理
- 存储和网络管理
- 多用户支持

## 快速开始

1. 复制 `.env.example` 为 `.env`（可选）：
   ```bash
   cp .env.example .env
   ```

2. 启动服务：
   ```bash
   docker compose up -d
   ```

3. 访问 Web 界面：`http://localhost:8080`

## 要求

- **Docker Socket**：容器挂载 `/var/run/docker.sock` 以管理主机 Docker 容器。
- **存储**：数据存储在 `./data`（映射到容器内的 `/DATA`）。

## Docker Socket 访问

CasaOS 需要访问主机 Docker 守护进程，以便：
- 从应用商店安装和管理基于 Docker 的应用
- 监控运行中的容器
- 管理容器生命周期（启动、停止、重启）

**安全提示**：授予 Docker socket 访问权限等同于授予主机 root 权限。请仅在受信任的网络中使用。

## 环境变量

基本设置不需要环境变量。

## 端口

| 端口   | 协议 | 说明            |
|--------|------|-----------------|
| `8080` | HTTP | CasaOS Web 界面 |
