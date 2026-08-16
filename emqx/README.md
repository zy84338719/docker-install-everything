# EMQX

EMQX MQTT broker / EMQX MQTT 消息代理

## Quick Start / 快速开始

```bash
cp .env.example .env
docker-compose up -d
```

## Access / 访问

- Dashboard: http://127.0.0.1:18083
- Default credentials / 默认账号: admin / public

## Ports / 端口

| Port | Protocol | Description / 说明 |
|------|----------|-------------------|
| 1883 | TCP | MQTT |
| 8083 | WebSocket | MQTT over WebSocket |
| 8084 | WebSocket (SSL) | MQTT over WebSocket (SSL) |
| 8883 | TCP (SSL) | MQTT over TLS |
| 18083 | HTTP | Dashboard / 管理面板 |

## Volumes / 数据卷

| Host Path | Container Path | Description / 说明 |
|-----------|---------------|-------------------|
| ./data/emqx | /opt/emqx/data | EMQX data / EMQX 数据 |
| ./log/emqx | /opt/emqx/log | EMQX logs / EMQX 日志 |

## Environment Variables / 环境变量

| Variable | Default | Description / 说明 |
|----------|---------|-------------------|
| EMQX_VERSION | 5.8 | EMQX image version / 镜像版本 |

## Test Connection / 测试连接

```bash
# Subscribe / 订阅
mosquitto_sub -h 127.0.0.1 -t test/topic

# Publish / 发布
mosquitto_pub -h 127.0.0.1 -t test/topic -m "hello"
```
