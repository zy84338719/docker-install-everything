# Gogs

Self-hosted Git service built with Go.

## Quick Start

```bash
cp .env.example .env
docker-compose up -d
```

## Access

- Web UI: http://127.0.0.1:10880
- SSH: `ssh -p 10022 git@127.0.0.1`

## Volumes

| Host Path | Container Path | Description |
|-----------|---------------|-------------|
| `./data/gogs` | `/data` | Gogs data (repositories, config, database) |

## Configuration

| Variable | Default | Description |
|----------|---------|-------------|
| `GOGS_VERSION` | `latest` | Gogs Docker image version |

## First Run

On first access, Gogs will present an installation wizard where you can configure:

- Database type (SQLite recommended for small teams)
- Repository root path
- HTTP/SSH settings
- Admin account
