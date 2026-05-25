# Learning Agent Setup

**WCB 任务：** Week 1 AI 向任务 | Learning Agent Setup
**完成日期：** 2026-05-25

---

## 选择的 Learning Agent：Hermes Agent

Hermes Agent 是一个 CLI AI Agent，支持工具调用、持久记忆、技能系统、定时任务等功能，适合作为 AI×Web3 School 的长期学习助手。

---

## 配置内容

### 1. 环境
- 平台：macOS 26.5
- 安装方式：Hermes Agent CLI
- 工作目录：`~/ai-web3-school-cohort-0`

### 2. 集成的能力

| 能力 | 用途 | 状态 |
|------|------|------|
| WCB API 连接 | 拉取任务列表、查询进度、获取活动日程 | ✅ |
| GitHub 读写 | 学习产出自动 commit + push | ✅ |
| 持久记忆 | 跨会话保留学习偏好、环境配置 | ✅ |
| 技能系统 | ai-web3-school-learning-agent 技能指导学习流程 | ✅ |
| 飞书集成 | 日历、提醒、文档等 | ✅ |
| 浏览器 | 查阅 Handbook、搜索资料 | ✅ |

### 3. Learning Agent 启动 Prompt

```
请作为我的 AI × Web3 School Learning Agent，先阅读启动 Prompt：
https://aiweb3.school/learning-agent.zh.txt
并结合 Handbook：https://aiweb3.school/zh/handbook/
帮我初始化个人学习计划、GitHub 学习仓库、每日打卡草稿和 Handbook feedback 流程。
```

---

## Agent 已执行的学习任务

- 拉取 WCB Week 1 全部任务并分析优先级
- 制定每日学习计划（综合 WCB 任务 + Handbook 章节 + 线上活动日程 + 用户进度）
- 完成「AI×Web3 信息流关注清单」任务并提交 GitHub
- 辅助 Web3 实操（Sepolia 水龙头、合约部署等）
- 学习笔记自动整理、git commit + push

---

## 为什么选择 Hermes

1. **工具调用能力**：可以直接操作终端、读写文件、调用 API，不只是聊天
2. **持久记忆**：用户偏好、学习进度跨会话保留，不用每次重复
3. **技能扩展**：ai-web3-school-learning-agent 技能封装了完整的学习工作流
4. **本地运行**：代码和数据都在本地，隐私可控

---

## 下一步

- 继续用 Hermes 辅助 Week 2 学习
- 探索 Handbook feedback 流程（提交学习过程中的 Handbook 改进建议）
- 尝试用 Hermes 的 cronjob 做每日学习提醒

---

*Repo: [ai-web3-school-cohort-0](https://github.com/San-Y108/ai-web3-school-cohort-0)*
