# 任务: 部署或调用一个最小智能合约

## 合约信息

| 字段 | 值 |
|---|---|
| 合约地址 | `0x80ac7a484a4759ccae47f735e12997361b58658f` |
| 部署交易 | `0x380366fdd443d59903b59660424e1dac6e20af2234bb959b5f2194214b10c9a1` |
| 网络 | Sepolia |
| Gas 消耗 | 117,683 |
| 合约类型 | SimpleStorage (存一个 uint256) |

Sepolia Etherscan: https://sepolia.etherscan.io/address/0x80ac7a484a4759ccae47f735e12997361b58658f

## 合约代码

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract SimpleStorage {
    uint256 private storedNumber;

    function set(uint256 _number) public {
        storedNumber = _number;
    }

    function get() public view returns (uint256) {
        return storedNumber;
    }
}
```

## 操作流程

1. 在 Remix IDE 中编写 SimpleStorage.sol
2. 用 Solidity Compiler 编译（0.8.x 版本）
3. 环境选 Injected Provider - MetaMask（连 Sepolia 测试网）
4. 点 Deploy → MetaMask 签名 → 交易上链
5. 合约出现后，点 get() 读取（返回 0，免费）
6. 点 set() 写入值（花 gas，修改链上状态）
7. 再点 get() 验证（返回新值）

## 理解

### 什么是合约部署？
本质上是一笔特殊的交易——to 字段为空，data 字段是编译后的字节码。
节点执行这笔交易，把字节码写入链上，返回一个合约地址。
之后这个地址永远存在，任何人都可以通过 RPC 跟它交互。

### 什么是状态变更 vs 只读查询？
- get() 是 view 函数 → eth_call → 不花 gas → 不产生交易
- set() 改变 storedNumber → eth_sendTransaction → 花 gas → 产生交易记录

### Gas 去哪了？
Gas 是按操作计费的燃料。storedNumber 从 0 变 42，需要矿工/验证者执行并存储新状态，
所以付费。get() 只是读取，节点本地就能完成，不需要全网共识，免费。

### 为什么叫"最小智能合约"？
它只有两个函数，但包含了所有 dApp 的核心模式：
- 状态变量（storedNumber）
- 写函数（set，改变状态）
- 读函数（get，查询状态）
Uniswap 的 swap()、Aave 的 deposit()，本质就是更复杂的 set/get。

## 踩坑

- Remix 的 Injected Provider 选项被浏览器隐藏，需要点 Customize → 手动启用
- 部署后面板不自动显示合约，点 Deploy 再部署一次就出来了
- 验证合约是否在链上：用 curl 调 RPC 的 eth_call，不需要 Remix
