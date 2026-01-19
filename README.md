# WenDui · 问对（后端）

## 前端库索引

https://github.com/d0ublecl1ck/the-question

## 快速开始

```bash
cd /Users/d0ublecl1ck/the-question/.worktrees/backend-fastapi/backend
uv sync
cp .env.example .env
```

`.env` 最小配置示例：

```
ENV=development
DEBUG=false
DATABASE_URL=mysql+pymysql://wendui:wendui@127.0.0.1:3306/wendui
SECRET_KEY=change-me
OPENAI_API_KEY=
MINIMAX_API_KEY=
```

请确保本地或 Docker 内的 MySQL 已启动，并将 `.env` 中的 `DATABASE_URL` 指向 MySQL。

启动：

```bash
uv run uvicorn app.main:app --reload
```

访问：`http://127.0.0.1:8000`


## Docker 一键启动

```bash
# 构建并启动
OPENAI_API_KEY=your-key MINIMAX_API_KEY=your-key   docker compose up -d --build
```

- 服务启动后访问：`http://127.0.0.1:8000`
- 数据库默认账号：`wendui` / `wendui`，库名：`wendui`
- 生产部署请务必修改 `SECRET_KEY`（在 `docker-compose.yml` 的 `api.environment` 中）
- 启动时会执行 `alembic upgrade head`，自动建表/迁移

## 运行测试

```bash
cd backend
uv run pytest
```

## 数据库迁移

```bash
cd backend
uv run alembic upgrade head
```

生成新迁移：

```bash
cd backend
uv run alembic revision --autogenerate -m "<message>"
```

## 市场预设技能（种子脚本）

写入预设技能到市场（含 system 用户归属）：

```bash
cd backend
PYTHONPATH=. uv run scripts/seed_market_skills.py --path skills/market-presets.json
```

仅校验（不写入 DB）：

```bash
cd backend
PYTHONPATH=. uv run scripts/seed_market_skills.py --path skills/market-presets.json --dry-run
```
