# Nextcloud - Self-Hosted Cloud Storage

Nextcloud is a self-hosted productivity platform that keeps you in control of your data.

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
| Nextcloud | nextcloud | 8080 | Cloud storage platform |
| MySQL | nextcloud-mysql | - | Database backend |

## Directory Structure

```
nextcloud/
├── conf/
│   └── mysql/        # MySQL configuration
├── data/
│   ├── nextcloud/    # Nextcloud application data
│   └── mysql/        # MySQL data files
├── log/
├── docker-compose.yml
├── .env.example
└── README.md
```

## Usage

### Access Nextcloud

Open your browser and navigate to: `http://localhost:8080`

Login with the admin credentials set in `.env`:
- Username: `NEXTCLOUD_ADMIN_USER`
- Password: `NEXTCLOUD_ADMIN_PASSWORD`

### First Time Setup

On first access, Nextcloud will complete the installation automatically using the environment variables provided.

## Configuration

### Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| NEXTCLOUD_VERSION | Nextcloud version | 28 |
| NEXTCLOUD_ADMIN_USER | Admin username | admin |
| NEXTCLOUD_ADMIN_PASSWORD | Admin password | - |
| MYSQL_VERSION | MySQL version | 8.0 |
| MYSQL_ROOT_PASSWORD | MySQL root password | - |
| MYSQL_DATABASE | Database name | nextcloud |
| MYSQL_USER | Database user | nextcloud |
| MYSQL_PASSWORD | Database password | - |

### MySQL

Add custom MySQL configuration files to `conf/mysql/`.

## Backup

To backup Nextcloud data:

```bash
# Backup application data
tar -czf nextcloud-data-backup.tar.gz data/nextcloud/

# Backup database
docker exec nextcloud-mysql mysqldump -u root -p nextcloud > nextcloud-db-backup.sql
```
