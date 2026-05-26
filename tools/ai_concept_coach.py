#!/usr/bin/env python3
"""
AI Concept Coach
一个零依赖 CLI 小工具：输入 AI / Web3 概念，输出解释、类比、检查题和学习建议。

定位：Week 1「AI 向任务｜完成 AI 可交互学习产物」最小 demo。
注意：不读取 API Key，不连接钱包，不包含任何私钥/助记词。
"""

from __future__ import annotations

import textwrap


CONCEPTS = {
    "llm": {
        "name": "大语言模型 / LLM",
        "plain": "LLM 是在大量文本上训练出来的模型。它最核心的动作不是“真正像人一样思考”，而是根据上下文预测下一个最可能出现的 token。因为训练数据足够大、模型足够复杂，它表现出解释、总结、翻译、写代码等能力。",
        "analogy": "像一个读过海量资料的写作助手：你给它上文和要求，它根据学到的语言规律继续写下去。",
        "points": [
            "输入叫 prompt，模型会根据 prompt 生成输出。",
            "模型一次能看到的上下文有限，叫 context window。",
            "输出可能有幻觉，所以重要结论需要人工验证。",
        ],
        "quiz": "为什么说 LLM 的输出需要人工验证？",
        "keywords": ["幻觉", "不一定正确", "验证", "来源", "事实"],
        "next": "用一个你最近学的 Web3 概念问 LLM，然后检查它有没有说错。",
    },
    "prompt": {
        "name": "Prompt / 提示词",
        "plain": "Prompt 是你给 AI 的任务说明。好的 prompt 不只是提问题，还会补充背景、目标、约束和输出格式，让模型更容易给出可用答案。",
        "analogy": "像给实习生派任务：只说“写一下”通常不够，要说明写给谁看、写多长、重点是什么、不要做什么。",
        "points": [
            "背景越清楚，输出越贴近需求。",
            "格式要求能减少后期整理成本。",
            "可以要求模型先提问、再回答，避免它乱猜。",
        ],
        "quiz": "一个好 prompt 通常应该包含哪些信息？",
        "keywords": ["背景", "目标", "格式", "约束", "角色"],
        "next": "把一个模糊问题改写成包含背景、目标、格式的 prompt。",
    },
    "agent": {
        "name": "AI Agent / 智能体",
        "plain": "Agent 是能围绕一个目标连续执行多步动作的 AI 系统。它不只是一问一答，还可能拆任务、调用工具、读取文件、运行命令、检查结果，再决定下一步。",
        "analogy": "LLM 像会回答问题的人，Agent 像会拿着任务清单去办事的人。",
        "points": [
            "Agent = LLM + 工具 + 记忆/状态 + 执行循环。",
            "适合处理需要多步骤验证的任务。",
            "风险是可能误操作，所以权限和边界很重要。",
        ],
        "quiz": "Agent 和普通聊天式 LLM 最大区别是什么？",
        "keywords": ["工具", "多步", "执行", "目标", "循环"],
        "next": "观察 Hermes 如何读取任务、写文件、运行 git，这就是 Agent 工作流。",
    },
    "wallet": {
        "name": "钱包 / Wallet",
        "plain": "Web3 钱包不是装币的软件，而是管理私钥、发起签名、证明你能控制某个地址的工具。链上的资产记录在区块链上，钱包只是帮你安全地操作这些资产。",
        "analogy": "钱包更像一把钥匙，而不是一个保险箱。资产在链上，钥匙决定谁能操作。",
        "points": [
            "地址可以公开，私钥和助记词绝不能公开。",
            "签名是在证明“我是这个地址的控制者”。",
            "转账和合约交互都需要签名并支付 gas。",
        ],
        "quiz": "为什么不能把助记词提交到 GitHub？",
        "keywords": ["私钥", "控制", "资产", "泄露", "盗"],
        "next": "打开 MetaMask 看账户地址，理解地址可公开、助记词不可公开。",
    },
    "smart contract": {
        "name": "智能合约 / Smart Contract",
        "plain": "智能合约是部署在区块链上的程序。它的代码和状态在链上，用户通过交易或读取调用与它交互。读取通常免费，写入会改变链上状态，需要签名和 gas。",
        "analogy": "像一台公开运行的自动售货机：规则写在机器里，谁来操作都按同一套规则执行。",
        "points": [
            "部署后会有合约地址。",
            "read 调用读取状态，不改链；write 调用改变状态，要发交易。",
            "合约逻辑一旦上链，修改成本很高，所以部署前要测试。",
        ],
        "quiz": "read 调用和 write 调用有什么区别？",
        "keywords": ["读取", "状态", "改变", "gas", "签名", "交易"],
        "next": "在 Remix 里对 SimpleStorage 分别点击 get 和 set，观察一个免费读取、一个需要交易确认。",
    },
    "gas": {
        "name": "Gas / 燃料费",
        "plain": "Gas 是区块链执行操作需要付出的计算费用。转账、部署合约、调用会改状态的函数都要消耗网络资源，所以要付 gas。",
        "analogy": "像开车要油费，链上执行计算也要付“燃料费”。",
        "points": [
            "读取链上数据通常不花 gas。",
            "写入链上状态需要 gas。",
            "网络拥堵时 gas 可能变贵。",
        ],
        "quiz": "为什么 set() 通常要 gas，而 get() 通常不要？",
        "keywords": ["写入", "改变状态", "读取", "计算", "交易"],
        "next": "在测试网交易详情里查看 gas used 字段。",
    },
}

