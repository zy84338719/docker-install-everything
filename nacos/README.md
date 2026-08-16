# Nacos

Alibaba Nacos service discovery and configuration management.

## Quick Start

```bash
cp .env.example .env
# Edit .env with your desired configuration
docker-compose up -d
```

## Access

- Web Console: http://127.0.0.1:8848/nacos
- Default credentials: `nacos` / `nacos`

## Ports

| Port | Description |
|------|-------------|
| 8848 | Nacos HTTP API and Web Console |
| 9848 | gRPC communication port |
| 9849 | gRPC communication port for server-to-server |

## Volumes

| Host Path | Container Path | Description |
|-----------|---------------|-------------|
| ./data/nacos | /home/nacos/data | Nacos data |
| ./log/nacos | /home/nacos/logs | Nacos logs |
| ./data/mysql | /var/lib/mysql | MySQL data |

## Notes

- Uses MySQL as the backend database (included as nacos-db service).
- Runs in standalone mode by default.
- For production, consider using an external MySQL instance and clustering mode.
