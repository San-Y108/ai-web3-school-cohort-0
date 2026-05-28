## Bittensor Validator Agent：链上动作权限策略

> WCB Task: Week 2｜Wallet / Permission｜Agent 链上动作权限策略（20 分）
> 场景：一个 AI agent 帮用户在 Bittensor Subnet 上管理 validator 操作

---

### 一、核心问题

Agent 参与链上动作时，最关键的问题不是 "how to sign a transaction"，而是 **how to limit what the agent can do**。

Bittensor 场景下的核心风险：
- Agent 拿到 hotkey → 可以查询数据、打分
- Agent 拿到 coldkey → 可以 stake / unstake TAO → 资金风险
- Agent 被攻击 → 可能破坏 validator 的 Yuma Consensus 评分 → reputation 风险（比资金风险更难恢复）

设计原则：**Agent 只用 hotkey 做日常操作，coldkey 的操作必须人工确认。**

---

### 二、执行流程图

```
用户说 "把 2 TAO stake 到 Subnet 14"
    ↓
Agent 用 hotkey 查询 Subnet 14 状态（read → 自动）
    ↓
Agent 生成操作建议（prepare → 自动）
    ↓
┌─────────────────────────────────────┐
│ Policy Engine（智能合约 + Guard）      │
│ 检查：预算 ≤ daily limit?             │
│      subnet 在 allowlist 里?         │
│      操作类型 = coldkey 操作?          │
│      ↓                               │
│  如果是 coldkey 操作 → 必须人工确认     │
│  如果是 hotkey 操作 → 可自动执行       │
└─────────────────────────────────────┘
    ↓
用户审查：金额、目标 subnet、预计收益
    ↓
用户用 coldkey 签名确认
    ↓
链上执行 → stake 完成
    ↓
Audit log 记录（tx hash、amount、subnet、时间、确认人）
```

**Bittensor 特有分层（hotkey vs coldkey）：**

| 层 | 权限 | 操作示例 | Agent 能做 |
|------|------|---------|-----------|
| Hotkey | 查询、日常打分 | 查 subnet 状态、查 TAO 余额、打分 | ✅ 自动 |
| Hotkey | 建议生成 | "Subnet 19 矿工质量下降，建议减少 stake" | ✅ 自动 |
| Coldkey | 资金操作 | stake TAO、unstake TAO、transfer | ❌ 必须人工确认 |
| Coldkey | 身份操作 | register/deregister subnet | ❌ 必须人工确认 |

---

### 三、Permission Policy 设计（Bittensor 场景）

**场景：** 用户委托 agent 管理 Bittensor validator，agent 用 hotkey 做日常监控，coldkey 操作必须人工确认。

**1. Budget limit（预算上限）**
- 单次 stake 上限：≤ 2 TAO
- 每日累计上限：≤ 10 TAO
- 超过上限 → 自动拒绝

**2. Subnet allowlist（子网白名单）**
- Agent 只能往用户指定的 subnet 里 stake TAO
- 例如：Subnet 1、3、14、19 在 allowlist
- 未知 subnet → 直接拒绝

**3. Action scope（动作范围）**
- Hotkey：read subnet stats, query TAO balance, view validator score, generate suggestions
- Coldkey（需人工）：stake TAO, unstake TAO, register/deregister subnet
- 禁止：transfer TAO（agent 不能主动转出资金）

**4. Human confirmation threshold（人工确认触发条件）**
- 任何 coldkey 操作 → 必须人工确认
- 首次 stake 到某个 subnet → 必须人工确认
- 操作超出 budget 或 allowlist → 直接拒绝（不给确认机会）
- 同一天已有 5 次以上 coldkey 操作 → 额外提醒

**5. Revoke（撤销机制）**
- 用户随时撤销 agent 的 hotkey 权限
- 撤销后 agent 只能查询，不能生成任何 coldkey 操作建议
- 不会影响已有的 stake（stake 仍然属于用户）

