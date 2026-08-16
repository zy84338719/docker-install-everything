# ZimaOS in Docker

在 Docker 中运行 ZimaOS 虚拟机 / Run ZimaOS in Docker

## 简介 / Introduction

本项目使用 [dockurr/zima](https://github.com/dockur/zima) 在 Docker 容器中运行 ZimaOS 操作系统。ZimaOS 是一个类似于 CasaOS 的家庭服务器操作系统，提供简洁的 Web 管理界面。

This project uses [dockurr/zima](https://github.com/dockur/zima) to run ZimaOS in a Docker container. ZimaOS is a home server OS similar to CasaOS, providing a clean web management interface.

## 前置要求 / Prerequisites

- **Docker** 和 **Docker Compose**
- **Docker Socket 访问 / Docker Socket Access**: 需要挂载 Docker socket 以支持容器管理。Docker socket mounting is required for container management.

## 快速开始 / Quick Start

```bash
# 1. 复制环境变量配置文件 / Copy env config
cp .env.example .env

# 2. 启动服务 / Start service
docker compose up -d

# 3. 查看日志 / View logs
docker compose logs -f
```

## 访问方式 / Access

| 方式 / Method | 地址 / Address | 说明 / Description |
|---|---|---|
| Web 管理界面 / Web UI | `http://localhost:8080` | ZimaOS 管理面板 / ZimaOS admin panel |

## 目录结构 / Directory Structure

```
zima/
├── docker-compose.yml
├── .env.example
├── .env              # 你的配置 / Your config
├── conf/             # 配置文件 / Configuration
├── data/             # ZimaOS 数据存储 / ZimaOS data storage
├── log/              # 日志文件 / Log files
├── shared/           # 共享文件夹 / Shared folder
└── README.md
```

## 功能特性 / Features

- 简洁的 Web 管理界面 / Clean web management interface
- 类似 CasaOS 的用户体验 / CasaOS-like user experience
- 支持 Docker 容器管理 / Supports Docker container management
- 支持文件管理和共享 / Supports file management and sharing
- 支持应用商店 / Supports app store
- 支持多用户管理 / Supports multi-user management

## 与 CasaOS 的关系 / Relationship with CasaOS

ZimaOS 由 CasaOS 团队开发，是 CasaOS 的商业版本。两者具有相似的界面和功能，但 ZimaOS 提供更多企业级特性。
ZimaOS is developed by the CasaOS team and is the commercial version of CasaOS. Both have similar interfaces and features, but ZimaOS offers more enterprise-grade features.

## 注意事项 / Notes

- ZimaOS 数据存储在 `data/` 目录（映射为 `/DATA`）/ ZimaOS data stored in `data/` (mapped as `/DATA`)
- Docker socket 挂载允许 ZimaOS 管理宿主机容器 / Docker socket allows ZimaOS to manage host containers
- 首次启动需要初始化，请等待几分钟 / First boot requires initialization, wait a few minutes
- 停止容器时给予 1 分钟优雅关闭时间 / 1-minute graceful shutdown on stop

## 常见问题 / FAQ

**Q: 无法访问 Web 界面？/ Cannot access web interface?**
A: 等待几分钟让初始化完成，检查日志。/ Wait a few minutes for initialization, check logs.

**Q: Docker socket 权限问题？/ Docker socket permission issues?**
A: 确保当前用户在 docker 组中。/ Ensure current user is in docker group.

**Q: 如何备份数据？/ How to backup data?**
A: 备份 `data/` 目录即可。/ Backup the `data/` directory.
