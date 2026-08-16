# Samba SMB File Server (Docker)

## Description

Samba is an open-source implementation of the SMB/CIFS networking protocol. It provides file and print services to SMB/CIFS clients, allowing seamless file sharing between Linux/Unix servers and Windows, macOS, and Linux clients. This Docker image provides a ready-to-use Samba file server.

## Features

- SMB/CIFS file sharing protocol support
- Compatible with Windows, macOS, and Linux clients
- Simple user/password authentication
- Easy shared storage configuration
- Network file access from any device

## Quick Start

1. Copy `.env.example` to `.env` and configure credentials:
   ```bash
   cp .env.example .env
   ```

2. Start the service:
   ```bash
   docker compose up -d
   ```

3. Connect from your client device (see below).

## Connecting Clients

### Windows

Open File Explorer and navigate to:
```
\\<server-ip>\storage
```
Enter the username and password from your `.env` file when prompted.

### macOS

In Finder, press `Cmd+K` and enter:
```
smb://<server-ip>/storage
```

### Linux

Mount the share:
```bash
sudo mount -t cifs //<server-ip>/storage /mnt/samba -o username=<SAMBA_USER>,password=<SAMBA_PASSWORD>
```

Or using `smbclient`:
```bash
smbclient //<server-ip>/storage -U <SAMBA_USER>
```

## Environment Variables

| Variable          | Default   | Description            |
|-------------------|-----------|------------------------|
| `SAMBA_USER`      | `admin`   | Samba username         |
| `SAMBA_PASSWORD`  | `admin`   | Samba password         |

## Ports

| Port  | Protocol | Description          |
|-------|----------|----------------------|
| `445` | TCP      | SMB/CIFS file sharing|

---

# Samba SMB 文件服务器 (Docker)

## 描述

Samba 是 SMB/CIFS 网络协议的开源实现。它为 SMB/CIFS 客户端提供文件和打印服务，允许 Linux/Unix 服务器与 Windows、macOS 和 Linux 客户端之间无缝共享文件。此 Docker 镜像提供了一个开箱即用的 Samba 文件服务器。

## 功能

- SMB/CIFS 文件共享协议支持
- 兼容 Windows、macOS 和 Linux 客户端
- 简单的用户名/密码认证
- 易于配置的共享存储
- 从任何设备访问网络文件

## 快速开始

1. 复制 `.env.example` 为 `.env` 并配置凭据：
   ```bash
   cp .env.example .env
   ```

2. 启动服务：
   ```bash
   docker compose up -d
   ```

3. 从客户端设备连接（见下方说明）。

## 连接客户端

### Windows

打开文件资源管理器，导航到：
```
\\<服务器IP>\storage
```
提示时输入 `.env` 文件中的用户名和密码。

### macOS

在 Finder 中按 `Cmd+K`，输入：
```
smb://<服务器IP>/storage
```

### Linux

挂载共享：
```bash
sudo mount -t cifs //<服务器IP>/storage /mnt/samba -o username=<SAMBA_USER>,password=<SAMBA_PASSWORD>
```

或使用 `smbclient`：
```bash
smbclient //<服务器IP>/storage -U <SAMBA_USER>
```

## 环境变量

| 变量              | 默认值    | 说明            |
|-------------------|-----------|-----------------|
| `SAMBA_USER`      | `admin`   | Samba 用户名    |
| `SAMBA_PASSWORD`  | `admin`   | Samba 密码      |

## 端口

| 端口  | 协议 | 说明              |
|-------|------|-------------------|
| `445` | TCP  | SMB/CIFS 文件共享 |
