# Nginx

Nginx web server and reverse proxy.

## Quick Start

```bash
cp .env.example .env
# Edit .env with your desired configuration
docker-compose up -d
```

## Access

- HTTP: http://127.0.0.1
- HTTPS: https://127.0.0.1 (requires SSL certificate configuration)

## Ports

| Port | Description |
|------|-------------|
| 80 | HTTP |
| 443 | HTTPS |

## Volumes

| Host Path | Container Path | Description |
|-----------|---------------|-------------|
| ./conf/nginx.conf | /etc/nginx/nginx.conf | Main Nginx configuration |
| ./conf/conf.d | /etc/nginx/conf.d | Additional server block configs |
| ./html | /usr/share/nginx/html | Web root directory |
| ./logs | /var/log/nginx | Nginx access and error logs |

## Configuration

- Main config: `conf/nginx.conf`
- Server blocks: `conf/conf.d/*.conf`
- Place your static files in the `html/` directory.
- Add additional virtual host configs as `.conf` files in `conf/conf.d/`.
