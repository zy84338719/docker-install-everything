# XXL-JOB

XXL-JOB distributed task scheduling platform.

## Quick Start

```bash
cp .env.example .env
# Edit .env with your desired configuration
docker-compose up -d
```

## Access

- Admin Console: http://127.0.0.1:8080/xxl-job-admin
- Default credentials: `admin` / `123456`

## Ports

| Port | Description |
|------|-------------|
| 8080 | XXL-JOB Admin web console |

## Volumes

| Host Path | Container Path | Description |
|-----------|---------------|-------------|
| ./data/xxl-job | /data/applogs | XXL-JOB application logs |
| ./data/mysql | /var/lib/mysql | MySQL data |

## Notes

- Uses MySQL as the backend database (included as xxl-job-db service).
- The XXL-JOB tables will be auto-created on first startup.
- Register your executors with the admin console to start scheduling jobs.
