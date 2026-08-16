# Golang + MySQL + Redis

Full-stack Go development environment with MySQL and Redis.

## Quick Start

```bash
cp .env.example .env
docker-compose up -d
```

## Services

| Service | Container | Port | Description |
|---------|-----------|------|-------------|
| Golang | golang-app | 8080 | Go development container |
| MySQL | golang-mysql | 3306 | MySQL database |
| Redis | golang-redis | 6379 | Redis cache |

## Usage

Exec into the Go container to build and run your application:

```bash
# Enter the Go container
docker exec -it golang-app bash

# Inside the container, build and run your app
go build -o app .
./app
```

### Connecting to MySQL

- Host: `mysql` (use container name)
- Port: `3306`
- User: `root`
- Password: see `MYSQL_ROOT_PASSWORD` in `.env`
- Database: see `MYSQL_DATABASE` in `.env`

### Connecting to Redis

- Host: `redis` (use container name)
- Port: `6379`

## Volumes

| Host Path | Container Path | Description |
|-----------|---------------|-------------|
| `./conf` | `/go/src/app` | Go application source code |
| `./data/mysql` | `/var/lib/mysql` | MySQL data persistence |
| `./data/redis` | `/data` | Redis data persistence |
| `./conf/my.cnf` | `/etc/mysql/conf.d/my.cnf` | MySQL configuration |

## Configuration

| Variable | Default | Description |
|----------|---------|-------------|
| `GOLANG_VERSION` | `1.23` | Go Docker image version |
| `MYSQL_VERSION` | `8.0` | MySQL Docker image version |
| `MYSQL_ROOT_PASSWORD` | `root` | MySQL root password |
| `MYSQL_DATABASE` | `golang` | Default database name |
| `REDIS_VERSION` | `7.4` | Redis Docker image version |
