# PostgreSQL Replication

PostgreSQL master-slave replication setup.

## Quick Start

```bash
cp .env.example .env
docker-compose up -d
```

## Access

- Master: `localhost:5432`
- Slave: `localhost:5433`

## Replication Setup

After starting the containers, configure the slave to replicate from the master:

```bash
# 1. Connect to the slave container
docker exec -it pg-slave bash

# 2. Stop PostgreSQL, clear data, and run pg_basebackup
pg_ctl stop -D /var/lib/postgresql/data
rm -rf /var/lib/postgresql/data/*
pg_basebackup -h pg-master -D /var/lib/postgresql/data -U replicator -Fp -Xs -P -R

# 3. Start PostgreSQL on the slave
pg_ctl start -D /var/lib/postgresql/data
```

## Configuration

Edit `.env` to customize:

| Variable | Default | Description |
|----------|---------|-------------|
| POSTGRES_VERSION | 17 | PostgreSQL image version |
| POSTGRES_PASSWORD | postgres | Master superuser password |
| REPLICATION_USER | replicator | Replication username |
| REPLICATION_PASSWORD | replicator | Replication password |

## Services

- **pg-master**: Primary PostgreSQL server (read/write)
- **pg-slave**: Replica PostgreSQL server (read-only)

## Directory Structure

```
postgresql-replication/
├── conf/          # PostgreSQL configuration
│   ├── master.conf    # Master server config
│   └── pg_hba.conf    # Client authentication config
├── data/          # Persistent data (master, slave)
├── log/           # Log files
├── docker-compose.yml
├── .env.example
└── README.md
```

---

# PostgreSQL 主从复制

PostgreSQL 主从复制（Master-Slave Replication）部署。

## 快速开始

```bash
cp .env.example .env
docker-compose up -d
```

## 访问地址

- Master: `localhost:5432`
- Slave: `localhost:5433`

## 复制配置步骤

启动容器后，需要配置从服务器从主服务器复制数据：

```bash
# 1. 进入从服务器容器
docker exec -it pg-slave bash

# 2. 停止 PostgreSQL，清空数据，执行 pg_basebackup
pg_ctl stop -D /var/lib/postgresql/data
rm -rf /var/lib/postgresql/data/*
pg_basebackup -h pg-master -D /var/lib/postgresql/data -U replicator -Fp -Xs -P -R

# 3. 启动从服务器的 PostgreSQL
pg_ctl start -D /var/lib/postgresql/data
```

## 配置说明

编辑 `.env` 文件进行自定义配置：

| 变量 | 默认值 | 说明 |
|------|--------|------|
| POSTGRES_VERSION | 17 | PostgreSQL 镜像版本 |
| POSTGRES_PASSWORD | postgres | 主服务器超级用户密码 |
| REPLICATION_USER | replicator | 复制用户名 |
| REPLICATION_PASSWORD | replicator | 复制用户密码 |

## 服务组件

- **pg-master**: 主 PostgreSQL 服务器（可读写）
- **pg-slave**: 从 PostgreSQL 服务器（只读）

## 目录结构

```
postgresql-replication/
├── conf/          # PostgreSQL 配置文件
│   ├── master.conf    # 主服务器配置
│   └── pg_hba.conf    # 客户端认证配置
├── data/          # 持久化数据 (master, slave)
├── log/           # 日志文件
├── docker-compose.yml
├── .env.example
└── README.md
```
