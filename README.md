# AI × Web3 School — Week 1 Proof-of-Work Pack

**学生：** 严硕 (San-Y108)
**GitHub：** https://github.com/San-Y108/ai-web3-school-cohort-0
**Week 1 学习时间：** 2026-05-18 至 2026-05-25

---

## Week 1 学习总览

本周从零开始，完成了 AI 基础和 Web3 基础的系统学习，并通过测试网实操验证了概念理解。核心收获：

- **AI 侧：** LLM 是推理层不是真相源；Prompt 是软约束不是安全边界；Context 决定模型看见什么
- **Web3 侧：** 钱包是身份和签名入口；智能合约是可编程的状态机；交易需要区块浏览器验证
- **交叉理解：** AI 可以解释、规划、提醒，但签名和链上写操作必须由人确认

---

## PoW Pack 内容清单

### 1. AI 学习记录或概念卡片

| 文件 | 内容 |
|------|------|
| [concepts/ai-basics.md](concepts/ai-basics.md) | AI 基础概念卡片（LLM、Prompt、Context、Agent、Tool Use） |
| [concepts/llm-prompt-context.md](concepts/llm-prompt-context.md) | Handbook AI 基础前三章系统笔记（Token、Embedding、Transformer、Hallucination、Instruction、Few-shot、Structured Output、Prompt Injection、Context Window、Context Engineering、Memory、Knowledge Base） |

---

### 2. Learning Agent / AI 工具实践记录

| 文件 | 内容 |
|------|------|
| [tasks/learning-agent-setup.md](tasks/learning-agent-setup.md) | Hermes Agent 配置记录，包括：选择的 Agent、集成能力（WCB API、GitHub、持久记忆、技能系统）、启动 Prompt、已执行的学习任务示例 |

**关键 Prompt 示例：**
```
请作为我的 AI × Web3 School Learning Agent，先阅读启动 Prompt：
https://aiweb3.school/learning-agent.zh.txt
并结合 Handbook：https://aiweb3.school/zh/handbook/
帮我初始化个人学习计划、GitHub 学习仓库、每日打卡草稿和 Handbook feedback 流程。
```

---

### 3. Web3 概念卡片或测试网交易记录

**Web3 概念卡片：**

| 文件 | 内容 |
|------|------|
| [concepts/cryptography.md](concepts/cryptography.md) | 密码学基础（哈希、公私钥、签名） |
| [concepts/network-basics.md](concepts/network-basics.md) | 网络基础（节点、区块、共识） |
| [concepts/wallet-basics.md](concepts/wallet-basics.md) | 钱包基础（EOA、助记词、签名） |
| [concepts/wallets-vs-exchanges.md](concepts/wallets-vs-exchanges.md) | 钱包 vs 交易所（自托管 vs 托管） |
| [concepts/smart-contract-and-accounts.md](concepts/smart-contract-and-accounts.md) | 智能合约与账户（合约地址、读写操作、Gas） |

**测试网交易记录：**

| 文件 | 内容 |
|------|------|
| [tasks/testnet-tx.md](tasks/testnet-tx.md) | Sepolia 测试网转账记录（0.01 ETH 自转账） |
| [tasks/smart-contract-deploy.md](tasks/smart-contract-deploy.md) | SimpleStorage 合约部署与调用记录 |

---

### 4. 测试网交易哈希 / 合约地址 / 区块浏览器链接

**交易哈希：**
```
0x3875a5b77e029dbc735f376030e19c6668b0621b8db735f6d0869c915f5ab092
```

**Etherscan 链接：**
https://sepolia.etherscan.io/tx/0x3875a5b77e029dbc735f376030e19c6668b0621b8db735f6d0869c915f5ab092

**合约地址：**
```
0x80ac7a484a4759ccae47f735e12997361b58658f
```

**合约 Etherscan 链接：**
https://sepolia.etherscan.io/address/0x80ac7a484a4759ccae47f735e12997361b58658f

---

### 5. AI × Web3 最小交叉实验或流程图

| 文件 | 内容 |
|------|------|
| [tasks/ai-web3-minimal-workflow.md](tasks/ai-web3-minimal-workflow.md) | AI×Web3 最小交叉流程图，覆盖 6 个阶段：AI 生成说明 → 人工复核 → 钱包签名 → 测试网执行 → 区块浏览器验证 → GitHub 记录 |

**流程图核心：**
```
AI 生成说明（候选建议）
  → 人工复核（检查边界、决定是否执行）
  → 钱包签名（私钥授权、不可撤销）
  → 链上执行（区块链共识）
  → 区块浏览器验证（链上真相）
  → GitHub 记录（公开证据）
```

---

### 6. 本周遇到的问题和一次人工修正记录

**问题：** 测试网水龙头领不到币

**背景：** 
在完成「完成一笔测试网交易」任务时，需要领取 Sepolia 测试币。尝试了多个水龙头：
- Chainlink 水龙头：要求主网持有 ≥1 LINK（新用户不可用）
- Google Cloud 水龙头：连接出错
- Alchemy 水龙头：需要注册账号

**修正过程：**
1. 发现问题：传统水龙头都有门槛或限制
2. 搜索替代方案：找到 PoW 水龙头（sepolia-faucet.pk910.de）
3. 验证可用性：零门槛，无需注册，直接领取
4. 记录方案：记录到 `references/testnet-operations.md`，方便后续使用

**关键学习：**
- 测试网水龙头有多种类型，各有门槛
- PoW 水龙头是最稳定的新手方案
- 遇到问题时，搜索替代方案比反复尝试更高效

**相关文件：**
- [tasks/testnet-tx.md](tasks/testnet-tx.md) — 测试网交易记录
- `references/testnet-operations.md` — 测试网操作参考（包含水龙头方案）

---

