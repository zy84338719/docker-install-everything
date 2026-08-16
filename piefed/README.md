# PieFed (Docker)

## Description

PieFed is a federated link aggregation and discussion platform, similar to Reddit and Lemmy. It is built on the ActivityPub protocol, allowing it to federate with other platforms in the Fediverse, including Lemmy, Mastodon, and others. PieFed emphasizes community moderation tools, transparency, and user privacy.

## Features

- Federated link aggregation and discussions (ActivityPub)
- Community creation and management
- Upvote/downvote system with reputation tracking
- Rich text posts with Markdown support
- Federates with Lemmy, Mastodon, and other ActivityPub platforms
- Built-in moderation tools
- User privacy focused

## Quick Start

1. Copy `.env.example` to `.env` (optional):
   ```bash
   cp .env.example .env
   ```

2. Start the service:
   ```bash
   docker compose up -d
   ```

3. Access the web interface at `http://localhost:8080`

4. Complete the initial setup wizard to configure your instance.

## Requirements

- **Storage**: Data is stored in `./data`.
- **Network**: Ensure port 8080 is available.

## Federation

PieFed uses the ActivityPub protocol to federate with other instances. Once set up, your communities can be followed by users on Lemmy, Mastodon, and other compatible platforms. Users on your instance can also interact with content from federated instances.

## Environment Variables

No environment variables are required for basic setup.

## Ports

| Port  | Protocol | Description      |
|-------|----------|------------------|
| `8080`| HTTP     | PieFed web UI    |

---

# PieFed (Docker)

## 描述

PieFed 是一个联邦式链接聚合和讨论平台，类似于 Reddit 和 Lemmy。它基于 ActivityPub 协议构建，可以与 Fediverse 中的其他平台进行联合，包括 Lemmy、Mastodon 等。PieFed 注重社区管理工具、透明度和用户隐私。

## 功能

- 联邦式链接聚合和讨论（ActivityPub）
- 社区创建和管理
- 投票系统和声誉追踪
- 支持 Markdown 的富文本帖子
- 与 Lemmy、Mastodon 及其他 ActivityPub 平台联合
- 内置管理工具
- 注重用户隐私

## 快速开始

1. 复制 `.env.example` 为 `.env`（可选）：
   ```bash
   cp .env.example .env
   ```

2. 启动服务：
   ```bash
   docker compose up -d
   ```

3. 访问 Web 界面：`http://localhost:8080`

4. 完成初始设置向导以配置您的实例。

## 要求

- **存储**：数据存储在 `./data`。
- **网络**：确保端口 8080 可用。

## 联邦功能

PieFed 使用 ActivityPub 协议与其他实例进行联合。设置完成后，您的社区可以被 Lemmy、Mastodon 和其他兼容平台上的用户关注。您实例上的用户也可以与联合实例上的内容进行互动。

## 环境变量

基本设置不需要环境变量。

## 端口

| 端口   | 协议 | 说明            |
|--------|------|-----------------|
| `8080` | HTTP | PieFed Web 界面 |
