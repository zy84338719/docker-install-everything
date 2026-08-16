# HAProxy

HAProxy load balancer and reverse proxy.

## Quick Start

```bash
cp .env.example .env
docker-compose up -d
```

## Access

- Stats dashboard: http://127.0.0.1:8404/stats
- Frontend: http://127.0.0.1:80

Default stats credentials: `admin` / `admin` (change in `conf/haproxy.cfg`).

## Volumes

| Host Path | Container Path | Description |
|-----------|---------------|-------------|
| `./conf/haproxy.cfg` | `/usr/local/etc/haproxy/haproxy.cfg` | HAProxy configuration (read-only) |
| `./log` | `/var/log/haproxy` | HAProxy log files |

## Configuration

Edit `conf/haproxy.cfg` to add your backend servers and adjust load balancing settings.

| Variable | Default | Description |
|----------|---------|-------------|
| `HAPROXY_VERSION` | `3.2` | HAProxy Docker image version |