### 7. 受限 Web3 助手设计与 CLI 原型

| 文件 | 内容 |
|------|------|
| [tasks/limited-web3-assistant-workflow.md](tasks/limited-web3-assistant-workflow.md) | 受限合约交互检查助手设计文档（525 行，覆盖状态机、权限模型、Mermaid 流程图、案例演示、异常处理） |
| [tools/limited_web3_assistant.py](tools/limited_web3_assistant.py) | CLI 原型：explain / checklist / calldata / verify / query（链上只读查询） |

**核心设计：**
```
AI 辅助 → 解释操作、生成检查清单、指导验证
AI 不能 → 签名、转账、授权、接触私钥/助记词
人工确认 → 两个不可跳过的检查点（清单复核 + MetaMask 弹窗）
```

---

### 8. AI 可交互学习产物 — AI Concept Coach

| 文件 | 内容 |
|------|------|
| [tools/ai_concept_coach.py](tools/ai_concept_coach.py) | CLI 概念学习工具：输入概念名 → 解释、类比、检查题、反馈、下一步练习 |
| [tasks/ai-interactive-learning-product.md](tasks/ai-interactive-learning-product.md) | 任务说明文档：工具介绍、AI 辅助 vs 人工修改、局限性 |

**覆盖 6 个概念：** LLM、Prompt、Agent、Wallet、Smart Contract、Gas

---

### 9. 行业观察进阶 — 拆解 AI × Web3 项目

| 文件 | 内容 |
|------|------|
| [tasks/ai-web3-project-teardown.md](tasks/ai-web3-project-teardown.md) | 拆解 Cobo Agentic Wallet + Hermes Agent：问题、AI/Web3 分工、可验证材料、学习收获 |

**拆解对象：**
- **Cobo Agentic Wallet** — 为 AI Agent 设计的链上钱包，核心是 Pact 授权协议
- **Hermes Agent** — 通用 AI Agent 平台，核心是 Tool Calling + Skills + Memory

---

## 其他 Week 1 产出

**前置准备任务（全部 APPROVED）：**
- 建立 AI × Web3 行业信息流关注清单（SUBMITTED）
- 加入课程社群并完成自我介绍
- 在 X 发布你的 AI × Web3 School 起点
- 创建课程 GitHub repo
- 完成课程工具准备
- 完成 Proof-of-Work 提交测试

**线上活动（APPROVED）：**
- 5.18 Co-learning
- 5.18 AI 时代的 Web3 架构能力
- 5.19 AI Agent 入门：Hermes 从 0 到 1

**Web3 进阶任务（APPROVED）：**
- 比较 EOA、智能账户、多签的权限差异

---

## 学习笔记

| 日期 | 内容 |
|------|------|
| [daily/2026-05-18.md](daily/2026-05-18.md) | 开营日 |
| [daily/2026-05-19.md](daily/2026-05-19.md) | 前置准备 + AI Agent 入门 |
| [daily/2026-05-22.md](daily/2026-05-22.md) | Web3 架构分享 |
| [daily/2026-05-23.md](daily/2026-05-23.md) | 智能合约部署 |
| [daily/2026-05-25.md](daily/2026-05-25.md) | AI 基础前三章学习 + 流程图完成 |
| [daily/2026-05-26.md](daily/2026-05-26.md) | 受限 Web3 助手 + AI 学习产物 + 拆解 AI×Web3 项目 |

---

## 总结

Week 1 完成了从零到一的基础搭建：
- **AI 侧：** 理解了 LLM、Prompt、Context、RAG、Agent 的核心概念
- **Web3 侧：** 完成了测试网交易、合约部署、账户类型比较
- **交叉理解：** 画出了 AI×Web3 最小安全链路流程图；拆解了 Cobo Agentic Wallet 和 Hermes Agent，理解了"架构级权限限制 vs prompt 约束"
- **工具链：** 配置了 Hermes Agent 作为学习助手，接入了 WCB API 和 GitHub
- **产出：** 受限 Web3 助手设计文档 + CLI 原型、AI 概念教练 CLI、AI×Web3 项目拆解报告

下一步：继续 Week 2 剩余任务（Security/Privacy threat model、Payment/Commerce 拆解）。

---

## Week 2 产出

| 文件 | 内容 |
|------|------|
| [tasks/ai-web3-problem-map-direction.md](tasks/ai-web3-problem-map-direction.md) | AI×Web3 问题地图与主方向选择（5方向，主线：Identity/Reputation） |
| [tasks/ai-web3-problem-map.html](tasks/ai-web3-problem-map.html) | 可视化问题地图（深色主题 SVG） |
| [tasks/week2-direction-research.md](tasks/week2-direction-research.md) | Week 2 方向研究索引 |
| [tasks/agent-profile-sketch.md](tasks/agent-profile-sketch.md) | Hermes Agent profile 设计（8字段 + MCP vs A2A 对比） |
| [tasks/contribution-tracker-sketch.md](tasks/contribution-tracker-sketch.md) | DAO 贡献记录工作流草图 |
| [tasks/agent-wallet-permission-policy.md](tasks/agent-wallet-permission-policy.md) | Agent 钱包权限策略：执行流程、Policy 设计、ERC-4337/Safe/Guard 解析 |
| [tasks/bittensor-agent-threat-model.md](tasks/bittensor-agent-threat-model.md) | Bittensor Validator Agent 威胁模型：资产、攻击面、Policy 策略、低风险/高风险分级 |
| [tasks/payment-commerce-flow.md](tasks/payment-commerce-flow.md) | 最小支付与商业流程拆解：7 环节 + x402 vs MPP 对比 |

---

*GitHub Repo: https://github.com/San-Y108/ai-web3-school-cohort-0*
*Week 1 Proof-of-Work Pack — 2026-05-26*
