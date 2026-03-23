# StableBank

**A decentralized savings protocol on Solana.**
> Deposit SOL. We stake it. You earn. No banks. No middlemen.

---

## The Idea

Traditional banks take your money, lend it out at 10–20%, and pay you back 0.5%.
StableBank flips that. Your SOL gets staked on existing Solana protocols — you keep the yield.

No LP. No trading. No complexity.
Just **deposit → stake → earn.**

---

## How It Works

```
User sends SOL to StableBank
           |
           v
StableBank stakes it natively on Solana
           |
           v
Staking yield accumulates (6–9% APY)
           |
           v
User earns yield on their balance
           |
           v
User withdraws SOL + earnings anytime
```

StableBank is the savings account that banks never gave you.

---

## Onramp / Offramp

StableBank is designed so that anyone — even without crypto knowledge — can use it.
No wallet setup. No SOL required upfront. Just savings that earn.

```
ONRAMP
User has Naira / USD
           |
           v
Pay via bank transfer, card, or mobile money
(Transak / Flutterwave)
           |
           v
SOL purchased automatically
           |
           v
SOL deposited into StableBank and starts earning

OFFRAMP
User wants to withdraw earnings
           |
           v
StableBank unstakes SOL
           |
           v
SOL converts to USDC via Jupiter swap
           |
           v
Transak / Flutterwave converts USDC to Naira / USD
           |
           v
Lands in user bank account
```

Onramp / Offramp providers:

| Provider | Coverage | Notes |
|---|---|---|
| Transak | Nigeria, 150+ countries | Naira + bank transfer support |
| Flutterwave | Nigeria first | Local bank transfer, cards |
| MoonPay | Global | Card payments |
| Onramp.money | Solana native | Direct SOL onramp |

---

## Staking Backends

StableBank does not build staking from scratch.
It sits on top of existing, battle-tested Solana staking protocols:

| Protocol | Type | Est. Yield |
|---|---|---|
| Native Solana Staking | Validator delegation | ~6-7% APY |
| Marinade Finance | Liquid Staking | ~7% APY |
| Jito | Liquid Staking + MEV | ~8-9% APY |
| Sanctum | LST Infrastructure | Varies |

StableBank routes deposits to these protocols and passes yield back to users minus a small protocol fee.

---

## Yield Aggregator (Phase 2)

StableBank will automatically route SOL to whichever protocol offers the best yield at any given time.

```
User deposits SOL
           |
           v
Aggregator checks all protocols in real time
Native: 6-7% | Marinade: 7% | Jito: 8-9% | Kamino: 10%+
           |
           v
SOL routed to best yield automatically
           |
           v
User always earns maximum available APY
```

---

## Agentic Yield Optimization (Phase 2)

An autonomous agent monitors yields 24/7 and rebalances deposits when better opportunities arise.
No human input required — the agent handles everything.

```
Agent monitors all protocol yields every epoch
           |
           v
Detects better opportunity
(e.g. Jito yield > Native by 1%)
           |
           v
Agent triggers rebalance automatically
           |
           v
SOL moves to higher yield protocol
           |
           v
User earns better yield without doing anything
```

When Phase 3 goes on-chain, the agent becomes a **crank** — an off-chain bot that triggers
on-chain rebalancing instructions through the Pinocchio program.

---

## Architecture

### Option A — Off-Chain (Phase 1, Complete)
A backend server holds a custodial wallet, receives user SOL, stakes natively on Solana, and tracks balances in a database.

- Cheapest to build, no deployment costs, ship fast
- Custodial — users trust you with their SOL
- Best for: personal testing and close circle of users

### Option B — Aggregator + Agent (Phase 2, Now)
Backend integrates multiple staking protocols. An autonomous agent monitors yields and rebalances automatically. Onramp/offramp added for Naira users.

- Still off-chain, no smart contract needed yet
- Agent handles yield optimization without human input
- Best for: expanding to more users with better yield

### Option C — Hybrid (Phase 3)
A lightweight Pinocchio program handles deposits and withdrawals. Backend agent triggers on-chain rebalancing as a crank.

- Partially trustless, lower cost than fully on-chain
- Best for: small public beta with real trust guarantees

### Option D — Fully On-Chain (Phase 4)
Everything lives in a Solana program. Non-custodial. Users always control their funds.

- Fully trustless, production-grade
- Best for: full public launch

> Current stage: Phase 2

---

## Tech Stack

| Layer | Tool |
|---|---|
| Blockchain | Solana |
| On-Chain Programs | Pinocchio |
| Backend | Rust (Axum, solana-sdk, solana-client) |
| Staking | Native Solana → Marinade → Jito (aggregated) |
| Agent | Rust async agent (tokio) |
| Database | SQLite (Phase 1-2) → PostgreSQL (Phase 3+) |
| Frontend | Next.js + TypeScript + Tailwind CSS |
| Wallet | Solana Wallet Adapter (Phantom, Solflare) |
| Onramp / Offramp | Transak / Flutterwave |
| RPC | Helius (free tier) |

