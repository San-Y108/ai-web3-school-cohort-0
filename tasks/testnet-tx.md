# 任务2: 完成一笔测试网交易

## 交易信息

| 字段 | 值 |
|---|---|
| 网络 | Sepolia 测试网 |
| 交易哈希 | `0x3875a5b77e029dbc735f376030e19c6668b0621b8db735f6d0869c915f5ab092` |
| 状态 | 成功 (ok) |
| 发送方 | `0xa88AD9d49F6FC2CfE37428327C104325AAFa9506` |
| 接收方 | `0xa88AD9d49F6FC2CfE37428327C104325AAFa9506` |
| 转账金额 | 0.01 SepoliaETH |
| Gas Used | 21,000 |
| Gas Price | ~2.52 Gwei |
| 交易费用 | ~0.000053 ETH |

Etherscan 链接: https://sepolia.etherscan.io/tx/0x3875a5b77e029dbc735f376030e19c6668b0621b8db735f6d0869c915f5ab092

## 操作流程

1. 打开 MetaMask,确认网络为 Sepolia Test Network
2. 点击 Send,粘贴自己的钱包地址
3. 输入金额 0.01 ETH
4. 确认交易,等待上链

## 观察到的细节

- **Gas 正好 21000**: 这是最简单的 ETH 转账的标准 gas 消耗,没有调用任何合约
- **自己转给自己**: 安全无风险,但能完整体验从签名→广播→确认的全流程
- **费用极低**: 测试网 gas price 只有 2.5 Gwei 左右,远低于主网

## 理解

这笔交易让我实际感受到:
- 交易不是"即时"的,需要等区块确认
- 即使转账给自己,也要付 gas 费
- Gas Used × Gas Price = 实际手续费
- 交易哈希是链上唯一的身份证,可以在 Explorer 上公开查询
