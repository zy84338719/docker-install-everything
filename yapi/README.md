# example

> ⚠️ 注意：YApi 上游项目（jayfong/yapi 镜像）约 5 年未更新，事实上已停止维护，且不再适配新版 Node/MongoDB。本目录将 mongo 固定在 6.0 以尽量保持兼容。仅供学习/演示使用，生产环境建议改用 Apifox、ApiPost、ShowDoc 等替代品。

## Usage

```bash
cp .env.example .env
docker-compose up -d
```

访问： [http://127.0.0.1:40001](http://127.0.0.1:40001)
默认的登录账号为 admin@yapi.com，密码为 admin，可在 .env 文件中调整。

