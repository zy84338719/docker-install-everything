# Traefik

Traefik cloud-native reverse proxy and load balancer.

## Quick Start

```bash
cp .env.example .env
docker-compose up -d
```

## Access

- Dashboard: http://127.0.0.1:8080
- HTTP: http://127.0.0.1:80
- HTTPS: https://127.0.0.1:443

## Configuration

Edit `.env` to customize:

| Variable | Default | Description |
|----------|---------|-------------|
| TRAEFIK_VERSION | v3.2 | Traefik image version |

## Directory Structure

```
traefik/
├── conf/          # Traefik configuration (traefik.yml)
├── data/          # Persistent data storage
├── log/           # Log files
├── docker-compose.yml
├── .env.example
└── README.md
```

---

# Traefik

Traefik 云原生反向代理和负载均衡器。

## 快速开始

```bash
cp .env.example .env
docker-compose up -d
```

## 访问地址

- Dashboard: http://127.0.0.1:8080
- HTTP: http://127.0.0.1:80
- HTTPS: https://127.0.0.1:443

## 配置说明

编辑 `.env` 文件进行自定义配置：

| 变量 | 默认值 | 说明 |
|------|--------|------|
| TRAEFIK_VERSION | v3.2 | Traefik 镜像版本 |

## 目录结构

```
traefik/
├── conf/          # Traefik 配置文件 (traefik.yml)
├── data/          # 持久化数据存储
├── log/           # 日志文件
├── docker-compose.yml
├── .env.example
└── README.md
```
