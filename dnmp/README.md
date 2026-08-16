# DNMP - Docker + Nginx + MySQL + PHP

A Docker-based LNMP (Linux + Nginx + MySQL + PHP) development environment.

## Quick Start

```bash
# Copy environment file
cp .env.example .env

# Edit .env with your settings
vim .env

# Start services
docker-compose up -d

# Stop services
docker-compose down
```

## Services

| Service | Container | Port | Description |
|---------|-----------|------|-------------|
| Nginx | dnmp-nginx | 80, 443 | Web server |
| MySQL | dnmp-mysql | 3306 | Database |
| PHP-FPM | dnmp-php | 9000 | PHP processor |

## Directory Structure

```
dnmp/
├── conf/
│   ├── nginx/        # Nginx configuration
│   ├── mysql/        # MySQL configuration
│   └── php/          # PHP configuration
├── data/
│   ├── nginx/        # Web root directory
│   ├── mysql/        # MySQL data files
│   └── php/          # PHP data
├── log/
│   ├── nginx/        # Nginx logs
│   ├── mysql/        # MySQL logs
│   └── php/          # PHP logs
├── docker-compose.yml
├── .env.example
└── README.md
```

## Usage

### Access Nginx

Place your web files in `data/nginx/` directory.

Access via: `http://localhost`

### Connect to MySQL

```bash
# Using MySQL client
mysql -h 127.0.0.1 -P 3306 -u app_user -p

# Using Docker exec
docker exec -it dnmp-mysql mysql -u root -p
```

### PHP Extensions

To install additional PHP extensions, create a Dockerfile in `conf/php/`:

```dockerfile
FROM php:8.2-fpm
RUN docker-php-ext-install pdo_mysql mysqli
```

## Configuration

### Nginx

Edit `conf/nginx/default.conf` to configure virtual hosts.

### MySQL

Add custom MySQL configuration files to `conf/mysql/`.

### PHP

Add custom PHP configuration files to `conf/php/` (e.g., `php.ini`).
