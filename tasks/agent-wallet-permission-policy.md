## Agent 链上动作权限策略（Wallet / Permission / Safe Execution）

> WCB Task: Week 2｜Wallet / Permission｜Agent 链上动作权限策略（20 分）

---

### 一、核心问题

Agent 参与链上动作时，最关键的问题不是 "how to sign a transaction"，而是 **how to limit what the agent can do**。

- Agent 不应该持有 private key
- Agent 可以 propose（提议）交易，但不能 execute（执行）高风险动作
- Permission = budget + scope + time window + human confirmation + audit log

---

### 二、执行流程图

```
Agent proposes action
       │
       ▼
┌─────────────────┐
│ Policy Engine    │  ← checks: budget, allowlist, action type, rate limit
│ (smart contract  │
│  or guard)       │
└────────┬────────┘
         │
    ┌────┴────┐
    │         │
 low-risk  high-risk
    │         │
    ▼         ▼
 auto-execute  pause → human confirmation required
    │              │
    │         user reviews & approves / rejects
    │              │
    ▼              ▼
 wallet signs → chain executes
         │
         ▼
   audit log records
   (tx hash, action, amount, timestamp, approval status)
```

**Three action tiers:**

| Tier | Examples | Agent behavior |
|------|----------|---------------|
| Read-only | check balance, read contract state, view tx history | Auto — no permission needed |
| Prepare | generate tx params, estimate gas, explain ABI, suggest action | Auto-generate, but cannot execute |
| Write | transfer, approve, swap, deploy contract, upgrade, governance vote | Must pause for human confirmation |

---

### 三、Permission Policy 设计

给一个 agent wallet 场景设计权限策略：

**1. Budget limit（预算上限）**
- 单次交易上限：例如 ≤ 0.01 ETH
- 每日累计上限：例如 ≤ 0.05 ETH / day
- 超过上限 → 自动拒绝，不需要人工确认

**2. Contract allowlist（合约白名单）**
- Agent 只能调用白名单内的合约地址
- 例如：Uniswap Router、Aave Pool、特定 ERC-20
- 未知合约 → 拒绝或暂停请求人工确认

**3. Action scope（动作范围）**
- 允许：read, swap (≤ budget), approve (≤ budget)
- 禁止：deploy contract, upgrade proxy, governance vote, transfer to unknown address
- 禁止动作 → 直接拒绝，不给用户确认机会

**4. Human confirmation threshold（人工确认阈值）**
- 金额 > 0.005 ETH → 需要人工确认
- 调用非白名单合约 → 需要人工确认
- 首次 approve 某 token → 需要人工确认
- 低于阈值的白名单内操作 → 可自动执行

**5. Revoke（撤销机制）**
- 用户可随时撤销 agent 的所有权限
- 撤销后 agent 只能做 read-only 操作
- 实现方式：revoke session key / remove guard / update policy

**6. Audit log（审计日志）**
- 每次动作记录：action type, amount, contract, tx hash, timestamp, approval status
- 日志公开可查（链上或 off-chain 可验证记录）
- 用于事后复盘、追责、reputation 积累

**7. Failure handling（失败处理）**
- 交易失败 → 记录失败原因，不自动重试
- 余额不足 → 暂停，通知用户
- Gas 过高 → 暂停，建议等待或手动操作
- Policy 违规 → 拒绝 + 记录

---

### 四、ERC-4337 / Safe / Guard / Policy 为什么重要

这三个机制解决同一类问题：**how to enforce rules at the infrastructure level, not just trust the agent**。

**ERC-4337（Account Abstraction）**
- 把 EOA（普通钱包）变成 smart account（智能账户）
- 智能账户可以内置规则：每日限额、白名单、多签、时间锁
- 关键能力：user operation = 可编程的交易请求，不只是简单的签名
- 对 agent 的意义：agent 的每个动作都可以被 policy 拦截，不需要信任 agent 本身

