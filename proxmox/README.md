# Proxmox VE (Docker)

## Description

Proxmox Virtual Environment (VE) is an open-source server management platform for enterprise virtualization. It tightly integrates the KVM hypervisor and Linux Containers (LXC), software-defined storage, and networking functionality, all on a single platform. This Docker image runs Proxmox VE in a container for quick evaluation and testing.

## Features

- Full-featured web-based management interface
- KVM virtualization and LXC container support
- Cluster management capabilities
- Built-in backup and restore functionality
- Role-based access control

## Quick Start

1. Copy `.env.example` to `.env` and configure:
   ```bash
   cp .env.example .env
   ```

2. Start the service:
   ```bash
   docker compose up -d
   ```

3. Access the web interface at `https://localhost:8006`

## Requirements

- **KVM support**: The host must have `/dev/kvm` available. Verify with:
  ```bash
  ls -la /dev/kvm
  ```
- **Privileged mode**: The container runs in privileged mode for virtualization capabilities.
- **Memory**: At least 2GB RAM recommended for the container.
- **Storage**: Data is stored in `./data` and cluster config in `./config`.

## Default Credentials

- **Username**: `root`
- **Password**: Value of `PASSWORD` in `.env` (default: `root`)

## Environment Variables

| Variable   | Default | Description                      |
|------------|---------|----------------------------------|
| `PASSWORD` | `root`  | Root password for Proxmox web UI |

## Ports

| Port  | Protocol | Description          |
|-------|----------|----------------------|
| `8006`| HTTPS    | Proxmox web UI       |

---

# Proxmox VE (Docker)

## 描述

Proxmox Virtual Environment (VE) 是一个开源的企业级虚拟化服务器管理平台。它将 KVM 虚拟化和 Linux 容器 (LXC)、软件定义存储和网络功能紧密集成在单一平台上。此 Docker 镜像可在容器中运行 Proxmox VE，便于快速评估和测试。

## 功能

- 全功能的 Web 管理界面
- KVM 虚拟化和 LXC 容器支持
- 集群管理功能
- 内置备份和恢复功能
- 基于角色的访问控制

## 快速开始

1. 复制 `.env.example` 为 `.env` 并进行配置：
   ```bash
   cp .env.example .env
   ```

2. 启动服务：
   ```bash
   docker compose up -d
   ```

3. 访问 Web 界面：`https://localhost:8006`

## 要求

- **KVM 支持**：主机必须有 `/dev/kvm` 可用。验证方法：
  ```bash
  ls -la /dev/kvm
  ```
- **特权模式**：容器需要以特权模式运行以支持虚拟化功能。
- **内存**：建议容器至少分配 2GB 内存。
- **存储**：数据存储在 `./data`，集群配置存储在 `./config`。

## 默认凭据

- **用户名**：`root`
- **密码**：`.env` 中 `PASSWORD` 的值（默认：`root`）

## 环境变量

| 变量       | 默认值 | 说明                        |
|------------|--------|-----------------------------|
| `PASSWORD` | `root` | Proxmox Web 界面的 root 密码 |

## 端口

| 端口   | 协议  | 说明              |
|--------|-------|-------------------|
| `8006` | HTTPS | Proxmox Web 界面  |
