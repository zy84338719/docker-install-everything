# HashiCorp Vault

HashiCorp Vault secrets management service.

## Quick Start

```bash
cp .env.example .env
docker-compose up -d
```

## Access

- Web UI: http://127.0.0.1:8200
- Root Token: `root` (default, change in production)

## Configuration

Edit `.env` to customize:

| Variable | Default | Description |
|----------|---------|-------------|
| VAULT_VERSION | 1.18 | Vault image version |
| VAULT_DEV_ROOT_TOKEN | root | Root token for dev mode |

## Directory Structure

```
vault/
├── conf/          # Configuration files
├── data/          # Persistent data storage
├── log/           # Log files
├── docker-compose.yml
├── .env.example
└── README.md
```

---

# HashiCorp Vault

HashiCorp Vault 密钥管理服务。

## 快速开始

```bash
cp .env.example .env
docker-compose up -d
```

## 访问地址

- Web UI: http://127.0.0.1:8200
- Root Token: `root`（默认值，生产环境请修改）

## 配置说明

编辑 `.env` 文件进行自定义配置：

| 变量 | 默认值 | 说明 |
|------|--------|------|
| VAULT_VERSION | 1.18 | Vault 镜像版本 |
| VAULT_DEV_ROOT_TOKEN | root | 开发模式的 Root Token |

## 目录结构

```
vault/
├── conf/          # 配置文件
├── data/          # 持久化数据存储
├── log/           # 日志文件
├── docker-compose.yml
├── .env.example
└── README.md
```
