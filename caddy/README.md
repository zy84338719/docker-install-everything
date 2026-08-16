# Caddy Docker 安装

## 简介

Caddy 是一个现代化的 Web 服务器，支持自动 HTTPS，配置简单。

## 快速开始

```bash
# 1. 复制环境变量文件
cp .env.example .env

# 2. 修改配置文件
vim conf/Caddyfile

# 3. 启动服务
docker-compose up -d

# 4. 访问 Caddy
# http://localhost
```

## 目录结构

```
caddy/
├── docker-compose.yml
├── .env.example
├── README.md
├── conf/          # Caddy 配置文件
│   └── Caddyfile  # 主配置文件
├── data/          # 证书和数据存储
├── config/        # 运行时配置
└── log/           # 日志目录
```

## 环境变量

| 变量 | 默认值 | 说明 |
|------|--------|------|
| CADDY_VERSION | 2.7 | Caddy 版本 |

## 常用命令

```bash
# 启动服务
docker-compose up -d

# 停止服务
docker-compose down

# 查看日志
docker-compose logs -f

# 重新加载配置
docker exec caddy caddy reload --config /etc/caddy/Caddyfile

# 进入容器
docker exec -it caddy sh
```

## 配置说明

### 反向代理

```
example.com {
    reverse_proxy backend:8080
}
```

### 静态文件

```
example.com {
    root * /srv
    file_server
}
```

### 自动 HTTPS

Caddy 会自动为配置的域名申请 Let's Encrypt 证书。

## 注意事项

1. 自动 HTTPS 需要域名指向服务器 IP
2. 80 和 443 端口必须开放
3. 证书存储在 data 目录，不要删除
