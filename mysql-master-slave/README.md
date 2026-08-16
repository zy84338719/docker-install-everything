# MySQL Master-Slave Replication

MySQL master-slave replication setup with Docker for read-write separation.

## Usage

```bash
cp .env.example .env
docker-compose up -d
```

## Replication Setup

### Step 1: Create replication user on master

```bash
docker exec -it mysql-master mysql -u root -p

CREATE USER 'repl'@'%' IDENTIFIED BY 'repl_password';
GRANT REPLICATION SLAVE ON *.* TO 'repl'@'%';
FLUSH PRIVILEGES;

SHOW MASTER STATUS;
```

Note the `File` and `Position` values from `SHOW MASTER STATUS`.

### Step 2: Configure slave

```bash
docker exec -it mysql-slave mysql -u root -p

CHANGE MASTER TO
  MASTER_HOST='mysql-master',
  MASTER_PORT=3306,
  MASTER_USER='repl',
  MASTER_PASSWORD='repl_password',
  MASTER_LOG_FILE='mysql-bin.000001',
  MASTER_LOG_POS=154;

START SLAVE;
SHOW SLAVE STATUS\G
```

### Step 3: Verify replication

```bash
# On master
docker exec -it mysql-master mysql -u root -p
USE test;
CREATE TABLE test (id INT PRIMARY KEY, name VARCHAR(50));
INSERT INTO test VALUES (1, 'hello');

# On slave
docker exec -it mysql-slave mysql -u root -p
USE test;
SELECT * FROM test;
```

## Directory Structure

- `conf/` - Configuration files (master.cnf, slave.cnf)
- `data/` - Data persistence (master/, slave/)
- `log/` - Log files (master/, slave/)
