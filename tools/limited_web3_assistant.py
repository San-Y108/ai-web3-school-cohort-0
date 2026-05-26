#!/usr/bin/env python3
"""
受限 Web3 助手 CLI — 只读/检查型，零外部依赖

定位：AI×Web3 School Week 1 进阶任务
功能：解释操作、生成检查清单、链上只读查询、指导链上验证
绝对不做：连钱包、发交易、读私钥、写入链上状态
"""

from __future__ import annotations

import hashlib
import json
import sys
import urllib.request

CONTRACT = "0x80ac7a484a4759ccae47f735e12997361b58658f"
EXPLORER = "https://sepolia.etherscan.io"
NETWORK = "Sepolia"
RPC = "https://sepolia.gateway.tenderly.co"


def keccak256(s: str) -> bytes:
    # ⚠️ Python 的 hashlib.sha3_256 ≠ 以太坊的 keccak256
    # 这里只用于 calldata 教学展示，不用于真实 RPC 调用
    return hashlib.sha3_256(s.encode()).digest()


# 以太坊函数选择器（keccak256 的前 4 字节，硬编码，确保正确）
SELECTOR_GET = "6d4ce63c"       # get()
SELECTOR_SET = "60fe47b1"       # set(uint256)


# ── explain ──────────────────────────────────────────────────────────

def explain_get() -> None:
    print("=== 操作解释 ===")
    print("get() 是一个只读查询函数。")
    print("- 它通过 eth_call 发起，不产生交易")
    print("- 不需要 MetaMask 签名")
    print("- 不消耗 Gas")
    print("- 不会改变链上状态")
    print("- 返回值是当前 storedNumber 的值")
    print()
    print("=== 风险等级 ===")
    print("低 — 只读操作，无签名、无 gas、无状态变更")
    print()
    print("=== 操作步骤 ===")
    print("1. 在 Remix 的 Deployed Contracts 区域找到合约")
    print("2. 点击 get() 按钮（不需要在 MetaMask 确认）")
    print("3. 观察返回值")
    print()
    print("=== 异常提醒 ===")
    print("- 如果 MetaMask 弹出了签名窗口，说明你可能误点了其他函数，立即取消")
    print("- get() 不应该需要签名或支付 gas")


def explain_set(value: str | None) -> None:
    v = value if value else "<value>"
    print("=== 操作解释 ===")
    print(f"set({v}) 是一个写入操作，会改变合约的 storedNumber 状态。")
    print("- 它通过 eth_sendTransaction 发起，产生一笔交易")
    print("- 需要 MetaMask 签名（私钥授权）")
    print("- 消耗 Gas（Sepolia 测试币）")
    print("- 交易上链后不可撤销")
    print(f"- 执行后 storedNumber 会从当前值变为 {v}")
    print()
    print("=== 风险等级 ===")
    print("中 — 写入操作，需要签名和 gas，改变链上状态")
    print()
    print("=== 风险提醒 ===")
    print("⚠️ 这是一个写入操作，需要人工确认：")
    print()
    print("1. 签名 = 私钥授权 = 不可撤销")
    print("   - 一旦你在 MetaMask 点了「确认」，交易就会被广播到全网")
    print("   - 测试网无资产风险，但养成习惯很重要")
    print()
    print("2. AI 幻觉风险")
    print("   - 检查清单是「候选建议」，不是「最终命令」")
    print("   - 最终判断权在你手里")
    print()
    print("3. UI 显示 ≠ 链上真相")
    print("   - Remix 显示「成功」不代表链上真的成功")
    print("   - 必须用 Etherscan 验证")
    print()
    print("=== 后续步骤 ===")
    if value:
        print("运行 checklist 命令生成检查清单：")
        print(f"  python3 tools/limited_web3_assistant.py checklist set {value}")
    else:
        print("运行 checklist 命令生成检查清单：")
        print("  python3 tools/limited_web3_assistant.py checklist set <value>")


def cmd_explain(args: list[str]) -> None:
    if not args:
        print("用法：python3 tools/limited_web3_assistant.py explain <get|set> [value]")
        return
    op = args[0].lower()
    if op == "get":
        explain_get()
    elif op == "set":
        value = args[1] if len(args) > 1 else None
        explain_set(value)
    else:
        print(f"未知操作：{op}")
        print("用法：python3 tools/limited_web3_assistant.py explain <get|set> [value]")


# ── checklist ────────────────────────────────────────────────────────

