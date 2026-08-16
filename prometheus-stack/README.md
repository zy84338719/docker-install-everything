# Prometheus Stack

完整的 Prometheus 监控栈，包含 Prometheus、Grafana、Alertmanager、PrometheusAlert、Blackbox Exporter、VMware Exporter 和 Node Exporter。

A complete Prometheus monitoring stack with Prometheus, Grafana, Alertmanager, PrometheusAlert, Blackbox Exporter, VMware Exporter, and Node Exporter.

## 组件说明 / Components

| 组件 | 端口 | 说明 |
|------|------|------|
| Prometheus | 9090 | 监控数据采集和存储 |
| Grafana | 3000 | 监控可视化面板 |
| Alertmanager | 9093 | 告警管理和通知 |
| PrometheusAlert | 8080 | 告警集成工具（钉钉、微信等） |
| Blackbox Exporter | 9115 | 网络探测（HTTP、TCP、ICMP、DNS） |
| VMware Exporter | 9272 | VMware ESXi/vSphere 指标采集 |
| Node Exporter | 9100 | 主机指标采集 |

## 使用方法 / Usage

```bash
cp .env.example .env
# 编辑 .env 文件，配置 VMware 连接信息（如需要）
docker-compose up -d
```

## 访问地址 / Access

| 服务 | 地址 |
|------|------|
| Prometheus | http://127.0.0.1:9090 |
| Grafana | http://127.0.0.1:3000 |
| Alertmanager | http://127.0.0.1:9093 |
| PrometheusAlert | http://127.0.0.1:8080 |
| Blackbox Exporter | http://127.0.0.1:9115 |
| VMware Exporter | http://127.0.0.1:9272 |
| Node Exporter | http://127.0.0.1:9100 |

默认 Grafana 账号密码：`admin` / `admin`

## 推荐 Grafana Dashboard / Recommended Dashboards

| Dashboard ID | 名称 | 说明 |
|-------------|------|------|
| 1860 | Node Exporter Full | 主机监控全览 |
| 11243 | VMware ESXi | VMware ESXi 集群监控 |
| 9628 | Prometheus Stats | Prometheus 自身状态 |

在 Grafana 中通过 `+` → `Import` → 输入 ID 即可导入。

## 配置文件说明 / Configuration

| 文件路径 | 说明 |
|---------|------|
| `conf/prometheus/prometheus.yml` | Prometheus 采集配置 |
| `conf/prometheus/rules/alert_rules.yml` | 告警规则 |
| `conf/alertmanager/alertmanager.yml` | Alertmanager 路由配置 |
| `conf/prometheusalert/app.conf` | PrometheusAlert 配置 |
| `conf/blackbox/blackbox.yml` | Blackbox 探测模块配置 |
| `conf/vmware/config.yml` | VMware Exporter 配置 |

## 自定义告警规则 / Custom Alert Rules

在 `conf/prometheus/rules/` 目录下添加 `.yml` 文件即可自动加载。

示例已包含：实例宕机、CPU 高负载、内存不足、磁盘空间不足、VMware 主机/虚拟机状态等告警。

## 与已有 prometheus 目录的区别 / Difference from prometheus/

- `prometheus/`：基础版，包含 Prometheus + Grafana + Pushgateway + Alertmanager
- `prometheus-stack/`：完整版，增加了 PrometheusAlert、Blackbox Exporter、VMware Exporter、Node Exporter，适合生产环境

## 参考 / Reference

- 来源: [robotneo/prometheus-everything](https://github.com/robotneo/prometheus-everything)
- Prometheus: [prometheus.io](https://prometheus.io/)
- Grafana: [grafana.com](https://grafana.com/)
