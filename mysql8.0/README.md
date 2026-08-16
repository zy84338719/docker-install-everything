# MySQL 8.0

MySQL 8.0 is the latest major version with improved performance, JSON support, and window functions.

## Usage

```bash
cp .env.example .env
docker-compose up -d
```

## Connect

```bash
mysql -h127.0.0.1 -P3306 -uroot -proot
```

## Directory Structure

- `conf/` - Configuration files
- `data/` - Data persistence
- `log/` - Log files
