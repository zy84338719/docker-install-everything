# Portainer

Portainer Docker management UI / Portainer Docker 管理界面

## Quick Start / 快速开始

```bash
cp .env.example .env
docker-compose up -d
```

## Access / 访问

- URL: http://127.0.0.1:9000
- On first visit, set your admin password / 首次访问时设置管理员密码

## Ports / 端口

| Port | Description / 说明 |
|------|-------------------|
| 9000 | Web UI |

## Volumes / 数据卷

| Host Path | Container Path | Description / 说明 |
|-----------|---------------|-------------------|
| ./data/portainer | /data | Portainer data / Portainer 数据 |
| /var/run/docker.sock | /var/run/docker.sock | Docker socket |

## Environment Variables / 环境变量

See `.env.example` for available variables / 参见 `.env.example` 了解可用变量
