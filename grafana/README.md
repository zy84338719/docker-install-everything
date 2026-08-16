# Grafana

Grafana monitoring dashboard / Grafana 监控仪表盘

## Quick Start / 快速开始

```bash
cp .env.example .env
docker-compose up -d
```

## Access / 访问

- URL: http://127.0.0.1:3000
- Default credentials / 默认账号: admin / admin

## Ports / 端口

| Port | Description / 说明 |
|------|-------------------|
| 3000 | Web UI |

## Volumes / 数据卷

| Host Path | Container Path | Description / 说明 |
|-----------|---------------|-------------------|
| ./data/grafana | /var/lib/grafana | Grafana data / Grafana 数据 |
| ./conf/grafana.ini | /etc/grafana/grafana.ini | Grafana config / Grafana 配置 |

## Environment Variables / 环境变量

| Variable | Default | Description / 说明 |
|----------|---------|-------------------|
| GRAFANA_VERSION | 11.4.0 | Grafana image version / 镜像版本 |
| GF_ADMIN_USER | admin | Admin username / 管理员用户名 |
| GF_ADMIN_PASSWORD | admin | Admin password / 管理员密码 |
