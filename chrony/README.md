# Chrony NTP Server (Docker)

## Description

Chrony is a versatile implementation of the Network Time Protocol (NTP). It can synchronize the system clock with NTP servers, and it can also act as an NTP server itself, providing time synchronization to other devices on the network. Chrony is designed to work well in a variety of conditions, including intermittent network connections and congested networks.

## Features

- NTP server for network time synchronization
- Fast and accurate time synchronization
- Works well with intermittent network connections
- Supports NTPv4 protocol
- Low resource usage
- Suitable for virtual machines and containers

## Quick Start

1. Copy `.env.example` to `.env` (optional):
   ```bash
   cp .env.example .env
   ```

2. Start the service:
   ```bash
   docker compose up -d
   ```

3. Configure your devices to use this server as their NTP server.

## Client Configuration

### Linux

Edit `/etc/chrony/chrony.conf` (or `/etc/chrony.conf`):
```
server <server-ip> iburst
```
Then restart chrony:
```bash
sudo systemctl restart chrony
```

### Windows

Open an elevated Command Prompt:
```cmd
w32tm /config /manualpeerlist:<server-ip> /syncfromflags:manual /reliable:YES /update
w32tm /resync
```

### macOS

```bash
sudo sntp -sS <server-ip>
```

## Requirements

- **SYS_TIME capability**: The container needs `SYS_TIME` capability to set the system clock.
- **Port 123**: NTP uses UDP port 123. Ensure no other NTP service is running on the host.

## How It Works

1. Chrony synchronizes time from upstream NTP servers (e.g., pool.ntp.org)
2. It then serves as an NTP server for your local network
3. Devices on your network can query this server for accurate time
4. This reduces external NTP traffic and provides consistent time across your network

## Environment Variables

No environment variables are required.

## Ports

| Port | Protocol | Description |
|------|----------|-------------|
| `123`| UDP      | NTP service |

---

# Chrony NTP 服务器 (Docker)

## 描述

Chrony 是网络时间协议 (NTP) 的多功能实现。它可以将系统时钟与 NTP 服务器同步，也可以作为 NTP 服务器本身，为网络上的其他设备提供时间同步。Chrony 设计用于在各种条件下良好工作，包括间歇性网络连接和拥塞的网络。

## 功能

- 用于网络时间同步的 NTP 服务器
- 快速且准确的时间同步
- 在间歇性网络连接下表现良好
- 支持 NTPv4 协议
- 低资源占用
- 适用于虚拟机和容器

## 快速开始

1. 复制 `.env.example` 为 `.env`（可选）：
   ```bash
   cp .env.example .env
   ```

2. 启动服务：
   ```bash
   docker compose up -d
   ```

3. 将您的设备配置为使用此服务器作为 NTP 服务器。

## 客户端配置

### Linux

编辑 `/etc/chrony/chrony.conf`（或 `/etc/chrony.conf`）：
```
server <服务器IP> iburst
```
然后重启 chrony：
```bash
sudo systemctl restart chrony
```

### Windows

打开提升权限的命令提示符：
```cmd
w32tm /config /manualpeerlist:<服务器IP> /syncfromflags:manual /reliable:YES /update
w32tm /resync
```

### macOS

```bash
sudo sntp -sS <服务器IP>
```

## 要求

- **SYS_TIME 能力**：容器需要 `SYS_TIME` 能力来设置系统时钟。
- **端口 123**：NTP 使用 UDP 端口 123。确保主机上没有其他 NTP 服务运行。

## 工作原理

1. Chrony 从上游 NTP 服务器（如 pool.ntp.org）同步时间
2. 然后作为 NTP 服务器为您的本地网络提供服务
3. 网络上的设备可以查询此服务器获取准确时间
4. 这减少了外部 NTP 流量，并在整个网络中提供一致的时间

## 环境变量

不需要环境变量。

## 端口

| 端口 | 协议 | 说明      |
|------|------|-----------|
| `123`| UDP  | NTP 服务  |
