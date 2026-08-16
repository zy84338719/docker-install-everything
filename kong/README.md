# kong

Kong API Gateway，基于 PostgreSQL 存储，包含数据库迁移步骤。

## Usage

```bash
cp .env.example .env
docker-compose up -d
```

等待 kong-migration 完成后，Kong 会自动启动。

验证 Kong 是否运行正常

```bash
curl -i http://localhost:8001/
```

测试代理

```bash
curl -i http://localhost:8000/
```

访问 Kong Admin API（HTTPS）

```bash
curl -k https://localhost:8444/
```

查看日志

```bash
docker logs -f kong
```

## 端口说明

| 端口 | 用途 |
|------|------|
| 8000 | HTTP 代理 |
| 8443 | HTTPS 代理 |
| 8001 | Admin API (HTTP) |
| 8444 | Admin API (HTTPS) |
| 5432 | PostgreSQL |
