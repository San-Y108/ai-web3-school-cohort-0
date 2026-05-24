# Week 1 工具准备记录

## 1. 协作工具

| 工具 | 接入方式 | Week 1 用途 |
|------|---------|------------|
| **Telegram** | 移动端 + 网页版 | 社群公告、同学交流、课程通知 |
| **Zoom** | 桌面客户端 | 线上 Co-learning、开营仪式、嘉宾分享 |
| **Google Calendar** | 浏览器 + macOS 日历同步 | 管理课程日程（已配置"工作"日历追踪所有线上活动） |
| **GitHub** | CLI (`gh` + `git`) + Web | 托管学习产出仓库 [ai-web3-school-cohort-0](https://github.com/San-Y108/ai-web3-school-cohort-0) |

环境：
- macOS 26.5
- Google Chrome + Safari
- Git 2.50.1

## 2. AI 工具

| 工具 | 版本 | Week 1 用途 |
|------|------|------------|
| **Hermes Agent** | v0.14.0 | CLI AI Agent，作为学习协管：拉取 WCB 任务列表、制定每日学习计划、审查产出质量、自动管理 Git 提交 |
| **Claude** | Web / Claude Code | 逐步引导学习，概念解释，代码理解（用户偏好 Claude 做教学引导） |
| **Python 3** | 3.13.5 | 编写链上合约交互脚本（如 `contract_interact.py`），数据分析 |
| **Node.js** | v24.15.0 | JS/TS 合约交互，Web3 前端兜底 |

选择说明：
- Hermes Agent 负责项目管理（任务追踪、计划制定、产出审查）
- Claude 负责教学内容（概念讲解、逐步引导）
- 两者互补：Hermes 管"做什么、做到哪了"，Claude 管"怎么做、为什么"

## 3. Web3 工具

| 工具 | 用途 | 已用/已测 |
|------|------|----------|
| **MetaMask** | 浏览器钱包插件，管理 Sepolia 测试网账户 | ✅ 已部署合约 |
| **Remix IDE** | 在线 Solidity 开发环境，编译+部署+交互 | ✅ 已部署 SimpleStorage |
| **Sepolia Etherscan** | 区块浏览器，查询交易/合约/地址 | ✅ 已验证合约上链 |
| **Sepolia Faucet** | 测试币水龙头（sepolia-faucet.pk910.de PoW 方式） | ✅ 已领测试 ETH |
| **RPC 节点** | ethereum-sepolia-rpc.publicnode.com | ✅ 已通过 curl 调 eth_call |

Web3 钱包地址（Sepolia）：`0xa88AD9d49F6FC2CfE37428327C104325AAFa9506`

工具路径选择：
- **Remix IDE**（而非 Hardhat/Foundry）：新手友好，浏览器即开即用，适合理解合约部署核心流程
- **MetaMask**（而非其他钱包）：生态最广，社区支持足
- **PoW 水龙头**（而非 Alchemy/Chainlink）：零门槛，无需注册

## 4. 工具使用记录

已用上述工具完成的任务：
- 开营仪式参与（Zoom）
- 加入社群自我介绍（Telegram）
- 创建 GitHub 学习仓库（GitHub + Git CLI）
- 完成一笔 Sepolia 测试网交易（MetaMask + Etherscan + Faucet）
- 部署 SimpleStorage 智能合约（Remix + MetaMask + Solidity Compiler）
- 链上合约交互验证（curl + RPC + Etherscan）

## 5. 下一步计划

目前工具已覆盖 Week 1 全部需求，无需额外安装。如有新任务引入 Hardhat/Foundry 等本地开发框架，届时按需补充。

GitHub: https://github.com/San-Y108/ai-web3-school-cohort-0