def checklist_get() -> None:
    print("get() 是只读操作，风险极低。")
    print("检查清单：")
    print(f"□ 确认 MetaMask 连接的是 {NETWORK} 测试网")
    print(f"□ 确认合约地址是 {CONTRACT}")
    print("□ 确认调用的是 get()，不是 set()")


def checklist_set(value: str | None) -> None:
    v = value if value else "<value>"
    print(f"=== set({v}) 交易前检查清单 ===")
    print()
    print(f"□ 1. 网络：MetaMask 当前网络是不是 {NETWORK}？（不是主网！）")
    print(f"□ 2. 合约地址：目标地址是不是 {CONTRACT}？")
    print("□ 3. 函数：调用的是 set() 还是别的函数？")
    print(f"□ 4. 参数：输入的是不是 {v}？有没有多打或少打数字？")
    print(f"□ 5. value：交易的 ETH value 是不是 0？（SimpleStorage 的 set 不需要转 ETH）")
    print("□ 6. Gas：gas 费是否在合理范围内？（Sepolia 测试网通常几 Gwei）")
    print()
    print("=== MetaMask 弹窗检查 ===")
    print("当你点击 set() 后，MetaMask 会弹出确认窗口。请检查：")
    print(f"1. to 地址：是不是 {CONTRACT}？")
    print("2. value：是不是 0 ETH？（SimpleStorage 的 set 不需要转 ETH）")
    print("3. data：是否包含 set(uint256) 的函数选择器和参数")
    print("4. gas：是否在合理范围内？")
    print()
    print("如果任何一项不对，立即取消交易。")


def cmd_checklist(args: list[str]) -> None:
    if not args:
        print("用法：python3 tools/limited_web3_assistant.py checklist <get|set> [value]")
        return
    op = args[0].lower()
    if op == "get":
        checklist_get()
    elif op == "set":
        value = args[1] if len(args) > 1 else None
        checklist_set(value)
    else:
        print(f"未知操作：{op}")
        print("用法：python3 tools/limited_web3_assistant.py checklist <get|set> [value]")


# ── calldata ─────────────────────────────────────────────────────────

def cmd_calldata(args: list[str]) -> None:
    if not args:
        print("用法：python3 tools/limited_web3_assistant.py calldata <value>")
        print("value 必须是正整数")
        return
    raw = args[0]
    try:
        value = int(raw)
        if value <= 0:
            raise ValueError
    except ValueError:
        print(f"错误：{raw} 不是正整数。value 必须是正整数。")
        return

    selector = SELECTOR_SET
    padded = f"{value:064x}"
    calldata = f"0x{selector}{padded}"

    print(f"=== set({value}) 的 Calldata 结构 ===")
    print()
    print("函数签名：set(uint256)")
    print(f"函数选择器：0x{selector}（keccak256(\"set(uint256)\") 前 4 字节）")
    print(f"参数 {value} 的十六进制：0x{padded}（32 字节，左补零）")
    print(f"完整 calldata：{calldata}")
    print()
    print("=== 解读 ===")
    print("- 函数选择器告诉合约：我要调用 set()")
    print(f"- 后面 32 字节是参数：我要把 {value} 存进去")
    print("- 这就是 MetaMask 弹窗里 data 字段的内容")
    print("- 你不需要手动拼这个，Remix 会自动生成")
    print("- 但理解它有助于检查 MetaMask 弹窗是否正确")


# ── verify ───────────────────────────────────────────────────────────

