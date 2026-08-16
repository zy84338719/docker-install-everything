# Apache Kafka

Apache Kafka is a distributed event streaming platform capable of handling trillions of events per day.

## Services

- **kafka**: Apache Kafka broker
- **zookeeper**: Zookeeper for Kafka coordination

## Quick Start

```bash
cp .env.example .env
# Edit .env with your settings
docker-compose up -d
```

## Access

- Kafka broker: localhost:9092
- Zookeeper: localhost:2181

## Ports

| Port | Service    |
|------|------------|
| 9092 | Kafka      |
| 9093 | Controller |
| 2181 | Zookeeper  |

## Data Volumes

- `./data/kafka` - Kafka data
- `./data/zookeeper` - Zookeeper data

## Configuration

- `./conf/server.properties` - Kafka broker configuration

## Usage Examples

Create a topic:
```bash
docker exec kafka kafka-topics.sh --create --topic test --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1
```

Produce messages:
```bash
docker exec -it kafka kafka-console-producer.sh --broker-list localhost:9092 --topic test
```

Consume messages:
```bash
docker exec -it kafka kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic test --from-beginning
```
