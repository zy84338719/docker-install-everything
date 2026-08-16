# Munin (Docker)

## Description

Munin is a networked system monitoring, measurement, and alerting tool. It uses RRDtool to create graphs of resource usage over time, providing a visual overview of system performance. Munin can monitor CPU, memory, disk, network, and many other metrics through a plugin-based architecture.

## Features

- System resource monitoring and graphing
- RRDtool-based time-series graphs
- Plugin-based architecture for extensibility
- Web-based dashboard with historical data
- Alert/notification capabilities
- Monitors CPU, memory, disk, network, and more

## Quick Start

1. Copy `.env.example` to `.env` (optional):
   ```bash
   cp .env.example .env
   ```

2. Optionally edit `conf/munin.conf` to customize monitoring.

3. Start the service:
   ```bash
   docker compose up -d
   ```

4. Access the web interface at `http://localhost:8080`

## Configuration

All configuration is done via `conf/munin.conf`. The default configuration:

- Monitors localhost (127.0.0.1)
- Stores data in `/var/lib/munin`
- Uses standard Munin templates

### Monitoring Remote Hosts

To monitor remote servers, install `munin-node` on the target server and add a host entry:

```conf
[remote-server]
    address 192.168.1.100
    use_node_name yes
```

### Plugin Configuration

Munin plugins can be configured with environment variables:

```conf
[cpu]
    env.scale no

[df]
    env.warning 80
    env.critical 90
```

## Requirements

- **Storage**: RRD data and HTML output are stored in `./data`.
- **Configuration**: Edit `conf/munin.conf` to customize.

## Environment Variables

No environment variables are required. All configuration is in `conf/munin.conf`.

## Ports

| Port  | Protocol | Description      |
|-------|----------|------------------|
| `8080`| HTTP     | Munin web UI     |

---

# Munin (Docker)

## 描述

Munin 是一个网络化系统监控、测量和告警工具。它使用 RRDtool 创建资源使用情况随时间变化的图表，提供系统性能的可视化概览。Munin 可以通过基于插件的架构监控 CPU、内存、磁盘、网络和许多其他指标。

## 功能

- 系统资源监控和图表展示
- 基于 RRDtool 的时间序列图表
- 基于插件的可扩展架构
- 带历史数据的 Web 仪表板
- 告警/通知功能
- 监控 CPU、内存、磁盘、网络等

## 快速开始

1. 复制 `.env.example` 为 `.env`（可选）：
   ```bash
   cp .env.example .env
   ```

2. 可选编辑 `conf/munin.conf` 自定义监控设置。

3. 启动服务：
   ```bash
   docker compose up -d
   ```

4. 访问 Web 界面：`http://localhost:8080`

## 配置

所有配置通过 `conf/munin.conf` 完成。默认配置：

- 监控 localhost（127.0.0.1）
- 数据存储在 `/var/lib/munin`
- 使用标准 Munin 模板

### 监控远程主机

要监控远程服务器，请在目标服务器上安装 `munin-node` 并添加主机条目：

```conf
[remote-server]
    address 192.168.1.100
    use_node_name yes
```

### 插件配置

Munin 插件可以通过环境变量配置：

```conf
[cpu]
    env.scale no

[df]
    env.warning 80
    env.critical 90
```

## 要求

- **存储**：RRD 数据和 HTML 输出存储在 `./data`。
- **配置**：编辑 `conf/munin.conf` 进行自定义。

## 环境变量

不需要环境变量。所有配置在 `conf/munin.conf` 中完成。

## 端口

| 端口   | 协议 | 说明            |
|--------|------|-----------------|
| `8080` | HTTP | Munin Web 界面  |
