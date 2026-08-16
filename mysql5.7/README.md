# MySQL 5.7

MySQL 5.7 is a stable relational database with good compatibility.

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
