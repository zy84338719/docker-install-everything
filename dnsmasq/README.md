# dnsmasq (Docker)

## Description

dnsmasq is a lightweight, easy-to-configure DNS forwarder and DHCP server. It is designed to provide DNS and optionally DHCP services to a small network. It can serve as a local DNS cache, ad blocker, and DHCP server, making it ideal for home labs, small offices, and development environments.

## Features

- Lightweight DNS forwarder and cache
- DHCP server functionality
- Local DNS hostname resolution
- Ad blocking via DNS sinkholing
- Low resource usage
- Simple configuration file

## Quick Start

1. Copy `.env.example` to `.env` (optional):
   ```bash
   cp .env.example .env
   ```

2. Edit the configuration file `conf/dnsmasq.conf` to suit your needs.

3. Start the service:
   ```bash
   docker compose up -d
   ```

4. Configure your devices or router to use this server as their DNS.

## Configuration

All configuration is done via `conf/dnsmasq.conf`. The default configuration includes:

- Listening on all interfaces
- Google DNS (8.8.8.8, 8.8.4.4) and Cloudflare DNS (1.1.1.1) as upstream servers
- DNS cache of 1000 entries
- Example entries for local DNS and DHCP (commented out)

### Common Configuration Examples

#### Add Local DNS Entries
```
address=/home.lan/192.168.1.1
address=/nas.lan/192.168.1.100
```

#### Enable DHCP Server
```
dhcp-range=192.168.1.100,192.168.1.200,255.255.255.0,24h
dhcp-option=option:router,192.168.1.1
dhcp-option=option:dns-server,192.168.1.1
```

#### Block Advertisements
```
address=/ads.example.com/
address=/tracking.example.com/
```

## Requirements

- **Port 53**: DNS service (TCP and UDP). Ensure no other DNS service is running on the host.
- **Port 67**: DHCP service (UDP). Only needed if using DHCP functionality.
- **Configuration**: Edit `conf/dnsmasq.conf` to customize.

## Environment Variables

No environment variables are required. All configuration is in `conf/dnsmasq.conf`.

## Ports

| Port | Protocol | Description  |
|------|----------|--------------|
| `53` | TCP/UDP  | DNS service  |
| `67` | UDP      | DHCP service |

---

# dnsmasq (Docker)

## 描述

dnsmasq 是一个轻量级、易于配置的 DNS 转发器和 DHCP 服务器。它旨在为小型网络提供 DNS 和可选的 DHCP 服务。它可以作为本地 DNS 缓存、广告拦截器和 DHCP 服务器，非常适合家庭实验室、小型办公室和开发环境。

## 功能

- 轻量级 DNS 转发器和缓存
- DHCP 服务器功能
- 本地 DNS 主机名解析
- 通过 DNS 陷坑进行广告拦截
- 低资源占用
- 简单的配置文件

## 快速开始

1. 复制 `.env.example` 为 `.env`（可选）：
   ```bash
   cp .env.example .env
   ```

2. 编辑配置文件 `conf/dnsmasq.conf` 以满足您的需求。

3. 启动服务：
   ```bash
   docker compose up -d
   ```

4. 将您的设备或路由器配置为使用此服务器作为 DNS。

## 配置

所有配置通过 `conf/dnsmasq.conf` 完成。默认配置包括：

- 监听所有接口
- Google DNS（8.8.8.8、8.8.4.4）和 Cloudflare DNS（1.1.1.1）作为上游服务器
- 1000 条 DNS 缓存
- 本地 DNS 和 DHCP 的示例条目（已注释）

### 常见配置示例

#### 添加本地 DNS 条目
```
address=/home.lan/192.168.1.1
address=/nas.lan/192.168.1.100
```

#### 启用 DHCP 服务器
```
dhcp-range=192.168.1.100,192.168.1.200,255.255.255.0,24h
dhcp-option=option:router,192.168.1.1
dhcp-option=option:dns-server,192.168.1.1
```

#### 拦截广告
```
address=/ads.example.com/
address=/tracking.example.com/
```

## 要求

- **端口 53**：DNS 服务（TCP 和 UDP）。确保主机上没有其他 DNS 服务运行。
- **端口 67**：DHCP 服务（UDP）。仅在使用 DHCP 功能时需要。
- **配置**：编辑 `conf/dnsmasq.conf` 进行自定义。

## 环境变量

不需要环境变量。所有配置在 `conf/dnsmasq.conf` 中完成。

## 端口

| 端口 | 协议     | 说明         |
|------|----------|--------------|
| `53` | TCP/UDP  | DNS 服务     |
| `67` | UDP      | DHCP 服务    |
