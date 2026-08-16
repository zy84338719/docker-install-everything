# Windows in Docker

在 Docker 中运行 Windows 虚拟机，支持自动安装、KVM 加速和远程桌面连接。

Run Windows in Docker with automatic installation, KVM acceleration, and RDP access.

## 前置条件 / Prerequisites

- 需要支持 KVM 的 Linux 主机（不支持 macOS 和 Windows 原生）
- CPU 需开启虚拟化（VT-x / AMD-V）

```bash
# 检查 KVM 是否可用
ls -la /dev/kvm
```

## 使用方法 / Usage

```bash
cp .env.example .env
# 编辑 .env 文件，选择 Windows 版本和配置
docker-compose up -d
```

## 访问方式 / Access

### Web Viewer（推荐）

打开浏览器访问：[http://127.0.0.1:8006](http://127.0.0.1:8006)

可通过网页直接查看和操作 Windows 桌面，无需安装客户端。

### 远程桌面 / Remote Desktop

使用 Windows 自带的「远程桌面连接」或 macOS 上的 Microsoft Remote Desktop：

- 地址：`127.0.0.1:3389`
- 用户名：见 `.env` 中 `USERNAME` 配置
- 密码：见 `.env` 中 `PASSWORD` 配置

## 支持的 Windows 版本 / Supported Versions

| 版本 | VERSION 值 | 说明 |
|------|-----------|------|
| Windows 11 | `win11` | 最新桌面版 |
| Windows 10 | `win10` | 经典桌面版 |
| Windows 10 LTSC | `ltsc10` | 长期服务版 |
| Windows 8 | `win8` | 旧版桌面 |
| Windows 7 | `win7` | 旧版桌面 |
| Windows Vista | `vista` | 旧版桌面 |
| Windows XP | `winxp` | 经典版 |
| Windows Server 2025 | `2025` | 最新服务器版 |
| Windows Server 2022 | `2022` | 服务器版 |
| Windows Server 2019 | `2019` | 服务器版 |
| Windows Server 2016 | `2016` | 服务器版 |
| Windows Server 2012 | `2012` | 服务器版 |
| Windows Server 2008 | `2008` | 服务器版 |

也可以指定自定义 ISO 的 URL 地址。

## 环境变量 / Environment Variables

| 变量 | 默认值 | 说明 |
|------|-------|------|
| `VERSION` | `win11` | Windows 版本 |
| `DISK_SIZE` | `64G` | 虚拟磁盘大小 |
| `RAM_SIZE` | `4G` | 内存大小 |
| `CPU_CORES` | `2` | CPU 核心数 |
| `USERNAME` | - | 登录用户名 |
| `PASSWORD` | - | 登录密码 |
| `LANGUAGE` | `English` | 系统语言 |

## 端口说明 / Ports

| 端口 | 说明 |
|------|------|
| `8006` | Web Viewer（网页访问） |
| `3389/tcp` | 远程桌面 RDP |
| `3389/udp` | 远程桌面 RDP |

## 高级配置 / Advanced

### 文件共享 / File Sharing

将文件放入 `./shared` 目录，Windows 中可通过网络访问共享文件夹。

### 磁盘直通 / Disk Passthrough

在 docker-compose.yml 中添加设备映射，将物理磁盘直通给 Windows：

```yaml
devices:
  - /dev/sdb:/disk1
  - /dev/sdc:/disk2
```

### USB 设备直通 / USB Passthrough

```yaml
environment:
  - USB_DEVICES=1234:5678
```

其中 `1234:5678` 为 USB 设备的 Vendor ID 和 Product ID。

## 参考 / Reference

- GitHub: [dockur/windows](https://github.com/dockur/windows)
