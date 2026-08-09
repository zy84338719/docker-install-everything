# example

> ⚠️ 注意：官方 `mongo-express` 镜像仓库已标注 DEPRECATED，后续可能不再更新。如需长期维护的 MongoDB Web 管理工具，建议关注其社区 fork 或其他替代方案。

## Usage

```bash
cp .env.example .env
docker-compose up -d mongo
docker-compose up -d mongo-express
```

访问： [http://127.0.0.1:8081](http://127.0.0.1:8081)

账号 dev，密码 dev，见 .env 中 ME_CONFIG_BASICAUTH_USERNAME 和 ME_CONFIG_BASICAUTH_PASSWORD 配置。