**6. Audit log（审计日志）**
- 每次操作记录：action、amount、subnet、hotkey 或 coldkey 操作、tx hash、时间、确认状态
- 用于验证 agent 是否只做了授权范围内的操作
- 对 Yuma Consensus 信誉评估也有帮助（可证明你的 validator 操作来源）

**7. Failure handling（失败处理）**
- Stake 交易失败 → 记录失败原因，不自动重试。通知用户
- Subnet 已满不接受新 stake → 通知用户选其他 subnet
- 余额不足 → 暂停 agent，等待用户充值
- Agent 建议的 subnet 不在 allowlist → 自动拒绝 + 记录

---

### 四、ERC-4337 / Safe / Guard 为什么重要（Bittensor 场景下）

这三个机制解决同一类问题：**how to enforce rules at the infrastructure level, not just trust the agent**。

在 Bittensor 场景下，agent 同时持有 hotkey 和 coldkey 的访问权限。如果只用 prompt 约束 agent（"请不要用 coldkey"），attacker 可以用 prompt injection 绕过。所以必须在链上层面做硬限制：

**ERC-4337（Account Abstraction）**
- 把普通钱包变成 programmable smart account
- 可以内置规则：只允许 hotkey 调用的函数、禁止 coldkey 操作自动执行
- 对于 Bittensor validator：可以把 "stake" 和 "unstake" 函数标记为 coldkey-only，必须走 human confirmation 路径

**Safe（Multisig Smart Account）**
- 多签钱包：需要多个签名才能执行。可以设置 "agent 提议 + 用户确认" 的 2-of-2 模式
- Guards 在交易执行前后做检查：金额是否超限、subnet 是否在白名单、操作是否来自 hotkey

**Guard / Policy 机制**
- Guard = 安全模块，在链上层面检查每笔交易
- 回到 Bittensor 场景：Guard 可以确保 **agent 不能绕过 coldkey 限制**
  - 即使 agent 被攻击，攻击者用 prompt injection 让它尝试 stake → Guard 发现这是 coldkey 操作 → 直接拒绝
  - Agent 没办法绕过 Guard，因为 Guard 是写在链上的

**一句话总结：**
> 在 Bittensor 场景下，hotkey 和 coldkey 的分层是设计基础；ERC-4337 / Safe / Guard 是保证这个分层不会被 agent 或 attacker 绕过的硬限制。

---

### 五、与 Bittensor 主线的衔接

Bittensor Subnet Validator 的操作链路是：

```
Identity: Bittensor 地址 = validator 身份
    ↓
Permission: hotkey = 允许日常操作；coldkey = 必须人工确认
    ↓
Execution: stake 操作通过 coldkey 签名后链上执行
    ↓
Reputation: Yuma Consensus 根据操作历史打分
```

Permission policy 是关键中间层：没有它，agent 可以绕过 hotkey/coldkey 的分层，直接动 coldkey 里的 TAO。

### 六、参考资料

- [ERC-4337 文档](https://docs.erc4337.io/)
- [Safe — What is Safe](https://docs.safe.global/home/what-is-safe)
- [Safe Smart Account Guards](https://docs.safe.global/advanced/smart-account-guards)
- [Bittensor Documentation](https://docs.bittensor.com/)
- [Cobo Agentic Wallet](https://www.cobo.com/products/agentic-wallet/manual/start-here/introduction)

### 七、一句话结论

在 Bittensor 的场景下，agent 最核心的安全设计不是"能不能自动交易"，而是 hotkey 和 coldkey 的分层。Agent 只拿 hotkey，coldkey 的操作用 ERC-4337 / Safe / Guard 做硬限制，确保 attacker 即使控制了 agent，也拿不走 coldkey 里的 TAO。

> Agent = hotkey only. Coldkey = human only. Guard = enforce this, no exceptions.
