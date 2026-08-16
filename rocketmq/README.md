# RocketMQ

Apache RocketMQ distributed messaging and streaming platform.

## Quick Start

```bash
cp .env.example .env
# Edit .env with your desired configuration
docker-compose up -d
```

## Access

- Dashboard: http://127.0.0.1:8080
- NameServer: `localhost:9876`

## Ports

| Port | Description |
|------|-------------|
| 9876 | NameServer port |
| 10911 | Broker port |
| 10909 | Broker VIP port |
| 8080 | RocketMQ Dashboard |

## Volumes

| Host Path | Container Path | Description |
|-----------|---------------|-------------|
| ./data/namesrv | /root/logs | NameServer data |
| ./log/namesrv | /root/logs | NameServer logs |
| ./data/broker | /root/store | Broker message store |
| ./log/broker | /root/logs | Broker logs |
| ./conf/broker.conf | /opt/rocketmq/conf/broker.conf | Broker configuration |

## Configuration

- Broker config: `conf/broker.conf`
- The dashboard provides a web UI for monitoring topics, consumers, and messages.
