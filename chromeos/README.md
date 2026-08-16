# ChromeOS Flex in Docker

在 Docker 中运行 ChromeOS Flex 虚拟机 / Run ChromeOS Flex in Docker

## 简介 / Introduction

本项目使用 [dockurr/chromeos](https://github.com/dockur/chromeos) 在 Docker 容器中运行 ChromeOS Flex 操作系统。支持通过 Web 浏览器或 VNC 访问。

This project uses [dockurr/chromeos](https://github.com/dockur/chromeos) to run ChromeOS Flex in a Docker container. Access via web browser or VNC.

## 前置要求 / Prerequisites

- **KVM 支持 / KVM Support**: 主机必须支持 KVM 虚拟化。The host must support KVM virtualization.
- **Docker** 和 **Docker Compose**
- **GPU 支持（可选）/ GPU Support (Optional)**: 如需 GPU 加速，需要 `/dev/dri` 设备。For GPU acceleration, `/dev/dri` device is needed.
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
| VNC 客户端 / VNC Client | `localhost:5900` | 使用任意 VNC 客户端 / Use any VNC client |

## 环境变量 / Environment Variables

| 变量 / Variable | 默认值 / Default | 说明 / Description |
|---|---|---|
| `VERSION` | `stable` | ChromeOS 版本通道 / ChromeOS version channel |
| `GPU` | `Y` | 是否启用 GPU 加速 / Enable GPU acceleration |
| `DISK_SIZE` | `64G` | 磁盘大小 / Disk size |
| `RAM_SIZE` | `4G` | 内存大小 / RAM size |
| `CPU_CORES` | `2` | CPU 核心数 / CPU cores |
| `AUDIO` | `N` | 是否启用音频 / Enable audio |

## 目录结构 / Directory Structure

```
chromeos/
├── docker-compose.yml
├── .env.example
├── .env              # 你的配置 / Your config
├── conf/             # 配置文件 / Configuration
├── data/             # 虚拟机磁盘数据 / VM disk data
├── log/              # 日志文件 / Log files
├── shared/           # 共享文件夹 / Shared folder
└── README.md
```

## 可用版本通道 / Available Version Channels

| 通道 / Channel | 说明 / Description |
|---|---|
| `stable` | 稳定版（推荐）/ Stable (recommended) |
| `beta` | 测试版 / Beta |
| `ltc` | 长期候选版 / Long-term Candidate |
| `ltr` | 长期发布版 / Long-term Release |

## GPU 加速 / GPU Acceleration

要启用 GPU 加速：
To enable GPU acceleration:

1. 确保主机有 GPU 且 `/dev/dri` 可用 / Ensure host has GPU and `/dev/dri` is available
2. 在 `.env` 中设置 `GPU=Y` / Set `GPU=Y` in `.env`
3. docker-compose.yml 已配置 `/dev/dri` 挂载 / docker-compose.yml already mounts `/dev/dri`

检查 GPU 设备 / Check GPU device:
```bash
ls -la /dev/dri/
```

## 开发者模式 / Developer Mode

ChromeOS Flex 默认以普通用户模式启动。如需开发者模式：
ChromeOS Flex boots in normal user mode by default. For developer mode:

1. 启动后在登录界面按 `Ctrl+Alt+T` 打开终端 / Press `Ctrl+Alt+T` at login to open terminal
2. 输入 `shell` 进入 shell / Type `shell` to enter shell
3. 使用 `sudo` 执行管理员命令 / Use `sudo` for admin commands

## 注意事项 / Notes

- 首次启动需要下载 ChromeOS 镜像，请耐心等待 / First boot requires ChromeOS image download, please wait
- 虚拟机数据存储在 `data/` 目录 / VM data stored in `data/` directory
- GPU 加速需要主机 GPU 支持 / GPU acceleration requires host GPU support
- 音频支持默认关闭，可在 `.env` 中启用 / Audio disabled by default, enable in `.env`
- 停止容器时给予 2 分钟优雅关闭时间 / 2-minute graceful shutdown on stop

## 常见问题 / FAQ

**Q: 启动失败提示 KVM 不可用 / KVM not available on startup?**
A: 确认主机支持 KVM 且已启用。/ Ensure host supports KVM and it is enabled.

**Q: GPU 加速不工作 / GPU acceleration not working?**
A: 检查 `/dev/dri` 是否存在，确认 GPU 驱动已安装。/ Check if `/dev/dri` exists and GPU drivers are installed.

**Q: 如何切换版本通道？/ How to switch version channels?**
A: 修改 `.env` 中的 `VERSION` 变量，重启容器。/ Change `VERSION` in `.env` and restart container.
