# Sentry

Sentry self-hosted error tracking and performance monitoring.

## Quick Start

```bash
cp .env.example .env
# Edit .env and set a strong SENTRY_SECRET_KEY
docker-compose up -d
```

## Access

- Web UI: http://127.0.0.1:9000

## Configuration

Edit `.env` to customize:

| Variable | Default | Description |
|----------|---------|-------------|
| SENTRY_VERSION | latest | Sentry image version |
| POSTGRES_VERSION | 17 | PostgreSQL image version |
| REDIS_VERSION | 7.4 | Redis image version |
| SENTRY_SECRET_KEY | your-secret-key-here | Secret key for Sentry (change this!) |
| SENTRY_DB_USER | sentry | Database username |
| SENTRY_DB_PASSWORD | sentry | Database password (change this!) |

## Services

- **sentry-web**: Sentry web frontend
- **sentry-worker**: Sentry background worker
- **sentry-db**: PostgreSQL database
- **sentry-redis**: Redis cache

## Directory Structure

```
sentry/
├── conf/          # Configuration files
├── data/          # Persistent data (postgres, redis)
├── log/           # Log files
├── docker-compose.yml
├── .env.example
└── README.md
```

---

# Sentry

Sentry 自托管错误追踪和性能监控服务。

## 快速开始

```bash
cp .env.example .env
# 编辑 .env 文件，设置一个强密码作为 SENTRY_SECRET_KEY
docker-compose up -d
```

## 访问地址

- Web UI: http://127.0.0.1:9000

## 配置说明

编辑 `.env` 文件进行自定义配置：

| 变量 | 默认值 | 说明 |
|------|--------|------|
| SENTRY_VERSION | latest | Sentry 镜像版本 |
| POSTGRES_VERSION | 17 | PostgreSQL 镜像版本 |
| REDIS_VERSION | 7.4 | Redis 镜像版本 |
| SENTRY_SECRET_KEY | your-secret-key-here | Sentry 密钥（请务必修改！） |
| SENTRY_DB_USER | sentry | 数据库用户名 |
| SENTRY_DB_PASSWORD | sentry | 数据库密码（请务必修改！） |

## 服务组件

- **sentry-web**: Sentry Web 前端
- **sentry-worker**: Sentry 后台工作者
- **sentry-db**: PostgreSQL 数据库
- **sentry-redis**: Redis 缓存

## 目录结构

```
sentry/
├── conf/          # 配置文件
├── data/          # 持久化数据 (postgres, redis)
├── log/           # 日志文件
├── docker-compose.yml
├── .env.example
└── README.md
```
