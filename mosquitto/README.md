# Mosquitto

Eclipse Mosquitto MQTT broker / Eclipse Mosquitto MQTT 消息代理

## Quick Start / 快速开始

```bash
cp .env.example .env
docker-compose up -d
```

## Access / 访问

- MQTT Port: 1883
- WebSocket Port: 9001

## Ports / 端口

| Port | Protocol | Description / 说明 |
|------|----------|-------------------|
| 1883 | TCP | MQTT |
| 9001 | WebSocket | MQTT over WebSocket |

## Volumes / 数据卷

| Host Path | Container Path | Description / 说明 |
|-----------|---------------|-------------------|
| ./conf/mosquitto.conf | /mosquitto/config/mosquitto.conf | Mosquitto config / Mosquitto 配置 |
| ./data/mosquitto | /mosquitto/data | Mosquitto data / Mosquitto 数据 |
| ./log/mosquitto | /mosquitto/log | Mosquitto logs / Mosquitto 日志 |

## Environment Variables / 环境变量

| Variable | Default | Description / 说明 |
|----------|---------|-------------------|
| MOSQUITTO_VERSION | 2 | Mosquitto image version / 镜像版本 |

## Test Connection / 测试连接

```bash
# Subscribe / 订阅
mosquitto_sub -h 127.0.0.1 -t test/topic

# Publish / 发布
mosquitto_pub -h 127.0.0.1 -t test/topic -m "hello"
```
