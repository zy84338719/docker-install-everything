# nodejs

Node.js 开发环境，容器启动后保持运行，可进入容器执行 npm/node 命令。

## Usage

```bash
cp .env.example .env
docker-compose up -d
```

进入容器

```bash
docker exec -it nodejs /bin/sh
```

在容器内初始化项目

```bash
cd /app
npm init -y
npm install express
node -e "require('express')().get('/',(req,res)=>res.send('Hello')).listen(3000)"
```

也可以将现有项目代码放入 `./data` 目录，容器内 `/app` 会自动同步。

如果想用 `npm start` 作为启动命令，修改 docker-compose.yml 中的 command：

```yaml
command: npm start
```
