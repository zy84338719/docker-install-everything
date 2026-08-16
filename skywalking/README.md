# SkyWalking

Apache SkyWalking Application Performance Monitor (APM) system.

## Quick Start

```bash
cp .env.example .env
# Edit .env with your desired configuration
docker-compose up -d
```

## Access

- Web UI: http://127.0.0.1:8080
- gRPC API: `localhost:11800`
- REST API: http://127.0.0.1:12800

## Ports

| Port | Description |
|------|-------------|
| 11800 | OAP gRPC service port (agent reporting) |
| 12800 | OAP REST API port |
| 8080 | SkyWalking Web UI |

## Volumes

| Host Path | Container Path | Description |
|-----------|---------------|-------------|
| ./data/oap | /skywalking/data | OAP data storage |

## Notes

- Uses H2 as the default storage backend (embedded, no external database needed).
- For production, switch to Elasticsearch or BanyanDB by setting `SW_STORAGE`.
- Configure your application agents to report to `localhost:11800` (gRPC).
