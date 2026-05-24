#!/usr/bin/env python3
"""命令行交互 SimpleStorage 合约 — 零依赖，纯标准库"""

import json
import hashlib
import urllib.request

RPC = "https://sepolia.gateway.tenderly.co"
CONTRACT = "0x80ac7a484a4759ccae47f735e12997361b58658f"


def keccak256(s: str) -> bytes:
    return hashlib.sha3_256(s.encode()).digest()


def call_rpc(method: str, params: list) -> dict:
    payload = json.dumps({"jsonrpc": "2.0", "method": method, "params": params, "id": 1}).encode()
    req = urllib.request.Request(RPC, data=payload, headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read())


def get():
    """读取 storedNumber（免费，不花 gas）"""
    selector = keccak256("get()")[:4].hex()
    result = call_rpc("eth_call", [{"to": CONTRACT, "data": f"0x{selector}"}, "latest"])
    value = int(result["result"], 16)
    print(f"storedNumber = {value}")
    return value


def set_help():
    """打印 set() 需要用到的 calldata"""
    print("\n=== 写入 set() 说明 ===")
    print("写操作需要私钥签名，这里打印 calldata 供备用。")
    print("格式: set(uint256)")
    selector = keccak256("set(uint256)")[:4].hex()
    print(f"函数选择器: 0x{selector}")
    print(f"合约地址: {CONTRACT}")
    print(f"示例 calldata (set 42):  0x{selector}{42:064x}")
    print(f"示例 calldata (set 888): 0x{selector}{888:064x}")
    print("\n在 Remix 的 Deployed Contracts → set 框里输入数字就行。")


if __name__ == "__main__":
    import sys
    cmd = sys.argv[1] if len(sys.argv) > 1 else "get"
    if cmd == "get":
        get()
    elif cmd == "set":
        set_help()
    else:
        print(f"用法: python3 {sys.argv[0]} get|set")
