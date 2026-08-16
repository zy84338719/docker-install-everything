# Virtual DSM - Synology DSM in Docker

在 Docker 中运行 Synology DSM 虚拟机 / Run Synology DSM in Docker

## 简介 / Introduction

本项目使用 [vdsm/virtual-dsm](https://github.com/vdsm/virtual-dsm) 在 Docker 容器中运行 Synology DSM（DiskStation Manager）操作系统。

This project uses [vdsm/virtual-dsm](https://github.com/vdsm/virtual-dsm) to run Synology DSM (DiskStation Manager) OS in a Docker container.

**声明 / Disclaimer**: 本项目与 Synology Inc. 无任何关联。Synology 是 Synology Inc. 的注册商标。This project is not affiliated with Synology Inc. Synology is a registered trademark of Synology Inc.

## 前置要求 / Prerequisites

- **KVM 支持 / KVM Support**: 主机必须支持 KVM 虚拟化。The host must support KVM virtualization.
- **Docker** 和 **Docker Compose**
- 检查 KVM / Check KVM: `ls -la /dev/kvm`

## 快速开始 / Quick Start

```bash
# 1. 复制环境变量配置文件 / Copy env config
cp .env.example .env

# 2. 编辑 .env 文件（可选）/ Edit .env (optional)
vim .env

# 3. 启动服务 / Start service
docker compose up -d

# 4. 查看日志 / View logs
docker compose logs -f
```

## 访问方式 / Access

| 方式 / Method | 地址 / Address | 说明 / Description |
|---|---|---|
| Web 管理界面 / Web UI | `http://localhost:5000` | DSM 管理面板 / DSM admin panel |

## 环境变量 / Environment Variables

| 变量 / Variable | 默认值 / Default | 说明 / Description |
|---|---|---|
| `DISK_SIZE` | `256G` | 虚拟磁盘大小 / Virtual disk size |
| `RAM_SIZE` | `2G` | 内存大小 / RAM size |
| `CPU_CORES` | `2` | CPU 核心数 / CPU cores |

## 目录结构 / Directory Structure

```
virtual-dsm/
├── docker-compose.yml
├── .env.example
├── .env              # 你的配置 / Your config
├── conf/             # 配置文件 / Configuration
├── data/             # DSM 磁盘数据 / DSM disk data
├── log/              # 日志文件 / Log files
├── shared/           # 共享文件夹 / Shared folder
└── README.md
```

## 功能特性 / Features

- 完整的 Synology DSM 操作系统 / Full Synology DSM operating system
- 支持 Synology Package Center / Supports Synology Package Center
- 支持 Docker 套件（在 DSM 内）/ Supports Docker package (inside DSM)
- 支持文件共享、媒体服务等 / Supports file sharing, media services, etc.

## 注意事项 / Notes

- 首次启动需要下载 DSM 镜像，请耐心等待 / First boot requires DSM image download, please wait
- 虚拟磁盘数据存储在 `data/` 目录 / Virtual disk data stored in `data/` directory
- 建议至少分配 2GB 内存 / Recommend at least 2GB RAM
- 停止容器时给予 2 分钟优雅关闭时间 / 2-minute graceful shutdown on stop

## 常见问题 / FAQ

**Q: 启动失败提示 KVM 不可用 / KVM not available on startup?**
A: 确认主机支持 KVM 且已启用。/ Ensure host supports KVM and it is enabled.

**Q: DSM 授权问题？/ DSM licensing issues?**
A: 虚拟 DSM 使用 Synology 提供的试用授权。/ Virtual DSM uses trial licenses provided by Synology.
