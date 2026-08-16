# Golang

Go development environment with hot-reload support.

## Quick Start

```bash
cp .env.example .env
docker-compose up -d
```

## Usage

The container stays running in the background. Exec into it to build and run your Go application:

```bash
# Enter the container
docker exec -it golang bash

# Inside the container, build and run your app
go build -o app .
./app
```

Your Go source code lives in `./conf` on the host, which maps to `/go/src/app` in the container.

## Access

- Application: http://127.0.0.1:8080

## Volumes

| Host Path | Container Path | Description |
|-----------|---------------|-------------|
| `./conf` | `/go/src/app` | Go application source code |

## Configuration

| Variable | Default | Description |
|----------|---------|-------------|
| `GOLANG_VERSION` | `1.23` | Go Docker image version |
