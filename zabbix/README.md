# Zabbix Monitoring Platform

Zabbix is an enterprise-class open source distributed monitoring solution.

## Services

- **zabbix-server**: Zabbix server for data collection and processing
- **zabbix-web**: Zabbix web frontend (Nginx + MySQL)
- **mysql**: MySQL database backend

## Quick Start

```bash
cp .env.example .env
# Edit .env with your settings
docker-compose up -d
```

## Access

- Web UI: http://localhost:8080
- Default login: Admin / zabbix
- Server port: 10051

## Ports

| Port  | Service       |
|-------|---------------|
| 8080  | Zabbix Web UI |
| 10051 | Zabbix Server |
| 3306  | MySQL         |

## Data Volumes

- `./data/mysql` - MySQL data
- `./data/zabbix-server` - Zabbix server data
- `./log/zabbix-server` - Zabbix server logs

## Configuration

- `./conf/my.cnf` - MySQL configuration
- `./conf/nginx.conf` - Nginx configuration for Zabbix web