**Safe（Multisig Smart Account）**
- 多签钱包：需要 N 个签名者中的 M 个批准才能执行
- Guards：在交易执行前后做检查（pre-check / post-check）
- 对 agent 的意义：可以设置 "agent 提议 + human 确认" 的 2-of-2 模式
- Guard 可以检查：金额是否超限、合约是否在白名单、调用函数是否允许

**Guard / Policy 机制**
- Guard = 附加在 smart account 上的安全模块
- 执行前检查 pre-validation：交易是否符合规则
- 执行后检查 post-execution：结果是否异常
- Policy = 规则本身（budget, allowlist, rate limit, time window）

**一句话总结：**
> ERC-4337 makes wallets programmable. Safe adds multi-sig and guards. Guards enforce policy. Together they turn "trust the agent" into "verify the agent."

中文：ERC-4337 让钱包可编程，Safe 加上多签和 guard，Guard 来执行策略。三者合在一起，把"信任 agent"变成"验证 agent"。

---

### 五、与 Identity / Reputation 方向的关系

昨天选的主方向是 Identity / Reputation / Capability。今天的 Wallet / Permission 是它的下游：

```
Identity: who is this agent? → trust score
    ↓
Permission: what can this agent do? → policy boundary
    ↓
Execution: how does this agent act on-chain? → safe execution
```

Agent 可信不等于 agent 应该无限制执行。即使 reputation 很高，permission 仍然需要 limit。这是 product 层面的核心 insight：
> Trust is not permission. Reputation shows history, but policy controls future actions.

中文：信任 ≠ 权限。Reputation 展示历史，但 policy 控制未来行为。

---

### 六、参考资料

- [ERC-4337 文档](https://docs.erc4337.io/)
- [Safe - What is Safe](https://docs.safe.global/home/what-is-safe)
- [Safe Smart Account Guards](https://docs.safe.global/advanced/smart-account-guards)
- [Cobo Agentic Wallet](https://www.cobo.com/products/agentic-wallet/manual/start-here/introduction)
- [Ethereum Account Abstraction](https://ethereum.org/roadmap/account-abstraction/)

---

### 七、一句话结论

Agent wallet 的核心不是让 agent 自动发交易，而是用 policy + infrastructure 把 agent 的能力限制在安全范围内。Permission boundary = budget + allowlist + human confirmation + audit log + revoke.

> We don't trust the agent. We constrain it.

---

### 八、Bittensor 场景扩展：Agent 管理 Validator 钱包

上面的通用框架可以直接映射到 Bittensor 场景。Bittensor 的钱包有两层 key：

**Hotkey（热键）：**
- 用于日常操作（查询 subnet 状态、给 miner 打分）
- 资金风险小 → 对应上面的 Read-only + Prepare 层
- Agent 可以拿到 hotkey，自动执行查询和打分类操作

**Coldkey（冷键）：**
- 存放 TAO，管理 stake / unstake
- 对应上面的 Write 层 → **必须人工确认**
- Agent 不能碰 coldkey。所有 stake、unstake、register/deregister 操作由用户签名确认

**权限策略映射：**

| 通用规则 | Bittensor 场景 |
|---------|---------------|
| Budget limit | 单次 stake ≤ 2 TAO，每日 ≤ 10 TAO |
| Allowlist | 只能往用户指定的 subnet 里 stake（如 Subnet 1、3、14、19） |
| Action scope | Hotkey = 查询+打分 / Coldkey = stake+unstake（禁止 transfer） |
| Human confirmation | 所有 coldkey 操作必须确认；首次 stake 某 subnet 也需确认 |
| Revoke | 撤销 agent 的 hotkey，不影响已有 stake |
| Audit log | 记录每次操作对应的 subnet、金额、hotkey/coldkey、确认状态 |

**为什么要区分 hotkey / coldkey？**

如果 agent 只用一把 key，被攻击后所有 TAO 都没了。分两层后：
- Hotkey 被攻击 → 只能影响日常打分，TAO 在 coldkey 里安全
- 用户用 coldkey 撤销 hotkey → 换一把新 hotkey → agent 恢复正常工作

这和 ERC-4337 / Safe / Guard 的逻辑一致：用代码层面做硬限制，不靠 agent "自觉"。
