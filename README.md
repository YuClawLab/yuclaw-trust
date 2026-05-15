<div align="center">

# YUCLAW-TRUST

**Hash-Anchored Audit Trail + ZKP Design Specification**

![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![Network](https://img.shields.io/badge/network-Ethereum_Sepolia-627EEA)
![Audit](https://img.shields.io/badge/audit-SHA--256_hash_chain-orange)
![Status](https://img.shields.io/badge/status-design_spec-yellow)
![License](https://img.shields.io/badge/license-MIT-red)

> SHA-256 hash chain of YUCLAW signal decisions, with selected hashes
> anchored on Ethereum Sepolia testnet by yuclaw-brain. Includes a Circom 2.0
> design specification for a future zk-SNARK compliance circuit.

</div>

---

> **Status — partial implementation, design-spec for zk-SNARK**
>
> | What is real today | What is on the roadmap |
> |---|---|
> | SHA-256 hash chain of decision payloads (`scripts/prove.py`) | Compiled zk-SNARK circuit with proving + verification keys |
> | Local proof-file inspection (`verify.py`) | On-chain proof verification (calling Sepolia from `verify.py` directly) |
> | Selected hashes anchored on Sepolia by yuclaw-brain | Anchoring every signal automatically |
> | Circom 2.0 design spec for a compliance circuit | Circuit compiled, witness generator, trusted setup |
>
> The hash chain and the on-chain anchoring are working today. The Groth16
> zk-SNARK proof generation described in the Circom file is **not yet wired
> up** — current proofs are SHA-256 hash anchors, not zk-SNARK proofs of
> strategy correctness.

---

## What this repo contains

| File | Purpose | LOC |
|---|---|---:|
| `scripts/prove.py` | SHA-256 hash-chain proof generator | 152 |
| `verify.py` | Local proof-file inspector | 84 |
| `circuits/compliance.circom` | Circom 2.0 circuit design spec (not compiled) | 85 |

Total: **321 lines** across two Python scripts and one Circom source.

---

## What's actually anchored on Sepolia

The yuclaw-brain pipeline publishes selected signal-decision hashes to
Ethereum Sepolia testnet. Several real anchors exist; example:

| Block | Date | Anchor |
|:---|:---:|:---|
| 10515603 | 2026-03-24 | Batch of STRONG_BUY signal hashes |
| 10515736 | 2026-03-24 | Follow-up batch |
| 10522560 | 2026-03-25 | Day 3 audit anchor |

Each anchor stores a hash of the signal-decision payload — **not** a
zk-SNARK proof. The on-chain record proves that the hash existed at that
block height; it does not (yet) prove the underlying strategy was
compliant in zero knowledge.

You can confirm anchors directly on [Ethereum Sepolia
Etherscan](https://sepolia.etherscan.io).

---

## Inspect local proofs

```bash
git clone https://github.com/YuClawLab/yuclaw-trust
cd yuclaw-trust
python3 verify.py
python3 verify.py LUNR
```

`verify.py` is a local audit-log inspector. It reads proof files at
`~/yuclaw/output/zkp_onchain/*.json` and prints their hash and recorded
anchor metadata. The on-chain anchoring is performed by yuclaw-brain when
the signal is first recorded, and the Etherscan transaction is the source
of truth. To verify the on-chain anchor directly, follow the Etherscan link
in the table above.

---

## Generate a hash-chain proof

```bash
python3 scripts/prove.py --position 50000 --portfolio 1000000 --limit 500
```

This generates a SHA-256-chained `ComplianceProof` record claiming that a
$50K position in a $1M portfolio is within a 5% (500 bps) risk limit. The
proof is appended to a local `audit_proofs.json` ledger; each entry chains
to the previous entry's hash.

Output `proof_type` is currently always `"hash_chain"`. The Groth16 path
described in the docstring activates when a compiled Circom artifact + key
material is present — neither is shipped today.

---

## The Circom design spec

`circuits/compliance.circom` is a Circom 2.0 specification for a
compliance circuit:

- **Public input**: `risk_limit_bps` (e.g., 500 = 5%)
- **Private inputs**: `position_size`, `portfolio_value`, `trade_pnl`
- **Constraint**: `position_size · 10000 ≤ portfolio_value · risk_limit_bps`

When compiled with a trusted setup, this circuit would let a prover
demonstrate "my trade was within the risk limit" without revealing the
position size or portfolio value. **No proving key, verification key, or
witness generator is in this repository**, so the circuit is currently a
design artifact, not an executable proof system.

---

## Honest framing

What we have today: **a tamper-evident audit log.** Each decision is
hashed; hashes chain; selected hashes are anchored on Sepolia. Anyone can
verify a hash exists at a block height and matches a published decision.

What we do **not** yet have: a zero-knowledge proof of strategy
correctness. Calling our current artifact a "zk-SNARK proof" overstates
what's running. The Circom circuit is the design for that future system;
turning it on means compiling the circuit, running a trusted setup, and
wiring the witness generator into `prove.py`.

---

## Ecosystem

| | |
|:---|:---|
| Production pipeline | [yuclaw-brain](https://github.com/YuClawLab/yuclaw-brain) |
| Live dashboard | [yuclawlab.github.io/yuclaw-brain](https://yuclawlab.github.io/yuclaw-brain) |
| PyPI | [pypi.org/project/yuclaw](https://pypi.org/project/yuclaw) |
| Anchoring wallet | `0x2c7736822714887143d524e6409b0cFDdaE86005` |
| Explorer | [Ethereum Sepolia](https://sepolia.etherscan.io) |

---

## Disclaimer

YUCLAW is open-source research and educational software. **It is NOT
financial advice or a recommendation to buy or sell any security.** Hash
anchoring on a testnet establishes timestamped existence of a payload; it
does not by itself imply the underlying strategy is profitable, compliant
in your jurisdiction, or suitable for any investment purpose. Trading
involves substantial risk of loss.

For educational and research purposes only. MIT Licensed.

---

<div align="center">

*Every YUCLAW signal-decision hash, anchored on Sepolia by yuclaw-brain.*

</div>
