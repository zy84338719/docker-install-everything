# Tomcat Docker 安装

## 简介

Apache Tomcat 是一个开源的 Java Servlet 容器，用于运行 Java Web 应用程序。

## 快速开始

```bash
# 1. 复制环境变量文件
cp .env.example .env

# 2. 启动服务
docker-compose up -d

# 3. 访问 Tomcat
# http://localhost:8080
```

## 目录结构

```
tomcat/
├── docker-compose.yml
├── .env.example
├── README.md
├── conf/          # Tomcat 配置文件
├── data/          # 数据目录
├── log/           # 日志目录
└── webapps/       # Web 应用目录
```

## 环境变量

| 变量 | 默认值 | 说明 |
|------|--------|------|
| TOMCAT_VERSION | 9.0 | Tomcat 版本 |

## 常用命令

```bash
# 启动服务
docker-compose up -d

# 停止服务
docker-compose down

# 查看日志
docker-compose logs -f

# 进入容器
docker exec -it tomcat bash
```

## 部署应用

将 WAR 文件放入 `webapps/` 目录，Tomcat 会自动部署。

## 注意事项

1. 首次运行会自动复制默认配置文件到 conf 目录
2. 端口 8080 可通过 .env 文件修改
3. 生产环境建议修改默认管理密码
