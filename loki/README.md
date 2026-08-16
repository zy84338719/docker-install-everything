# Loki

Grafana Loki log aggregation / Grafana Loki 日志聚合系统

## Quick Start / 快速开始

```bash
cp .env.example .env
docker-compose up -d
```

## Access / 访问

- URL: http://127.0.0.1:3100
- Push logs with Promtail or Docker logging driver / 使用 Promtail 或 Docker 日志驱动推送日志

## Ports / 端口

| Port | Description / 说明 |
|------|-------------------|
| 3100 | Loki HTTP API |

## Volumes / 数据卷

| Host Path | Container Path | Description / 说明 |
|-----------|---------------|-------------------|
| ./conf/loki-config.yml | /etc/loki/local-config.yaml | Loki config / Loki 配置 |
| ./data/loki | /loki | Loki data / Loki 数据 |

## Environment Variables / 环境变量

| Variable | Default | Description / 说明 |
|----------|---------|-------------------|
| LOKI_VERSION | 3.3.2 | Loki image version / 镜像版本 |

## Integration / 集成

Loki is commonly used with Grafana and Promtail / Loki 通常与 Grafana 和 Promtail 配合使用:

1. Deploy Grafana / 部署 Grafana
2. Add Loki as a data source in Grafana / 在 Grafana 中添加 Loki 数据源
3. Deploy Promtail to ship logs / 部署 Promtail 发送日志
