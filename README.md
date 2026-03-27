# YUCLAW Trust — ZKP Signal Verification

Verify any YUCLAW signal has a cryptographic proof on Ethereum Sepolia.

## Verify a signal
```bash
git clone https://github.com/YuClawLab/yuclaw-trust
cd yuclaw-trust
python3 verify.py LUNR
```

Output:
```
YUCLAW Trust — Verifying LUNR
========================================
  Local proof found
  Hash: 36980a0bb5f89dc3258970977b76d9c7...
  On-chain: YES
  Block: 10515603
  Explorer: https://sepolia.etherscan.io/tx/651aa6b4...
```

## List all proofs
```bash
python3 verify.py
```

## Verified signals

| Ticker | Signal | Block | Date |
|---|---|---|---|
| LUNR | STRONG_BUY | 10515603 | 2026-03-24 |
| ASTS | STRONG_BUY | 10515603 | 2026-03-24 |
| MRNA | STRONG_BUY | 10515603 | 2026-03-24 |
| LUNR | +14.68% CORRECT | 10515734 | 2026-03-24 |
| DELL | +4.01% CORRECT | 10515736 | 2026-03-24 |
| LUNR | Day 3 CORRECT | 10522560 | 2026-03-25 |

## What this proves

- YUCLAW generated a signal for this ticker
- The signal was recorded with a cryptographic hash
- The proof is permanently on Ethereum Sepolia blockchain
- The proof cannot be faked or altered after the fact

No other AI trading system has verifiable proof of its signals.

## Connect to YUCLAW
```bash
pip install yuclaw
yuclaw zkp        # Show ZKP proofs
yuclaw signals    # Show current signals
yuclaw start      # Start all engines
```

## Links

- Dashboard: https://yuclawlab.github.io/yuclaw-brain
- GitHub: https://github.com/YuClawLab
- Wallet: 0x2c7736822714887143d524e6409b0cFDdaE86005
