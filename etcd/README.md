# etcd - 分布式键值存储 / Distributed Key-Value Store

## 概述 / Overview

etcd 是一个分布式、可靠的键值存储系统，用于分布式系统中最关键的数据存储。
etcd is a distributed, reliable key-value store for the most critical data of a distributed system.

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

使用 etcdctl 测试 / Test with etcdctl:
```bash
# 设置值 / Set value
etcdctl --endpoints=http://127.0.0.1:2379 put /message "Hello etcd"

# 获取值 / Get value
etcdctl --endpoints=http://127.0.0.1:2379 get /message

# 列出所有键 / List all keys
etcdctl --endpoints=http://127.0.0.1:2379 get / --prefix
```

访问 API / Access API:
```bash
curl http://127.0.0.1:2379/version
curl http://127.0.0.1:2379/v3/kv/range -X POST -d '{"key": "L21lc3NhZ2U="}'
```

## 端口说明 / Ports

| 端口 / Port | 用途 / Purpose |
|---|---|
| 2379 | 客户端通信端口 / Client communication |
| 2380 | 节点间通信端口 / Peer communication |

## 环境变量 / Environment Variables

| 变量 / Variable | 默认值 / Default | 说明 / Description |
|---|---|---|
| ETCD_VERSION | 3.5 | etcd 镜像版本 / etcd image version |

## 常用命令 / Common Commands

```bash
# 查看日志 / View logs
docker-compose logs -f

# 进入容器 / Enter container
docker-compose exec etcd etcdctl endpoint health

# 查看状态 / Check status
docker-compose ps

# 查看集群状态 / Check cluster health
etcdctl --endpoints=http://127.0.0.1:2379 endpoint health
```

## 数据持久化 / Data Persistence

数据存储在 `./data/etcd` 目录下。
Data is stored in `./data/etcd`.