def cmd_verify(args: list[str]) -> None:
    if not args:
        print("用法：python3 tools/limited_web3_assistant.py verify <tx_hash>")
        return
    tx_hash = args[0]
    if not tx_hash.startswith("0x") or len(tx_hash) != 66:
        print("交易哈希格式错误。正确格式：0x 开头，共 66 个字符。")
        print("示例：0x3875a5b77e029dbc735f376030e19c6668b0621b8db735f6d0869c915f5ab092")
        return

    link = f"{EXPLORER}/tx/{tx_hash}"

    print("=== Etherscan 验证清单 ===")
    print()
    print(f"交易链接：{link}")
    print()
    print("请打开上面的链接，逐项检查：")
    print()
    print("□ 1. Status（状态）")
    print("  正常值：Success")
    print("  异常处理：如果是 Failed，查看 revert reason（通常是参数错误或 gas 不足）")
    print()
    print("□ 2. from（发送方）")
    print("  正常值：你的钱包地址")
    print("  异常处理：如果不匹配，可能用了错误的账户")
    print()
    print("□ 3. to（接收方）")
    print(f"  正常值：{CONTRACT}")
    print("  异常处理：如果不匹配，可能调用了错误的合约")
    print()
    print("□ 4. Value（转账金额）")
    print("  正常值：0 ETH")
    print("  异常处理：如果非零，set() 不应该转 ETH，可能是误操作")
    print()
    print("□ 5. Gas Used（消耗的 gas）")
    print("  正常值：合理范围（~50,000）")
    print("  异常处理：如果异常高，可能是合约逻辑复杂或出错")
    print()
    print("□ 6. Block（所在区块）")
    print("  正常值：有区块号")
    print("  异常处理：如果显示 Pending，交易还在等待打包")
    print()
    print("=== 状态验证 ===")
    print("对于写入操作（如 set），还需要验证合约状态是否真的变了：")
    print("1. 再次调用 get() 读取 storedNumber")
    print("2. 返回值应该与你 set 的值一致")
    print("3. 如果不一致，可能调用了错误的合约或函数")
    print()
    print("=== 排查指南 ===")
    print("- Status = Failed → 查看 revert reason")
    print("- from 不匹配 → 检查 MetaMask 当前账户")
    print("- to 不匹配 → 检查 Remix 中连接的合约地址")
    print("- value 非零 → 检查是否误操作了「Send ETH」")
    print("- get() 返回值不对 → 检查是否调用了正确的合约")


# ── query (链上只读查询) ──────────────────────────────────────────────

def call_rpc(method: str, params: list) -> dict:
    """调用 Sepolia RPC，只用于只读查询（eth_call / eth_getTransactionReceipt）"""
    payload = json.dumps({"jsonrpc": "2.0", "method": method, "params": params, "id": 1}).encode()
    req = urllib.request.Request(RPC, data=payload, headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=10) as resp:
        return json.loads(resp.read())


def query_get() -> None:
    """调用 eth_call 读取链上 storedNumber（免费、不需要签名）"""
    selector = SELECTOR_GET
    print("=== 链上查询：get() ===")
    print()
    print(f"合约地址：{CONTRACT}")
    print(f"网络：{NETWORK}")
    print(f"RPC：{RPC}")
    print(f"Calldata：0x{selector}（get() 的函数选择器）")
    print()
    print("正在查询...")
    try:
        result = call_rpc("eth_call", [{"to": CONTRACT, "data": f"0x{selector}"}, "latest"])
        value = int(result["result"], 16)
        print()
        print(f"✅ 查询成功")
        print(f"storedNumber = {value}")
        print()
        print("=== 解读 ===")
        print(f"- 这是 SimpleStorage 合约当前存储的值")
        print(f"- 通过 eth_call 查询，不产生交易，不花 gas")
        if value == 0:
            print("- 返回 0 说明合约从未被写入过（或被 set(0) 重置了）")
        else:
            print(f"- 说明之前有人调用过 set({value})")
        print()
        print("=== 验证方式 ===")
        print("你可以在 Etherscan 上验证这个结果：")
        print(f"1. 打开 {EXPLORER}/address/{CONTRACT}")
        print("2. 点击 Contract → Read Contract")
        print("3. 点击 get()，对比返回值是否一致")
    except Exception as e:
        print()
        print(f"❌ 查询失败：{e}")
        print()
        print("可能原因：")
        print("- RPC 节点不可用（Tenderly 有时会限流）")
        print("- 网络问题")
        print("- 合约地址错误")
        print()
        print("替代方案：直接在 Etherscan 上查看：")
        print(f"  {EXPLORER}/address/{CONTRACT}#readContract")


