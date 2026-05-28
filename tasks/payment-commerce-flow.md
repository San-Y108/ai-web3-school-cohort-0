## 最小支付与商业流程拆解（Payment / Commerce）

> WCB Task: Week 2｜Payment / Commerce｜最小支付与商业流程拆解（20 分）
> 场景：AI Agent 帮用户自动购买 AI 推理 API 服务（text-to-image）

---

### 一、场景与角色拆解

**场景：** 用户说"帮我生成 10 张产品图" → Agent 自动找到最便宜的 text-to-image API → 谈价格 → 付钱 → 拿结果 → 验收。

**5 个角色：**

| 角色 | 是谁 | 做什么 |
|------|------|--------|
| 下单方 | 用户的 AI Agent | 发现服务、发起请求、提交支付 |
| 执行方 | API 服务提供商（Seller） | 运行模型、生成结果 |
| 验收方 | Agent 自动验收 + 用户人工确认 | 检查格式/数量 + 确认质量 |
| 付款方 | Agent（用用户授权的预算） | 签名支付、在预算内操作 |
| 仲裁方 | 链上 reputation 系统 + 平台调解 | 裁定争议、降权低评分 seller |

---

### 二、最小 Payment / Commerce Flow

**环节 1：报价（Quote）**

Agent 请求 API："我要 10 张产品图"
API 返回 HTTP 402 Payment Required + 价格信息：
- 单价：0.05 TAO/张
- 总价：0.5 TAO
- Seller 地址、有效期

对应 x402 标准：server 响应 402 状态码 + payment instructions。买家不需要注册账号、不需要 session，HTTP 层直接完成报价。

---

**环节 2：预算授权（Budget Authorization）**

Agent 拿到报价 0.5 TAO → 先检查用户预设的预算上限：
- 用户设的：每天 2 TAO
- 这笔交易：0.5 TAO
- 0.5 < 2 → 通过，继续

超过预算 → 暂停，通知用户："这笔交易超预算，需要手动确认吗？"

对应 Cobo CAW 的 Pact 机制：用户事先授权预算范围，agent 只能在范围内自动操作。

---

**环节 3：执行（Execution）**

预算通过 → Agent 提交支付 payload 给 API：
- Agent 签名支付 → 发给 seller
- Seller 调用 facilitator 的 /verify 验证支付有效
- 验证通过 → 开始处理请求（生成图片）

对应 x402 标准：buyer 提交 payment payload → server verify → 开始执行。

注意：此时钱是预授权，执行失败则退回。

---

**环节 4：交付（Delivery）**

API 生成完 10 张图 → 返回结果给 Agent：
- Seller 调用 facilitator 的 /settle 确认收款
- 资源（图片 URL / base64）返回给 agent

对应 x402 标准：payment verified → server provides requested resource。

---

**环节 5：验收（Acceptance）**

两种验收方式，缺一不可：

**自动验收（Agent 做）：**
- 格式对不对？（PNG/JPG）
- 数量够不够？（10 张）
- 有没有空文件？

**人工验收（用户做）：**
- 图片质量是否符合需求
- 需要修改的地方能否接受

验收结果：
- 通过 → 进入付款完成
- 不通过 → 进入退款/争议流程

---

**环节 6：付款 / 退款 / 争议**

三种走向：

**验收通过：**
→ TAO 从用户钱包转给 seller → 交易完成

**验收不通过（明显垃圾）：**
→ TAO 退回用户钱包 → 记录 seller 负面评分（reputation 降权）

**有争议（部分可用）：**
→ 触发仲裁机制：
  - 链上：reputation 系统自动降低 seller 评分，影响其未来收入
  - 链下：平台调解或用户手动判定
  - 最终手段：用户手动撤销 agent 的支付权限

---

**环节 7：记录证明（Receipt）**

每笔交易必须留记录：
- 交易时间
- 买了什么（10 张产品图）
- 花了多少（0.5 TAO）
- Seller 地址
- 验收结果（通过 / 不通过）
- 交易状态（完成 / 退款 / 争议中）
- tx hash（链上可查）

记录用途：事后复盘、reputation 积累、争议举证。链上记录不可篡改，比传统的截图/邮件更可靠。

---

### 三、完整流程图

```
用户说 "生成 10 张产品图"
    ↓
Agent 请求 API 服务
    ↓
API 返回 402 + 报价（环节1）
    ↓
Agent 检查用户预算（环节2）
    ↓ 超预算 → 暂停通知用户手动确认
    ↓ OK
Agent 提交支付 → API 验证 → 执行（环节3）
    ↓
API 返回图片结果（环节4）
    ↓
Agent 自动验收 + 用户人工验收（环节5）
    ↓ 通过
    ↓   → 付款完成（环节6）
    ↓ 不通过
    ↓   → 退款/争议
记录 tx hash + 结果（环节7）
```

---

### 四、x402 vs MPP 对比

| 维度 | x402 | MPP |
|------|------|-----|
| **解决的问题** | API 的 paywall：卖家给 API 设付费门槛，买家自动付款 | Agent 支付：让 AI agent 能像人类一样完成支付 |
| **覆盖环节** | 报价 + 执行 + 交付（服务层面） | 预算授权 + 执行 + 结算（agent 层面） |
| **支付方式** | HTTP 402 + crypto-native（USDC on Base） | 传统支付 + crypto（Stripe 集成） |
| **验收机制** | 无内置验收，靠卖家自行设计 | 无内置验收 |
| **争议处理** | 无内置，靠链上 reputation | 无内置，靠平台调解 |
| **适合场景** | API 微支付、AI agent 自动付款 | 有 Stripe 账户的商家 + agent 购物 |
| **谁发起** | Seller（server 端设 paywall） | Buyer（agent 端发起支付） |

**核心区别：**

x402 解决的是 **seller 端** 怎么给服务定价、怎么收费。
MPP 解决的是 **buyer 端**（agent）怎么像人一样完成支付。

两者不冲突，可以组合：x402 做报价和交付，MPP 做 agent 侧的预算控制和支付执行。

---

### 五、参考资料

- [x402 Docs](https://docs.x402.org/introduction)
- [MPP Introduction](https://stripe.com/blog/machine-payments-protocol)
- [MPP 官方文档](https://docs.stripe.com/payments/machine/mpp)
- [Cobo CAW 文档](https://www.cobo.com/products/agentic-wallet/manual/start-here/introduction)
- [Stripe Agentic Commerce](https://stripe.com/blog/agentic-commerce)

---

### 六、一句话结论

Agent commerce 最难的不是"能不能转账"，而是怎么把报价、预算、执行、交付、验收、争议、记录串成一个可控的链路。x402 解决了 seller 端的定价和交付，但验收和争议还需要额外机制（reputation、平台调解、人工兜底）来补。
