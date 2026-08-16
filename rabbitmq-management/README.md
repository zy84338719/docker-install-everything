# RabbitMQ Management

RabbitMQ message broker with management plugin enabled.

## Quick Start

```bash
cp .env.example .env
docker-compose up -d
```

## Access

- Management UI: http://127.0.0.1:15672
- AMQP: `localhost:5672`
- Default credentials: `guest` / `guest`

## Configuration

Edit `.env` to customize:

| Variable | Default | Description |
|----------|---------|-------------|
| RABBITMQ_VERSION | 4.0 | RabbitMQ image version |
| RABBITMQ_DEFAULT_USER | guest | Default admin username |
| RABBITMQ_DEFAULT_PASS | guest | Default admin password |

## Directory Structure

```
rabbitmq-management/
├── conf/          # RabbitMQ configuration (rabbitmq.conf)
├── data/          # Persistent data storage
├── log/           # Log files
├── docker-compose.yml
├── .env.example
└── README.md
```

---

# RabbitMQ Management

RabbitMQ 消息队列服务（含管理插件）。

## 快速开始

```bash
cp .env.example .env
docker-compose up -d
```

## 访问地址

- Management UI: http://127.0.0.1:15672
- AMQP: `localhost:5672`
- 默认凭据: `guest` / `guest`

## 配置说明

编辑 `.env` 文件进行自定义配置：

| 变量 | 默认值 | 说明 |
|------|--------|------|
| RABBITMQ_VERSION | 4.0 | RabbitMQ 镜像版本 |
| RABBITMQ_DEFAULT_USER | guest | 默认管理员用户名 |
| RABBITMQ_DEFAULT_PASS | guest | 默认管理员密码 |

## 目录结构

```
rabbitmq-management/
├── conf/          # RabbitMQ 配置文件 (rabbitmq.conf)
├── data/          # 持久化数据存储
├── log/           # 日志文件
├── docker-compose.yml
├── .env.example
└── README.md
```
