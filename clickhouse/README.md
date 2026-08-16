# ClickHouse - 列式分析数据库 / Columnar Analytics Database

## 概述 / Overview

ClickHouse 是一个用于联机分析 (OLAP) 的高性能列式数据库管理系统。
ClickHouse is a high-performance columnar database management system for online analytical processing (OLAP).

## 快速开始 / Quick Start

```bash
# 复制环境变量配置 / Copy environment config
cp .env.example .env

# 启动服务 / Start service
docker-compose up -d

# 停止服务 / Stop service
docker-compose down
```

## 连接方式 / Connection

HTTP 接口 / HTTP interface:
```bash
curl 'http://127.0.0.1:8123/?query=SELECT%201'
```

使用 clickhouse-client / Using clickhouse-client:
```bash
clickhouse-client --host 127.0.0.1 --port 9000
```

## 端口说明 / Ports

| 端口 / Port | 用途 / Purpose |
|---|---|
| 8123 | HTTP 接口 / HTTP interface |
| 9000 | TCP 客户端接口 / TCP client interface |

## 环境变量 / Environment Variables

| 变量 / Variable | 默认值 / Default | 说明 / Description |
|---|---|---|
| CLICKHOUSE_VERSION | 24-alpine | ClickHouse 镜像版本 / Image version |
| CLICKHOUSE_DB | default | 默认数据库名 / Default database name |
| CLICKHOUSE_USER | default | 默认用户名 / Default username |
| CLICKHOUSE_PASSWORD | (空/empty) | 用户密码 / User password |

## 常用命令 / Common Commands

```bash
# 查看日志 / View logs
docker-compose logs -f

# 进入容器 / Enter container
docker-compose exec clickhouse clickhouse-client

# 查看状态 / Check status
docker-compose ps
```

## 数据持久化 / Data Persistence

- 数据存储在 `./data/clickhouse` 目录下
- 日志存储在 `./log/clickhouse` 目录下
- 自定义配置: `./conf/clickhouse.xml`

Data stored in `./data/clickhouse`, logs in `./log/clickhouse`, custom config at `./conf/clickhouse.xml`.
