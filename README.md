# docker-install-everything

> install all environments using docker-compose.
> 使用 docker-compose 安装各种服务。

## 项目特色

- 仅依赖 docker 和 docker-compose，无需本地复杂环境。
- 支持软件和服务多，并且在持续新增。
- 每个文件夹一组(套)服务，根据需要安装即可。
- 所有的文件夹相互独立，无互相依赖，降低使用难度。

## 使用方法

```
git clone https://github.com/FX-Max/docker-install-everything.git
cd docker-install-everything
# 进入里想要安装的服务文件夹后，按照文件夹内的 README 文件介绍使用。
# 以安装 redis 为例：
cd redis
# 根据目录下 README 中的说明操作即可
docker-compose up -d redis
```

## 支持列表

- activemq

    简要说明: [Apache ActiveMQ](https://activemq.apache.org/) 是一款流行的开源消息中间件，支持多种协议（OpenWire, AMQP, MQTT, STOMP）。

- airflow

    简要说明: [Apache Airflow](https://airflow.apache.org/) 是一个可编程的工作流编排平台，用于批量数据处理的调度和监控。

- apollo

    简要说明: [Apollo](https://github.com/apolloconfig/apollo/) 是一款可靠的分布式配置管理中心，诞生于携程框架研发部。

- caddy

    简要说明: [Caddy](https://caddyserver.com/) 是一款自动启用 HTTPS 的现代 Web 服务器，配置简洁。

- cat

    简要说明: [CAT](https://github.com/dianping/cat) 是美团开源的实时应用监控平台（Central Application Tracking）。

- clickhouse

    简要说明: [ClickHouse](https://clickhouse.com/) 是一款高性能的列式分析型数据库，适用于 OLAP 场景。

- consul

    简要说明: [HashiCorp Consul](https://www.consul.io/) 是一款服务网格和发现工具，提供服务注册、健康检查和 KV 存储。

- dnmp

    简要说明: Docker + Nginx + MySQL + PHP 集成开发环境，快速搭建 LNMP 栈。

- gogs

    简要说明: [Gogs](https://gogs.io/) 是一款轻量级的自托管 Git 服务，易于安装和维护。

- golang

    简要说明: [Go](https://golang.org/) 语言开发环境，基于 Docker 快速搭建 Go 开发和运行环境。

- golang-mysql-redis

    简要说明: Go + MySQL + Redis 集成开发环境，适用于 Go 后端项目快速搭建。

- grafana

    简要说明: [Grafana](https://grafana.com/) 是一款开源的监控可视化平台，支持多种数据源。

- haproxy

    简要说明: [HAProxy](https://www.haproxy.org/) 是一款高性能的 TCP/HTTP 负载均衡器和代理服务器。

- kafka

    简要说明: [Apache Kafka](https://kafka.apache.org/) 是一款分布式流处理平台，用于构建实时数据管道和流应用。

- kong

    简要说明: [Kong](https://konghq.com/) 是一款云原生的 API 网关和微服务管理层。

- kuboard

    简要说明: [Kuboard](https://kuboard.cn/) 是一款 Kubernetes 图形化管理工具，提供直观的集群管理界面。

- loki

    简要说明: [Grafana Loki](https://grafana.com/oss/loki/) 是一款开源的日志聚合系统，与 Grafana 配合使用。

- memcached

    简要说明: [Memcached](https://memcached.org/) 是一款高性能的分布式内存对象缓存系统。

- mosquitto

    简要说明: [Eclipse Mosquitto](https://mosquitto.org/) 是一款轻量级的开源 MQTT 消息代理，适用于 IoT 场景。

- mysql5.7

    简要说明: [MySQL 5.7](https://dev.mysql.com/doc/refman/5.7/en/) 关系型数据库，适合需要兼容旧版本的项目。

- mysql8.0

    简要说明: [MySQL 8.0](https://dev.mysql.com/doc/refman/8.0/en/) 关系型数据库，最新稳定版本。

- mysql-master-slave

    简要说明: MySQL 主从复制架构，实现读写分离和数据备份。

- nacos

    简要说明: [Nacos](https://nacos.io/) 是阿里巴巴开源的服务发现和配置管理平台。

- nats

    简要说明: [NATS](https://nats.io/) 是一款高性能的云原生消息系统，支持 JetStream 持久化。

- nextcloud

    简要说明: [Nextcloud](https://nextcloud.com/) 是一款开源的自托管云存储和协作平台。

- nginx

    简要说明: [Nginx](https://nginx.org/) 是一款高性能的 HTTP 和反向代理服务器。

- nodejs

    简要说明: [Node.js](https://nodejs.org/) JavaScript 运行时开发环境。

- beanstalkd

    简要说明: [beanstalkd](https://beanstalkd.github.io/)，高性能，轻量级的分布式内存队列。

- drawio

    简要说明: [drawio](https://github.com/jgraph/drawio)是一款强大、免费的绘图工具。

- elk

    简要说明: 强大的日志收集和分析解决方案，Elasticsearch + Logstash + Kibana + Filebeat。

- emqx

    简要说明: [EMQX](https://www.emqx.io/) 是一款企业级的开源 MQTT 消息代理，支持大规模 IoT 设备连接。

- etcd

    简要说明: [etcd](https://etcd.io/) 是一款分布式键值存储系统，Kubernetes 的核心组件。

- excalidraw

    简要说明: [excalidraw](https://excalidraw.com/)，非常流行的画图工具，在线白板。

- gitlab

    简要说明: [gitlab](https://about.gitlab.com/)，非常流行的开源的Git代码仓库系统。

- jenkins

    简要说明: [jenkins](https://github.com/jenkinsci/jenkins) 是最流行的可扩展的持续集成引擎。

- jira

    简要说明: JIRA 是由 Atlassian 公司出品的，被业界公认为最好的项目管理和开发管理工具。

- jumpserver

    简要说明: [JumpServer](https://github.com/jumpserver/jumpserver) 是广受欢迎的开源堡垒机。

- jumpserver-all-in-one

    简要说明: 一键部署 jumpserver 全套环境，不依赖外部服务。

- Maxwell

    简要说明: [Maxwell](https://github.com/zendesk/maxwell)，一个能实时读取MySQL二进制日志Binlog，并生成JSON格式的消息，作为生产者发送给Kafka等系统的应用程序。

- MinIO

    简要说明: [MinIO](https://github.com/minio/minio)，基于 Golang 的一款开源的高性能分布式存储方案，兼容亚马逊S3云存储服务接口。本 docker 版本是单机版本。

- MinIO-cluster

    简要说明: [MinIO](https://github.com/minio/minio) 分布式集群版本。

- mongo

    简要说明: [MongoDB](https://www.mongodb.com/) 是一个基于分布式文件存储的数据库。

- mongo-express

    简要说明: [mongo-express](https://github.com/mongo-express/mongo-express) 是一个基于 Node.js 和 express 的开源的 MongoDB Web 管理工具。

- phpmyadmin

    简要说明: [phpmyadmin](https://github.com/phpmyadmin/phpmyadmin) 是一款基于 Web 的 MySQL 数据库管理工具。

- portainer

    简要说明: [Portainer](https://www.portainer.io/) 是一款轻量级的 Docker 可视化管理工具。

- postgresql

    简要说明: [PostgreSQL](https://www.postgresql.org/) 是一款功能强大的开源关系型数据库。

- postgresql-replication

    简要说明: PostgreSQL 主从复制架构，实现高可用和读写分离。

- rabbitmq

    简要说明: [RabbitMQ](https://www.rabbitmq.com/) 是一款使用Erlang语言开发的，实现AMQP(高级消息队列协议)的开源消息中间件。

- rabbitmq-management

    简要说明: [RabbitMQ](https://www.rabbitmq.com/) 带管理插件的版本，提供 Web 管理界面。

- rocketmq

    简要说明: [Apache RocketMQ](https://rocketmq.apache.org/) 是阿里巴巴开源的分布式消息和流处理平台。

- skywalking

    简要说明: [Apache SkyWalking](https://skywalking.apache.org/) 是一款开源的应用性能监控（APM）系统。

- tomcat

    简要说明: [Apache Tomcat](https://tomcat.apache.org/) 是一款流行的 Java Servlet 容器和 Web 服务器。

- xxl-job

    简要说明: [XXL-JOB](https://www.xuxueli.com/xxl-job/) 是一款分布式任务调度平台，支持动态任务管理。

- zabbix

    简要说明: [Zabbix](https://www.zabbix.com/) 是一款企业级的开源监控解决方案。

- zeromq

    简要说明: [ZeroMQ](https://zeromq.org/) 是一款高性能的异步消息传递库，常用于分布式系统。

- redis

    简要说明: 快速搭建 [redis](https://github.com/redis/redis) 服务。

- redis-cluster

    简要说明: 快速搭建 [redis](https://github.com/redis/redis) 集群服务，1主多从多哨兵。

- sentry

    简要说明: [Sentry](https://sentry.io/) 是一款开源的实时错误追踪和监控平台。

- traefik

    简要说明: [Traefik](https://traefik.io/) 是一款云原生的反向代理和负载均衡器，自动发现 Docker 服务。

- vault

    简要说明: [HashiCorp Vault](https://www.vaultproject.io/) 是一款密钥和敏感数据管理工具。

- wikijs

    简要说明: 自建开源的wiki/文档管理系统 [wiki.js](https://js.wiki/)。

- wordpress

    简要说明: [wordpress](https://github.com/WordPress/WordPress)，最流行的免费建站系统。

- yapi

    简要说明: [YApi](https://github.com/YMFE/yapi) 是一个可本地部署的、打通前后端及QA的、可视化的接口管理平台。

- Yearning

	简要说明: [Yearning](https://github.com/cookieY/Yearning)，基于 Go 的开箱即用的MYSQL SQL审核工具。


## 欢迎加入

- 如果在使用本项目的过程中发现了问题或有建议，欢迎交流提 issue。
- 欢迎 fork 代码，不断改进优化。

## 感谢关注

如果项目对您有帮助，请帮忙点点小星星，谢谢。

## Support

IDE for this project is supported by [Jetbrains](https://jb.gg/OpenSourceSupport).

[![](https://resources.jetbrains.com/storage/products/company/brand/logos/jb_beam.png)](https://jb.gg/OpenSourceSupport)