ALIASES = {
    "大语言模型": "llm",
    "模型": "llm",
    "提示词": "prompt",
    "智能体": "agent",
    "钱包": "wallet",
    "合约": "smart contract",
    "智能合约": "smart contract",
    "燃料费": "gas",
}


def normalize(user_input: str) -> str | None:
    text = user_input.strip().lower()
    if text in CONCEPTS:
        return text
    for alias, key in ALIASES.items():
        if alias.lower() in text:
            return key
    for key in CONCEPTS:
        if key in text:
            return key
    return None


def wrap(text: str) -> str:
    return textwrap.fill(text, width=72)


def show_concept(key: str) -> None:
    item = CONCEPTS[key]
    print("\n" + "=" * 72)
    print(f"概念：{item['name']}")
    print("=" * 72)
    print("\n1. 大白话解释")
    print(wrap(item["plain"]))
    print("\n2. 类比")
    print(wrap(item["analogy"]))
    print("\n3. 关键点")
    for point in item["points"]:
        print(f"- {point}")
    print("\n4. 检查题")
    print(item["quiz"])
    answer = input("你的回答：").strip()
    matched = [kw for kw in item["keywords"] if kw in answer]
    print("\n5. 反馈")
    if matched:
        print(f"方向对了。你的回答里提到了：{', '.join(matched)}")
        print("可以再补一句：这个概念在真实操作里会影响什么决策。")
    else:
        print("这次回答还可以更具体。建议回到上面的关键点，至少覆盖 1-2 个关键词。")
        print(f"可参考关键词：{', '.join(item['keywords'])}")
    print("\n6. 下一步练习")
    print(item["next"])


def main() -> None:
    print("AI Concept Coach｜AI/Web3 概念交互学习小工具")
    print("可输入：llm / prompt / agent / wallet / smart contract / gas")
    print("输入 q 退出。")
    while True:
        raw = input("\n你想学习哪个概念？> ").strip()
        if raw.lower() in {"q", "quit", "exit"}:
            print("结束。记得把你真正理解的部分写进学习笔记。")
            return
        key = normalize(raw)
        if not key:
            print("暂时不认识这个概念。可以试试：llm、prompt、agent、wallet、smart contract、gas。")
            continue
        show_concept(key)


if __name__ == "__main__":
    main()
