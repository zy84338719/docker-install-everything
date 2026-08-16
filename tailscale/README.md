# Tailscale

[Tailscale](https://tailscale.com/) 是基于 WireGuard 的零配置 mesh VPN, 本配置将其部署为 **子网路由器**, 使不同局域网之间可以通过 Tailscale 隧道互相访问。

## 功能

- 子网路由: 将局域网子网广播到 Tailscale 网络, 其他节点可直接访问
- MTU 优化: 默认 1420 (Tailscale 默认 1280)
- 状态持久化: Docker volume 存储认证信息, 重启不丢失

## 前置条件

- Docker & Docker Compose
- Tailscale 账号 (免费)
- Auth Key: 从 [Tailscale Admin Console → Settings → Keys](https://login.tailscale.com/admin/settings/keys) 生成

## 使用方法

```bash
# 1. 配置
cp .env.example .env
vi .env   # 填入 Auth Key、主机名、子网路由

# 2. 启动
docker-compose up -d

# 3. 查看日志
docker-compose logs -f tailscale

# 4. 验证状态
docker-compose exec tailscale tailscale status
```

启动后, 登录 [Tailscale Admin Console → Machines](https://login.tailscale.com/admin/machines), 找到新节点, 点击 "..." → "Edit route settings" 批准子网路由。

## 常用命令

```bash
# 查看状态
docker-compose exec tailscale tailscale status

# 查看已连接的对等节点
docker-compose exec tailscale tailscale status --peers

# 重新认证
docker-compose exec tailscale tailscale up --force-reauth

# 重启
docker-compose restart tailscale

# 停止并清理
docker-compose down
```

## 宿主机要求

子网路由需要宿主机开启 IP 转发:

```bash
# 临时生效
sysctl -w net.ipv4.ip_forward=1

# 持久化
echo 'net.ipv4.ip_forward = 1' | sudo tee /etc/sysctl.d/99-tailscale.conf
sudo sysctl -p /etc/sysctl.d/99-tailscale.conf
```

## 故障排查

容器无法启动, 检查 TUN 设备:

```bash
ls -la /dev/net/tun
# 如果不存在, 可在 .env 中添加: TS_EXTRA_ARGS=--tun=userspace-networking
```

子网路由不通:

```bash
# 检查 IP 转发
sysctl net.ipv4.ip_forward

# 检查路由
ip route | grep 10.10

# 从对端 ping 测试
ping <对端 Tailscale IP>
```

## 多节点示例

在两台机器上分别部署, 作为各自的子网路由器:

| 节点 | TS_HOSTNAME | TS_ROUTES | 说明 |
|------|-------------|-----------|------|
| 机器 A | router-a | 10.10.30.0/24,10.10.10.0/24 | Studio 网段 |
| 机器 B | router-b | 10.10.21.0/24 | Dev 网段 |

部署后, 机器 A 可直接访问 `10.10.21.x`, 机器 B 可直接访问 `10.10.30.x`。