---

## Project Structure

```
stablebank/
├── backend/                   # Rust backend (Axum)
│   ├── src/
│   │   ├── main.rs
│   │   ├── config.rs
│   │   ├── db.rs
│   │   ├── staking.rs
│   │   ├── marinade.rs
│   │   ├── aggregator.rs      # Phase 2 — yield comparator
│   │   ├── agent.rs           # Phase 2 — autonomous rebalancer
│   │   ├── wallet/
│   │   │   └── mod.rs
│   │   └── routes/
│   │       ├── mod.rs
│   │       ├── deposit.rs
│   │       ├── balance.rs
│   │       ├── withdraw.rs
│   │       └── config.rs
│   ├── Cargo.toml
│   └── .env
├── programs/                  # On-chain programs (Pinocchio) — Phase 3
│   └── stablebank/
│       └── src/
├── app/                       # Next.js frontend
│   ├── app/
│   │   ├── page.tsx
│   │   ├── layout.tsx
│   │   ├── providers.tsx
│   │   └── globals.css
│   ├── components/
│   │   └── WalletButton.tsx
│   ├── lib/
│   │   └── api.ts
│   └── hooks/
│       └── useStableBank.ts
├── docs/
│   ├── whitepaper.md
│   └── architecture.md
├── README.md
└── .gitignore
```

---

## Status

> Phase 2 — Aggregator + Agent

| Milestone | Status |
|---|---|
| Whitepaper v0.1 | Done |
| README | Done |
| Protocol wallet + Solana connection | Done |
| Deposit route + DB recording | Done |
| Native staking integration | Done |
| Balance + yield tracking route | Done |
| Withdraw + claim routes | Done |
| Frontend (deposit / balance / withdraw) | Done |
| Secure config route (no hardcoded addresses) | Done |
| Yield aggregator (Native + Marinade + Jito) | In progress |
| Autonomous yield agent | In progress |
| Onramp / Offramp (Transak / Flutterwave) | Up next |
| Pinocchio on-chain program | Phase 3 |
| Crank bot (agent triggers on-chain rebalancing) | Phase 3 |
| Security review | Phase 4 |
| Mainnet launch | Phase 4 |

---

## Roadmap

### Phase 1 — Off-Chain MVP (Complete)
- Backend with deposit, staking, balance, withdraw
- SQLite database tracking all user positions
- Frontend — deposit, dashboard, withdraw UI
- Phantom wallet integration
- Secure protocol config endpoint
- Test full cycle on devnet with personal SOL

### Phase 2 — Aggregator + Agent (Now)
- Integrate Marinade and Jito alongside native staking
- Yield aggregator — fetch and compare APY from all protocols in real time
- Auto route deposits to best available yield
- Autonomous agent — monitors yields every epoch, rebalances without human input
- Onramp / Offramp — Naira to SOL and back via Transak / Flutterwave
- Migrate database to PostgreSQL

### Phase 3 — Hybrid On-Chain
- Pinocchio program for non-custodial deposits and withdrawals
- Agent becomes a crank — triggers on-chain rebalancing instructions
- Apply for Solana Foundation grant
- Superteam Nigeria — community, funding, code review

### Phase 4 — Fully On-Chain
- Full Pinocchio program — users always control their funds
- TVL cap at launch, grow gradually
- Bug bounty on Immunefi
- Audit (Solana Foundation grant funded)
- Mainnet public launch

---

## Funding & Cost Reality

| Cost | Phase 1 | Phase 2 | Phase 3 | Phase 4 |
|---|---|---|---|---|
| Deployment | $0 | $0 | Low | Medium |
| RPC (Helius) | Free | Free / $9/mo | Paid | Paid |
| Hosting | Free | Free / cheap | Paid | Paid |
| Audit | Not needed | Not needed | Not needed | Required |
| Starting SOL | Your own | Your own | Protocol reserve | Protocol reserve |

Funding targets: Solana Foundation grants, Superteam Nigeria, Colosseum hackathons.

---

## Risks & Honesty

- Phase 1 and 2 are custodial. Early users are trusting you personally, not a smart contract. Be transparent about this.
- Staking protocols carry risk. Battle-tested but not risk-free.
- Slashing risk is near zero on Solana but worth monitoring.
- Agent rebalancing introduces execution risk — bad timing can cost fees. Thresholds are in place to only rebalance when yield difference justifies the cost.
- Regulatory landscape around crypto savings products is evolving. Build responsibly.

---

## Contributing

Solo project through Phase 2. Contributions will open in Phase 3.
Ideas and feedback? Open an issue.

---

## License

MIT — see LICENSE

---

*StableBank — because you should be your own bank.*
