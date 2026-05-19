# Week 1 工具准备记录

**任务:** Week 1｜前置准备｜完成课程工具准备  
**WCB Task ID:** cmp3jypmh07s0n301e51hp6r3 (sort=970, 10pts)  
**日期:** 2026-05-19

---

## 一、协作工具

| 工具 | 状态 | 用途 |
|------|------|------|
| **Telegram** | ✅ 已就绪 | 课程社群交流、每日打卡、Learning Agent 对话 |
| **Zoom** | ⬜ 需安装 | 参加实时线上分享活动（今晚 20:00 Hermes Agent 入门） |
| **Google Calendar** | ✅ 已配置 | 课程日程管理，已添加"工作"日历 |
| **GitHub** | ✅ 已就绪 | 学习仓库托管、任务证明提交 |

### 协作工具详情

**Telegram:**
- 已加入 AI×Web3 School 课程群 @aiweb3school
- 通过 Hermes Agent Telegram 接入进行学习交互
- 用途：课程通知、社群答疑、协作讨论、Agent 交互

**Zoom:**
- 状态：macOS 未安装
- 下一步：今晚活动前安装 `brew install --cask zoom`
- 用途：实时线上分享活动（Week 1 有 5 场以上）

**Google Calendar / Apple Calendar:**
- 已配置多个日历：个人、工作、我的课表
- 已添加课程活动日程
- 用途：跟踪线上活动时间、任务截止日期

**GitHub:**
- CLI (`gh`) 已安装认证
- 学习仓库: https://github.com/San-Y108/ai-web3-school-cohort-0
- 用途：任务记录、学习日志、代码实验、Proof-of-Work 提交

---

## 二、AI 工具

| 工具 | 状态 | 用途 |
|------|------|------|
| **Hermes Agent** | ✅ 主力使用 | Learning Agent，学习计划、任务管理、概念解释、仓库维护 |
| **WCB API (Agent)** | ✅ 已连通 | 拉取任务列表、提交任务证明、查询课程进度 |
| **ChatGPT / Claude Web** | ✅ 可用 | 概念补充、快速问答、翻译辅助 |
| **Cursor** | ⬜ 可选 | AI 辅助代码编辑（VS Code 已替代基础需求） |
| **GLM / Z.AI** | ⬜ 待探索 | 课程赞助方工具，后续 Agent 实验时接入 |

### AI 工具详情

**Hermes Agent (主力):**
- 已配置为 Learning Agent，连接 Telegram
- 功能：每日学习计划、WCB API 任务管理、GitHub 仓库维护、概念解释
- 启动 Prompt 已加载：https://aiweb3.school/learning-agent.zh.txt
- 配置了 WCB API 密钥、GitHub 认证
- 用于：所有学习任务（信息流清单、工具准备、概念卡片、每日打卡等）

**WCB API:**
- 已配置 `WCB_AGENT_SECRET_API_KEY`
- 端点正常：`program.getById`, `tasks.listForLearner`, `tasks.submitProof`
- programId: cmnx791nl008sru0167pzp4ki
- trackId (Week 1): cmoy1hces012app01kp9ci5gb
- 用途：任务拉取、进度追踪、证明提交

**ChatGPT / Claude Web:**
- 浏览器直接使用
- 用途：快速概念查阅、翻译、简单问答

**Cursor / VS Code:**
- VS Code 已安装，能看代码但不会独立写
- Cursor 暂不需要，Hermes Agent + VS Code 覆盖当前需求

**GLM / Z.AI:**
- 后续 Agent 实验阶段接入
- 作为课程赞助方，关注其 API 和工具更新

---

## 三、Web3 工具

| 工具 | 状态 | 用途 |
|------|------|------|
| **MetaMask (浏览器钱包)** | ⬜ 待安装 | 测试网交互、交易签名、dApp 连接 |
| **Rabby 钱包** | ⬜ 待安装 | 多链钱包、交易预览、安全提醒 |
| **Etherscan (区块浏览器)** | ✅ 可用 | 查交易、合约、地址（浏览器直接访问） |
| **Remix IDE** | ✅ 可用 | 在线 Solidity IDE（浏览器直接访问） |
| **Hardhat / Foundry** | ⬜ 后续 | 本地合约开发框架（Week 1 不强制） |
| **测试网 ETH** | ⬜ 待领取 | 水龙头领取（Sepolia / Holesky） |

### Web3 工具详情

**MetaMask:**
- 下一步计划：安装浏览器扩展 → 创建新钱包 → 安全备份助记词
- 用途：Week 1 测试网交易实践、dApp 交互、Agent Wallet 实验
- 注意：仅用于测试，不与主网资产混用

**Rabby:**
- 可作为 MetaMask 替代或补充
- 优势：多链支持好、交易预览清晰、内置安全提醒
- 用途：多链交互、Agent 交易安全观察

**Etherscan (etherscan.io):**
- 无需安装，浏览器直接访问
- 用途：查看交易状态、合约代码、地址余额、gas 费用

**Remix IDE (remix.ethereum.org):**
- 在线使用，无需安装
- 用途：Solidity 合约编写和部署（Week 1 合约交互实践）

**Hardhat / Foundry:**
- 本地开发框架，Week 1 不强制
- 后续实验阶段根据需要安装

**测试网 ETH:**
- Sepolia / Holesky 水龙头领取
- 用途：支付测试网 gas 费，完成链上交互任务

---

## 四、工具准备完成度总结

### 已就绪 ✅
- Telegram（社群 + Agent 交互）
- GitHub（仓库 + CLI）
- Hermes Agent（主力学习助手）
- WCB API（任务管理）
- Git / VS Code / Node.js
- 浏览器工具（Etherscan、Remix、ChatGPT/Claude Web）
- Apple Calendar（日程管理）

### 今日待完成 ⬜
- [ ] Zoom 安装（今晚 20:00 前）
- [ ] MetaMask 或 Rabby 钱包安装（明日 Web3 实践前）

### 后续计划 ⬜
- [ ] 测试网 ETH 领取（做链上交互任务时）
- [ ] GLM/Z.AI API 探索（Agent 实验阶段）
- [ ] Hardhat/Foundry（合约开发深入时）
- [ ] Cursor（如需更深度 AI 辅助编码）

---

## 五、工具与 Week 1 任务对应

| Week 1 任务 | 所需工具 |
|-------------|---------|
| 建立信息流关注清单 | X/Twitter、浏览器 |
| 完成课程工具准备 | 本文档对应 |
| 创建 GitHub repo | Git、GitHub CLI |
| 加入社群+自我介绍 | Telegram |
| Learning Agent Setup | Hermes Agent、WCB API |
| Proof-of-Work 测试 | WCB 平台 |
| 整理 AI 基础概念卡片 | Hermes Agent、GitHub |
| 整理 Web3 概念卡片 | Hermes Agent、Etherscan |
| 线上活动参与 | Zoom、Telegram |
| AI Agent 入门实践 | Hermes Agent、浏览器 |
| 测试网交易实践 | MetaMask/Rabby、Etherscan、Remix |
| 合约交互实践 | MetaMask、Remix、Etherscan |

---

*Created: 2026-05-19*  
*Repo: https://github.com/San-Y108/ai-web3-school-cohort-0*
