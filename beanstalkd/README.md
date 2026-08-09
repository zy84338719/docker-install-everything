# example

> ⚠️ 注意：`schickling/beanstalkd` 与 `schickling/beanstalkd-console` 镜像约 8 年未更新，事实上已停止维护。仅供学习/演示使用，生产环境建议改用其他消息队列方案。

## Usage

```bash
docker-compose up -d beanstalkd
docker-compose up -d beanstalkd-console
```

beanstalkd 管理界面访问： [http://127.0.0.1:2080](http://127.0.0.1:2080)
