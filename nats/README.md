# NATS - 高性能消息系统 / High-Performance Messaging

## 概述 / Overview

NATS 是一个高性能、轻量级的消息系统，支持发布/订阅、请求/回复和队列组等模式。
NATS is a high-performance, lightweight messaging system supporting pub/sub, request/reply, and queue groups.

## 快速开始 / Quick Start

```bash
# 复制环境变量配置 / Copy environment config
cp .env.example .env

# 启动服务 / Start service
docker-compose up -d

# 停止服务 / Stop service
docker-compose down
```

## 端口说明 / Ports

| 端口 / Port | 用途 / Purpose |
|---|---|
| 4222 | 客户端连接端口 / Client connections |
| 8222 | HTTP 监控端口 / HTTP monitoring |
| 6222 | 集群路由端口 / Cluster routing |

## 访问监控 / Access Monitoring

打开浏览器访问 / Open browser to:
```
http://127.0.0.1:8222
```

## 环境变量 / Environment Variables

| 变量 / Variable | 默认值 / Default | 说明 / Description |
|---|---|---|
| NATS_VERSION | 2.10-alpine | NATS 镜像版本 / NATS image version |

## 常用命令 / Common Commands

```bash
# 查看日志 / View logs
docker-compose logs -f

# 重启服务 / Restart service
docker-compose restart

# 查看状态 / Check status
docker-compose ps
```

## 数据持久化 / Data Persistence

数据存储在 `./data/nats` 目录下（已启用 JetStream）。
Data is stored in `./data/nats` (JetStream enabled).
