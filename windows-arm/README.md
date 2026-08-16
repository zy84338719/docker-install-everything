# Windows ARM in Docker

在 Docker 中运行 Windows ARM 虚拟机 / Run Windows ARM in Docker

## 简介 / Introduction

本项目使用 [dockurr/windows](https://github.com/dockur/windows) 在 Docker 容器中运行 Windows ARM 版本。支持通过 Web 浏览器或 RDP 远程桌面访问。

This project uses [dockurr/windows](https://github.com/dockur/windows) to run Windows ARM in a Docker container. Access via web browser or RDP remote desktop.

## 前置要求 / Prerequisites

- **KVM 支持 / KVM Support**: 主机必须支持 KVM 虚拟化（ARM 架构）。The host must support KVM virtualization (ARM architecture).
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
| Web 浏览器 / Web Browser | `http://localhost:8006` | 内置 Web 查看器 / Built-in web viewer |
| RDP 远程桌面 / RDP | `localhost:3389` | 使用任意 RDP 客户端 / Use any RDP client |

## 环境变量 / Environment Variables

| 变量 / Variable | 默认值 / Default | 说明 / Description |
|---|---|---|
| `VERSION` | `tiny11` | Windows 版本 / Windows version |
| `DISK_SIZE` | `64G` | 磁盘大小 / Disk size |
| `RAM_SIZE` | `4G` | 内存大小 / RAM size |
| `CPU_CORES` | `2` | CPU 核心数 / CPU cores |
| `USERNAME` | `Windows` | 登录用户名 / Login username |
| `PASSWORD` | `Windows` | 登录密码 / Login password |
| `LANGUAGE` | `English` | 系统语言 / System language |

## 目录结构 / Directory Structure

```
windows-arm/
├── docker-compose.yml
├── .env.example
├── .env              # 你的配置 / Your config
├── conf/             # 配置文件 / Configuration
├── data/             # 虚拟机磁盘数据 / VM disk data
├── log/              # 日志文件 / Log files
├── shared/           # 共享文件夹 / Shared folder
└── README.md
```

## 可用 Windows 版本 / Available Windows Versions

- `tiny11` - 精简版 Windows 11 ARM / Slim Windows 11 ARM
- `win11` - Windows 11 ARM
- `win10` - Windows 10 ARM
- `ltsc10` - Windows 10 LTSC

## 注意事项 / Notes

- 首次启动需要下载 ISO 镜像，请耐心等待 / First boot requires ISO download, please wait
- 虚拟机数据存储在 `data/` 目录 / VM data stored in `data/` directory
- 共享文件夹 `shared/` 可在虚拟机内访问 / Shared folder `shared/` accessible inside VM
- 停止容器时给予 2 分钟优雅关闭时间 / 2-minute graceful shutdown on stop

## 常见问题 / FAQ

**Q: 启动失败提示 KVM 不可用 / KVM not available on startup?**
A: 确认主机是 ARM 架构且 KVM 已启用。/ Ensure host is ARM architecture with KVM enabled.

**Q: 如何传输文件到虚拟机？/ How to transfer files to VM?**
A: 将文件放入 `shared/` 目录，虚拟机内可访问。/ Place files in `shared/` directory, accessible inside VM.
