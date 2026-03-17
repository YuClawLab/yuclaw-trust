# Yuclaw-Trust — ZKP Cryptographic Audit Vault

**Zero-knowledge proof audit trail for AI-driven financial decisions.**

Every YUCLAW decision is cryptographically sealed with zk-SNARK proofs — proving compliance without revealing proprietary strategy logic.

## Overview

Yuclaw-Trust provides tamper-proof auditability for the YUCLAW ATROS system. Each AI decision (research conclusion, strategy validation, trade signal) is hashed, timestamped, and anchored with a zero-knowledge proof that verifies computational integrity without exposing model weights or prompt content.

## Key Features

- **zk-SNARK proofs** — prove a decision followed the stated policy without revealing the policy
- **SHA-256 hash chain** — append-only ledger with cryptographic linking
- **Audit receipts** — unique receipt ID for every decision, queryable and verifiable
- **Regulatory ready** — structured export for compliance review (MiFID II, SEC)
- **Offline verifiable** — proofs can be checked without access to the original model

## Architecture

```
YUCLAW Decision
       │
       ▼
┌──────────────┐
│  Hash Engine │──▶ SHA-256 chain
│  (decision)  │
└──────┬───────┘
       │
       ▼
┌──────────────┐
│  ZKP Circuit │──▶ zk-SNARK proof
│  (Groth16)   │
└──────┬───────┘
       │
       ▼
┌──────────────┐
│ Audit Ledger │──▶ SQLite + JSON export
│ (immutable)  │
└──────────────┘
```

## Audit Receipt Format

```json
{
  "receipt_id": "rcpt_1773720203958717811_e8d726d8",
  "timestamp": "2026-03-16T21:57:03Z",
  "decision_type": "strategy_validation",
  "verdict": "REJECTED",
  "hash": "e8d726d8517b9c9e...",
  "proof": "groth16:base64...",
  "verifiable": true
}
```

## Usage

```python
from yuclaw_trust import AuditVault

vault = AuditVault("audit.db")

# Seal a decision
receipt = vault.seal(
    decision_type="research",
    ticker="AAPL",
    verdict="BUY",
    evidence_hashes=["abc123...", "def456..."]
)

# Verify
assert vault.verify(receipt.receipt_id)

# Export for compliance
vault.export_json("audit_export.json")
```

## Verification

```bash
# Verify any receipt offline
python -m yuclaw_trust.verify --receipt rcpt_1773720203958717811_e8d726d8
# Output: VALID — decision integrity confirmed
```

## Part of YUCLAW ATROS

This is a component of the [YUCLAW ATROS](https://github.com/YuClawLab/yuclaw-brain) financial intelligence system.

## License

Proprietary — YuClawLab
