# Memcached - 分布式内存缓存系统 / Distributed Memory Cache

## 概述 / Overview

Memcached 是一个高性能的分布式内存对象缓存系统，用于加速动态 Web 应用。
Memcached is a high-performance distributed memory object caching system for speeding up dynamic web applications.

## 快速开始 / Quick Start

```bash
# 复制环境变量配置 / Copy environment config
cp .env.example .env

# 启动服务 / Start service
docker-compose up -d

# 停止服务 / Stop service
docker-compose down
```

## 测试连接 / Test Connection

使用 telnet 测试 / Test with telnet:
```bash
telnet 127.0.0.1 11211
```

使用 nc 测试 / Test with nc:
```bash
echo "stats" | nc 127.0.0.1 11211
```

## 端口说明 / Ports

| 端口 / Port | 用途 / Purpose |
|---|---|
| 11211 | Memcached 服务端口 / Memcached service port |

## 环境变量 / Environment Variables

| 变量 / Variable | 默认值 / Default | 说明 / Description |
|---|---|---|
| MEMCACHED_VERSION | 1.6 | Memcached 镜像版本 / Image version |
| MEMCACHED_MEMORY | 64 | 内存限制 (MB) / Memory limit (MB) |

## 常用操作 / Common Operations

```bash
# 设置值 / Set value
echo -e "set mykey 0 3600 5\r\nhello\r" | nc 127.0.0.1 11211

# 获取值 / Get value
echo -e "get mykey\r" | nc 127.0.0.1 11211

# 查看状态 / View stats
echo -e "stats\r" | nc 127.0.0.1 11211

# 清空所有 / Flush all
echo -e "flush_all\r" | nc 127.0.0.1 11211
```

## 常用命令 / Common Commands

```bash
# 查看日志 / View logs
docker-compose logs -f

# 重启服务 / Restart service
docker-compose restart

# 查看状态 / Check status
docker-compose ps
```