def query_tx(tx_hash: str) -> None:
    """调用 eth_getTransactionReceipt 查询交易状态（免费、不需要签名）"""
    print("=== 链上查询：交易状态 ===")
    print()
    print(f"交易哈希：{tx_hash}")
    print(f"网络：{NETWORK}")
    print(f"RPC：{RPC}")
    print()
    print("正在查询...")
    try:
        receipt = call_rpc("eth_getTransactionReceipt", [tx_hash])
        r = receipt.get("result")
        if r is None:
            print()
            print("⚠️ 未找到交易收据")
            print()
            print("可能原因：")
            print("- 交易还在 Pending（等待打包）")
            print("- 交易哈希错误")
            print("- 交易发生在其他网络")
            print()
            print(f"请在 Etherscan 上手动检查：{EXPLORER}/tx/{tx_hash}")
            return

        status = "Success" if r.get("status") == "0x1" else "Failed"
        from_addr = r.get("from", "未知")
        to_addr = r.get("to", "未知（合约创建）")
        gas_used = int(r.get("gasUsed", "0x0"), 16)
        block = int(r.get("blockNumber", "0x0"), 16)
        contract_addr = r.get("contractAddress")

        print()
        print(f"✅ 查询成功")
        print()
        print(f"状态：{status}")
        print(f"from：{from_addr}")
        print(f"to：{to_addr}")
        print(f"Gas Used：{gas_used:,}")
        print(f"区块号：{block:,}")

        if contract_addr:
            print(f"创建的合约地址：{contract_addr}")

        print()
        print("=== 检查清单 ===")
        checks = [
            ("Status", status, status == "Success", "查看 revert reason"),
            ("to 地址", to_addr, to_addr.lower() == CONTRACT.lower(), "可能调用了错误的合约"),
            ("Gas Used", f"{gas_used:,}", gas_used < 100_000, "异常高，可能是合约逻辑复杂"),
        ]
        for name, val, ok, hint in checks:
            mark = "✅" if ok else "⚠️"
            print(f"  {mark} {name}：{val}" + ("" if ok else f"（{hint}）"))

        print()
        print(f"Etherscan 链接：{EXPLORER}/tx/{tx_hash}")

    except Exception as e:
        print()
        print(f"❌ 查询失败：{e}")
        print()
        print(f"替代方案：直接在 Etherscan 上查看：{EXPLORER}/tx/{tx_hash}")


def cmd_query(args: list[str]) -> None:
    if not args:
        print("用法：")
        print("  python3 tools/limited_web3_assistant.py query get")
        print("  python3 tools/limited_web3_assistant.py query tx <tx_hash>")
        print()
        print("query get  — 调用 RPC 读取链上 storedNumber（免费、只读）")
        print("query tx   — 调用 RPC 查询交易状态（免费、只读）")
        return
    sub = args[0].lower()
    if sub == "get":
        query_get()
    elif sub == "tx":
        if len(args) < 2:
            print("用法：python3 tools/limited_web3_assistant.py query tx <tx_hash>")
            return
        tx_hash = args[1]
        if not tx_hash.startswith("0x") or len(tx_hash) != 66:
            print("交易哈希格式错误。正确格式：0x 开头，共 66 个字符。")
            print("示例：0x3875a5b77e029dbc735f376030e19c6668b0621b8db735f6d0869c915f5ab092")
            return
        query_tx(tx_hash)
    else:
        print(f"未知子命令：{sub}")
        print("可用子命令：get、tx")


# ── usage ────────────────────────────────────────────────────────────

USAGE = """\
受限 Web3 助手 — 只读/检查型 CLI 工具
用法：python3 tools/limited_web3_assistant.py <命令> [参数]

命令：
  explain <get|set> [value]     解释 get 或 set 操作的含义和风险
  checklist <get|set> [value]   生成 set 操作的交易前检查清单
  calldata <value>              展示 set(value) 的 calldata 结构
  verify <tx_hash>              根据 tx hash 生成 Etherscan 验证清单
  query get                     调用 RPC 读取链上 storedNumber（免费、只读）
  query tx <tx_hash>            调用 RPC 查询交易状态（免费、只读）

示例：
  python3 tools/limited_web3_assistant.py explain get
  python3 tools/limited_web3_assistant.py explain set 42
  python3 tools/limited_web3_assistant.py checklist set 42
  python3 tools/limited_web3_assistant.py calldata 42
  python3 tools/limited_web3_assistant.py verify 0x3875a5b77e029dbc735f376030e19c6668b0621b8db735f6d0869c915f5ab092
  python3 tools/limited_web3_assistant.py query get
  python3 tools/limited_web3_assistant.py query tx 0x3875a5b77e029dbc735f376030e19c6668b0621b8db735f6d0869c915f5ab092

注意：query 命令会连接 RPC 节点进行只读查询（eth_call），不会发送交易或读取私钥。
""",


def main() -> None:
    if len(sys.argv) < 2:
        print(USAGE)
        return
    cmd = sys.argv[1].lower()
    args = sys.argv[2:]
    if cmd == "explain":
        cmd_explain(args)
    elif cmd == "checklist":
        cmd_checklist(args)
    elif cmd == "calldata":
        cmd_calldata(args)
    elif cmd == "verify":
        cmd_verify(args)
    elif cmd == "query":
        cmd_query(args)
    else:
        print(f"未知命令：{cmd}")
        print()
        print(USAGE)


if __name__ == "__main__":
    main()
