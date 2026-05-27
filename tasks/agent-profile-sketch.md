# Agent Profile & Capability Declaration Sketch

## Selected Agent: Hermes Agent

### Agent Profile

| Field | Detail |
|-------|--------|
| **What it is** | Hermes Agent — an open-source AI terminal assistant that brings computer tools into the chat interface |
| **Maintained by** | Core team maintains the base framework; community contributes Skills/plugins (MetaMask + Snap model) |
| **Capabilities** | File read/write, terminal commands, Git management, external tool calling, learning management, information search |
| **Input / Output** | Natural language input → text or file output |
| **Calling methods** | CLI terminal, REST API, chat platforms (Feishu/Telegram), MCP protocol |
| **Pricing** | Free and open-source; pay-per-call or enterprise edition TBD |
| **Verification** | GitHub source audit + on-chain signature verification + community reputation (Stars/downloads) |
| **Failure handling** | Returns natural language explanation + error code; core team fixes core bugs, community fixes Skills plugin bugs |

---

### Design Rationale

- **Why open-source?** Trust. Anyone can read the code, anyone can run their own instance. No black box.
- **Why plugins (like MetaMask Snaps)?** One core team can't build every feature. Let the community extend it.
- **Why three-layer verification?** GitHub audit covers code-level trust, on-chain signature proves the running instance identity, community reputation gives social proof.
- **Why MCP alongside CLI/API?** CLI for humans, API for programs, chat platforms for non-technical users, MCP for other agents.

---

## Bonus: MCP vs A2A Comparison

|  | MCP | A2A |
|------|-----|------|
| **Full name** | Model Context Protocol | Agent-to-Agent |
| **What it connects** | Agent ⟷ Tools & Apps | Agent ⟷ Agent |
| **Real-world example** | Hermes calls your file system or runs a terminal command | One Hermes hands a data-fetching task to another Hermes |
| **Core question** | "How does an AI use this tool?" | "How do two AIs work together?" |
| **Common use** | Tool calling, data access, context injection | Task delegation, multi-agent workflows, negotiation |
| **Who defines it** | Anthropic (open standard) | Google (open protocol) |
| **Key insight** | Standardize the tool interface so any AI can use any tool | Standardize the agent interface so any agent can talk to any agent |

### Why both matter

MCP and A2A solve different layers of the same problem — an open AI ecosystem:

- **MCP** handles the vertical connection: an agent reaching down to use tools and data sources
- **A2A** handles the horizontal connection: agents talking to peers

A complete agent system needs both. Without MCP, your agent is blind and handless. Without A2A, your agent works alone when it should collaborate.
