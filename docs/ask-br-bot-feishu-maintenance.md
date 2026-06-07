# ask-br-bot Feishu 运维文档

本文记录 ask-br-bot 的后端、Feishu 事件订阅方式、EC2 部署形态和常见维护流程。不要把 `FEISHU_APP_SECRET`、Codex 登录 token、AWS key、SSH private key 等 secret 写进仓库。

## 当前状态

- 后端仓库：[v01dstar/askplanner](https://github.com/v01dstar/askplanner)
- 当前部署分支：fork 仓库 `main`
- 当前 Ask BR 化基线：`f07c566 Rebrand relay for Ask BR`
- 部署位置：AWS `us-east-2` 的 EC2，AWS 账号为 `tidb-br-dev-test`
- SSH private key：不要写入仓库；从安全渠道获取后放在本机私有路径
- 运行方式：`tmux` session `ask-br-bot`
- 启动命令约定：`tmux new -As ask-br-bot`
- Feishu 环境变量：EC2 用户的 `~/.bashrc`
- Codex 账号：当前使用 Andy 的个人 Codex 账号
- Feishu bot 管理人：Andy
- skills 来源：本仓库 `skills/tidb-backup-restore/`

兼容说明：

- Go module、二进制名、默认数据目录仍保留 `askplanner` / `.askplanner`，例如 `./bin/askplanner_larkbot` 和 `.askplanner/askplanner.log`。这是为了兼容现有部署和历史数据。
- 用户侧产品名和 prompt persona 已切换为 Ask BR。
- `contrib/agent-rules` 仍可能作为 workspace 兼容 repo 存在，但不是 Ask BR skill 来源。
- Ask BR 不再自动同步 `agent-rules`，也不再让 `agent-rules` 默认跟踪最新分支；只有明确执行 `/ws sync agent-rules` 时才会刷新它。

## 架构简述

ask-br-bot 是 Ask BR 的 Feishu/Lark bot 运行形态。用户在 Feishu 里提问后，后端通过 Feishu websocket 长连接收到 message event，然后把问题交给 Codex CLI，最后把 Codex 的回答回复到 Feishu。

关键链路：

1. `cmd/larkbot/main.go` 启动进程，加载环境变量，设置日志，并检查 `CODEX_BIN` 是否存在。
2. `internal/larkbot/app.go` 创建 Lark API client 和 websocket client。
3. websocket client 通过 `github.com/larksuite/oapi-sdk-go/v3/ws` 建立长连接。
4. 事件处理器注册 `OnP2MessageReceiveV1`，收到 Feishu 消息后做去重、消息过滤、typing reaction、附件/workspace/Clinic 预处理。
5. `internal/codex/responder.go` 调用 `codex exec` 或 `codex exec resume`。
6. 结果通过 Feishu reply API 回到原消息或 thread。

代码位置：

- websocket client 创建：`internal/larkbot/app.go`
- message event handler：`internal/larkbot/app.go`
- 启动入口：`cmd/larkbot/main.go`
- env 加载：`internal/config/config.go`
- Feishu 消息解析和会话 key：`internal/larkbot/message.go`
- Codex 调用：`internal/codex/runner.go`

Feishu websocket 模式不需要公网 HTTP callback 地址；进程只要能从 EC2 出站连接 Feishu/Lark Open Platform 即可。实现上使用 Lark 官方 Go SDK 的 websocket client，并把 `EventDispatcher` 作为 event handler 传进去。

## 登录 EC2

先确认 key 权限：

```bash
chmod 400 <ssh-private-key-path>
```

从 AWS 控制台进入 `tidb-br-dev-test` 账号，在 `us-east-2` 找到 ask-br-bot 对应 EC2，确认 public DNS/IP 和登录用户。常见登录用户是 `ec2-user` 或 `ubuntu`，以实例 AMI 为准。

```bash
ssh -i <ssh-private-key-path> <ec2-user-or-ubuntu>@<ec2-public-dns>
```

登录后建议先确认当前进程、tmux、repo 和 env：

```bash
tmux ls
tmux new -As ask-br-bot
pwd
git remote -v
env | grep -E '^(FEISHU_|CODEX_|WORKSPACE_|AGENT_RULES_|CLINIC_|LOG_FILE|PROJECT_ROOT|PROMPT_FILE)='
```

如果 `env` 里看不到 Feishu 或 Codex 配置，先执行：

```bash
source ~/.bashrc
```

## 启停和重载

进入 tmux：

```bash
tmux new -As ask-br-bot
```

如果 bot 正在前台跑，先用 `Ctrl-C` 停掉。然后在 askplanner repo 根目录更新代码、构建并启动：

```bash
source ~/.bashrc
git status --short
git pull --ff-only
git submodule update --init --recursive
make larkbot
./bin/askplanner_larkbot
```

启动后留在 tmux 内观察日志几秒，确认没有 startup error。detach tmux 用 `Ctrl-b d`。

更新到 Ask BR 化版本后，建议额外确认：

```bash
git log -1 --oneline
grep -n 'You are Ask BR' prompt
```

然后在 Feishu 里发送 BR/PITR 相关测试问题，确认回答不再默认走 SQL optimizer/query tuning 流程。

如果代码仓库或 submodule 是 private repo，机器上可能需要 GitHub CLI 登录：

```bash
gh auth status
gh auth login
```

也可以使用 GitHub SSH key 或 PAT，但不要把 token 写进 shell history、文档或仓库。

## 更新 skills

Ask BR 的主 skill 在本仓库 `skills/tidb-backup-restore/`。`contrib/agent-rules` 可能仍作为兼容 managed repo 存在，但现在不要把它当作 Ask BR skill 来源。

上线步骤：

1. 合并本仓库里的 `prompt` 或 `skills/tidb-backup-restore/` 变更。
2. 登录 EC2 并进入 `ask-br-bot` tmux session。
3. 重启 Ask BR 进程，让进程重新加载配置和 prompt。
4. 在 Feishu 里发一条测试问题。修改本仓库内置 skill 不需要 `/ws sync agent-rules`。

注意：

- `agent-rules` mirror 现在不会为了 Ask BR 自动定期同步；只有明确执行 `/ws sync agent-rules` 时才会刷新。
- 每个 Feishu 用户都有自己的 workspace；其中的 `contrib/agent-rules` 不应被视为 Ask BR 的主知识源。
- 每个用户 workspace 的 root 会自动创建 `skills -> <PROJECT_ROOT>/skills` 软链。Codex CLI 实际运行在用户隔离 workspace 内，因此这个软链必须存在，否则 prompt 中的 `skills/tidb-backup-restore/...` 相对路径会不可见，导致本地案例库误报“查不到”。
- workspace 的 environment hash 变化后，Ask BR 会避免复用旧 Codex session，防止继续沿用旧源码/旧 skills 上下文。

验证方式：

```bash
find .askplanner/workspaces/users -maxdepth 3 -name skills -type l -print | head
readlink .askplanner/workspaces/users/<user_key>/root/skills
```

如果已有用户 workspace 缺少 `skills` 软链，拉取包含该修复的代码并重启 larkbot 后，下一次用户提问或 `/ws status` 会触发 `Ensure` 自动补齐。

## Feishu 配置

EC2 的 `~/.bashrc` 至少需要包含：

```bash
export FEISHU_APP_ID=...
export FEISHU_APP_SECRET=...
export FEISHU_BOT_NAME=ask-br-bot
```

常见 Codex/Ask BR 配置：

```bash
export CODEX_BIN=codex
export CODEX_MODEL=gpt-5.5
export CODEX_REASONING_EFFORT=medium
export CODEX_SANDBOX=read-only
export LOG_FILE=.askplanner/askplanner.log
```

Feishu Open Platform 侧需要开启 websocket/event 订阅，并订阅接收消息事件。代码实际处理的是 `P2MessageReceiveV1`。群聊里 bot 只有在被明确 @ 时才处理消息，`FEISHU_BOT_NAME` 要和群里显示名匹配，否则 mention 检测可能失败。

## Codex 账号维护

当前 EC2 上 Codex CLI 使用 Andy 的个人账号。需要检查登录状态时：

```bash
codex --version
codex login status
```

如果 Codex CLI 不支持 `login status`，直接发一条 Feishu 测试问题并查看 `.askplanner/askplanner.log`。如果认证失效，需要在 EC2 上重新执行 `codex login`，按 CLI 提示完成认证。

长期建议把生产 bot 切到团队可维护的 Codex/OpenAI 账号，避免个人账号离职、权限变更或 token 过期影响服务。

## 日志和排障

默认日志路径：

```bash
.askplanner/askplanner.log
```

常用命令：

```bash
tail -f .askplanner/askplanner.log
tail -n 200 .askplanner/askplanner.log
grep -E 'startup error|websocket client failed|handle event error|codex|workspace' .askplanner/askplanner.log | tail -n 100
```

常见问题：

- 启动时报 `FEISHU_APP_ID and FEISHU_APP_SECRET are required`：没有 `source ~/.bashrc`，或 `.bashrc` 里缺 Feishu env。
- 启动时报 `locate Codex CLI`：`codex` 不在 `PATH`，或 `CODEX_BIN` 配错。
- websocket 连接失败：检查 Feishu app secret、event subscription、EC2 出站网络和 DNS。
- 群聊不响应：检查是否 @ 了 bot，以及 `FEISHU_BOT_NAME` 是否等于 bot 在 Feishu 群里的显示名。
- Codex 调用超时：检查 `CODEX_TIMEOUT_SEC`、Codex 账号登录状态、机器网络，以及是否有大附件或大 workspace 操作。
- skills 更新后没生效：重启 larkbot，并新开一次对话测试；如果只改了本仓库 `skills/tidb-backup-restore/`，不需要同步 `agent-rules`。
- Codex 回答说 `skills/tidb-backup-restore` 不在工作区：确认线上代码已包含 workspace `skills` 软链修复，重启 larkbot 后触发一次 `/ws status` 或新问题，让 `Ensure` 补齐 `<user>/root/skills`。
- 回答仍像 SQL tuning bot：确认线上代码已拉到 Ask BR 化提交，`prompt` 包含 `You are Ask BR`，并重启 larkbot。旧 Codex session 可能仍带旧 prompt，必要时让用户新开会话或执行重置。
- workspace env hash 因 `agent-rules` 变化而频繁失效：确认线上代码包含关闭 `agent-rules` 自动同步的版本；Ask BR 不应再因为兼容 repo 自动刷新而失效旧会话。

## 快速健康检查

部署或重启后，按顺序检查：

1. `tmux ls` 能看到 `ask-br-bot` session。
2. `tail -f .askplanner/askplanner.log` 没有连续 startup/websocket error。
3. Feishu 私聊 bot 发 `hi` 能收到回复。
4. 群里 `@ask-br-bot hi` 能收到回复。
5. 发 `/ws status` 能看到 workspace repo 状态。
6. 如刚更新 skills，发一个能命中新 skill 的测试问题。

## 交接注意事项

- SSH private key 只用于登录 EC2，不要提交到任何 repo，也不要把本机私钥路径写入仓库文档。
- Feishu app secret 在 EC2 `~/.bashrc`，不要复制到聊天或文档。
- Codex 目前是个人账号，重启或迁移机器前要确认 `codex login` 状态。
- 更新 private repo 代码前确认 EC2 上 `gh auth status` 正常。
- 修改 `prompt`、`skills/tidb-backup-restore/`、workspace repo ref 后，旧 Codex session 可能失效，这是预期行为。
