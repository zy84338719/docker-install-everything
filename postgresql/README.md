# PostgreSQL - 对象关系型数据库 / Object-Relational Database

## 概述 / Overview

PostgreSQL 是一个功能强大的开源对象关系数据库系统，具有高度的可扩展性和标准合规性。
PostgreSQL is a powerful, open-source object-relational database system with strong extensibility and standards compliance.

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

使用 psql 连接 / Connect with psql:
```bash
psql -h 127.0.0.1 -U postgres -d test
```

使用连接字符串 / Connection string:
```
postgresql://postgres:postgres@127.0.0.1:5432/test
```

## 端口说明 / Ports

| 端口 / Port | 用途 / Purpose |
|---|---|
| 5432 | PostgreSQL 服务端口 / PostgreSQL service port |

## 环境变量 / Environment Variables

| 变量 / Variable | 默认值 / Default | 说明 / Description |
|---|---|---|
| POSTGRES_VERSION | 17 | PostgreSQL 镜像版本 / Image version |
| POSTGRES_PASSWORD | postgres | 超级用户密码 / Superuser password |
| POSTGRES_DB | test | 默认数据库名 / Default database name |
| POSTGRES_USER | postgres | 超级用户名 / Superuser name |

## 配置说明 / Configuration

自定义配置文件位于 `./conf/postgresql.conf`，包含以下默认设置：
Custom config at `./conf/postgresql.conf` with these defaults:

- `listen_addresses = '*'` - 监听所有网络接口 / Listen on all interfaces
- `max_connections = 100` - 最大连接数 / Max connections
- `shared_buffers = 256MB` - 共享缓冲区大小 / Shared buffer size

## 常用命令 / Common Commands

```bash
# 查看日志 / View logs
docker-compose logs -f

# 进入容器 / Enter container
docker-compose exec postgres psql -U postgres -d test

# 备份数据库 / Backup database
docker-compose exec postgres pg_dump -U postgres test > backup.sql

# 恢复数据库 / Restore database
cat backup.sql | docker-compose exec -T postgres psql -U postgres -d test
```

## 数据持久化 / Data Persistence

数据存储在 `./data/postgres` 目录下。
Data is stored in `./data/postgres`.
