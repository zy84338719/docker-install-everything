# macOS in Docker

在 Docker 中运行 macOS 虚拟机 / Run macOS in Docker

## 简介 / Introduction

本项目使用 [dockurr/macos](https://github.com/dockur/macos) 在 Docker 容器中运行 macOS 操作系统。支持通过 Web 浏览器或 VNC 访问。

This project uses [dockurr/macos](https://github.com/dockur/macos) to run macOS in a Docker container. Access via web browser or VNC.

## 法律声明 / Legal Notice

**重要 / Important**: 运行 macOS 虚拟机需遵守 Apple 最终用户许可协议（EULA）。Apple 的 EULA 仅允许在 Apple 品牌硬件上运行 macOS 虚拟机。请确保您的使用符合相关法律法规。Running macOS virtual machines is subject to Apple's End User License Agreement (EULA). Apple's EULA only permits running macOS VMs on Apple-branded hardware. Please ensure your usage complies with applicable laws and regulations.

## 前置要求 / Prerequisites

- **KVM 支持 / KVM Support**: 主机必须支持 KVM 虚拟化。The host must support KVM virtualization.
- **AVX2 指令集 / AVX2 Instructions**: CPU 必须支持 AVX2 指令集。CPU must support AVX2 instructions.
- **Docker** 和 **Docker Compose**
- 检查 KVM / Check KVM: `ls -la /dev/kvm`
- 检查 AVX2 / Check AVX2: `grep avx2 /proc/cpuinfo`

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
| VNC 客户端 / VNC Client | `localhost:5900` | 使用任意 VNC 客户端 / Use any VNC client |

## 环境变量 / Environment Variables

| 变量 / Variable | 默认值 / Default | 说明 / Description |
|---|---|---|
| `VERSION` | `15` | macOS 版本（如 15, 14, 13）/ macOS version (e.g. 15, 14, 13) |
| `DISK_SIZE` | `256G` | 磁盘大小 / Disk size |
| `RAM_SIZE` | `8G` | 内存大小 / RAM size |
| `CPU_CORES` | `4` | CPU 核心数 / CPU cores |

## 目录结构 / Directory Structure

```
macos/
├── docker-compose.yml
├── .env.example
├── .env              # 你的配置 / Your config
├── conf/             # 配置文件 / Configuration
├── data/             # 虚拟机磁盘数据 / VM disk data
├── log/              # 日志文件 / Log files
├── shared/           # 共享文件夹 / Shared folder
└── README.md
```

## 可用 macOS 版本 / Available macOS Versions

| 版本 / Version | 名称 / Name | 代号 / Codename |
|---|---|---|
| `15` | macOS Sequoia | Sequoia |
| `14` | macOS Sonoma | Sonoma |
| `13` | macOS Ventura | Ventura |
| `12` | macOS Monterey | Monterey |

## 注意事项 / Notes

- 首次启动需要下载 macOS 恢复镜像，请耐心等待 / First boot requires macOS recovery image download, please wait
- 建议至少分配 8GB 内存和 4 核 CPU / Recommend at least 8GB RAM and 4 CPU cores
- AVX2 指令集是必需的，不支持的 CPU 将无法运行 / AVX2 is required, unsupported CPUs will not work
- 虚拟机数据存储在 `data/` 目录 / VM data stored in `data/` directory
- 共享文件夹 `shared/` 可在虚拟机内访问 / Shared folder `shared/` accessible inside VM
- 停止容器时给予 2 分钟优雅关闭时间 / 2-minute graceful shutdown on stop

## 常见问题 / FAQ

**Q: 启动失败提示 KVM 不可用 / KVM not available on startup?**
A: 确认主机支持 KVM 且已启用。/ Ensure host supports KVM and it is enabled.

**Q: 启动失败提示 AVX2 不支持 / AVX2 not supported?**
A: macOS 虚拟化需要 AVX2 指令集，请检查 CPU 是否支持。/ macOS virtualization requires AVX2, check CPU support.

**Q: 如何传输文件到虚拟机？/ How to transfer files to VM?**
A: 将文件放入 `shared/` 目录，虚拟机内可访问。/ Place files in `shared/` directory, accessible inside VM.
