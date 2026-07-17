<div align="center">

# YUCLAW-TRUST

**Git-Anchored Verified Research Ledger**

![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![Ledger](https://img.shields.io/badge/ledger-git--anchored-blue)
![Audit](https://img.shields.io/badge/audit-SHA--256_daily_roots-orange)
![Status](https://img.shields.io/badge/status-live_daily-green)
![License](https://img.shields.io/badge/license-MIT-red)

> SHA-256 hash-chain audit log for YUCLAW research signals.
> Git-anchored — clone and verify independently.

</div>

---

## The live artifact: `verified_research_ledger.jsonl`

This file is the Verified Research Ledger. It is written **daily by
[yuclaw-brain](https://github.com/YuClawLab/yuclaw-brain) before its public
pages update** (one commit per trading day, e.g.
`ledger: 2026-07-16 — 79 signals, root 6989db4d3ee7`), so the git history of
this repository is the tamper-evidence: editing a past day would rewrite
published commits.

One JSON line per day:

```json
{"date": "2026-07-16",
 "generated_at": "2026-07-16T23:00:05+00:00",
 "snapshot_count": 79,
 "daily_root": "6989db4d3ee7f22e9a8bedfecabfcbdfe539abf6245ff9974f334524690e4ff1",
 "entries": [{"ticker": "AAPL",
              "snapshot_id": "snap_AAPL_92b30577f9dd8cc6",
              "signal_label": "WATCH",
              "content_hash": "9ce0d0d9…"}, "…"]}
```

- **`content_hash`** — sha-256 of each signal snapshot's canonical content.
- **`daily_root`** — sha-256 over the day's sorted, `|`-joined content
  hashes: one 64-hex root per day. Sorting makes the root independent of
  database row order.

### Clone and verify

```bash
# Reproduce every published Validation Lab statistic AND recompute every
# ledger leaf + daily root against this repository:
pip install yuclaw
yuclaw replay-lab            # exit 0 = statistics and roots reproduced

# Standalone path (Python ≥ 3.10 stdlib only, no installs):
curl -sO https://yuclawlab.github.io/yuclaw-brain/replay/lab_replay_bundle.json
curl -sO https://raw.githubusercontent.com/YuClawLab/yuclaw-brain/main/tools/replay_lab.py
python3 replay_lab.py lab_replay_bundle.json

# Check one signal on one date against its ledger row:
yuclaw verify AAPL --date 2026-07-16
```

`yuclaw replay-lab` recomputes each leaf hash and each daily root from
published derived data and compares them to this file; any mismatch exits
non-zero with a diff report. `yuclaw verify` checks a single snapshot's
content hash against its ledger entry. Both check **record integrity and
timing — not investment merit.**

---

## Historical experiments — March 2026, retired

Before v3.0, YUCLAW experimented with on-chain anchoring and a zk-SNARK
design. These artifacts are preserved as historical record; none of them
runs today.

| File | What it was |
|---|---|
| `scripts/prove.py` | SHA-256 hash-chain proof generator (historical) |
| `verify.py` | Local inspector for the retired proof files (historical) |
| `circuits/compliance.circom` | Circom 2.0 design artifact — no longer planned (see its in-file HISTORICAL note) |

### Sepolia anchors (historical record)

During the March 2026 experiment, selected hashes were published to
Ethereum Sepolia testnet by yuclaw-brain. The anchors remain visible
on-chain; block numbers preserved verbatim:

| Block | Date | Anchor |
|:---|:---:|:---|
| 10515603 | 2026-03-24 | signal-decision hash batch (pre-v3 label vocabulary) |
| 10515736 | 2026-03-24 | signal-decision hash batch (pre-v3 label vocabulary) |
| 10522560 | 2026-03-25 | signal-decision hash batch (pre-v3 label vocabulary) |

Each anchor stored a hash of a signal-decision payload — not a zk-SNARK
proof. They can still be confirmed on
[Ethereum Sepolia Etherscan](https://sepolia.etherscan.io); the last
anchors were published during the March 2026 experiment, and anchoring was
retired at v3.0.

### `scripts/prove.py` (historical)

The hash-chain prover generated `ComplianceProof` records around a
position/portfolio risk-limit example. That example was a design-era demo:
**YUCLAW is research-only and holds no positions.** The Groth16 path in its
docstring was never wired up — no proving key, verification key, or witness
generator was ever shipped.

### `circuits/compliance.circom` (historical)

A Circom 2.0 design artifact for a risk-limit circuit (public
`risk_limit_bps`; private `position_size`, `portfolio_value`,
`trade_pnl`). It was never compiled and is no longer planned — the file
carries the same HISTORICAL note at the top of its source.

On-chain and zero-knowledge directions were retired at v3.0 in favor of the
public git ledger above.

---

## Ecosystem

| | |
|:---|:---|
| Production pipeline | [yuclaw-brain](https://github.com/YuClawLab/yuclaw-brain) |
| Live dashboard | [yuclawlab.github.io/yuclaw-brain](https://yuclawlab.github.io/yuclaw-brain) |
| PyPI | [pypi.org/project/yuclaw](https://pypi.org/project/yuclaw) |
| Historical anchoring wallet (retired) | `0x2c7736822714887143d524e6409b0cFDdaE86005` |
| Explorer | [Ethereum Sepolia](https://sepolia.etherscan.io) (historical anchors) |

---

## Disclaimer

YUCLAW is open-source research and educational software. **It is NOT
financial advice or a recommendation to buy or sell any security.** Hash
anchoring establishes timestamped existence of a payload; it does not by
itself imply the underlying research is profitable, compliant in your
jurisdiction, or suitable for any investment purpose. Trading involves
substantial risk of loss.

For educational and research purposes only. MIT Licensed.

---

<div align="center">

*Every YUCLAW signal snapshot, hashed daily into a public git ledger —
clone and verify independently.*

</div>
