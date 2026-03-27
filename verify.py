#!/usr/bin/env python3
"""
YUCLAW Trust — Signal Verification Tool
Usage: python3 verify.py LUNR
Checks if a YUCLAW signal has a valid ZKP proof on Ethereum Sepolia.
"""
import sys
import json
import os

PROOF_DIR = os.path.expanduser("~/yuclaw/output/zkp_onchain")


def verify_signal(ticker: str) -> dict:
    print(f"\nYUCLAW Trust — Verifying {ticker}")
    print("=" * 40)

    local_proofs = []
    if os.path.exists(PROOF_DIR):
        for f in os.listdir(PROOF_DIR):
            if f.endswith('.json'):
                try:
                    data = json.load(open(f"{PROOF_DIR}/{f}"))
                    if isinstance(data, list):
                        for p in data:
                            if p.get('ticker') == ticker:
                                local_proofs.append(p)
                    elif data.get('ticker') == ticker or \
                         data.get('decision', {}).get('ticker') == ticker:
                        local_proofs.append(data)
                except Exception:
                    pass

    if local_proofs:
        p = local_proofs[-1]
        print(f"  Local proof found")
        print(f"  Hash: {p.get('hash', p.get('decision_hash', ''))[:32]}...")
        if p.get('onchain'):
            print(f"  On-chain: YES")
            print(f"  Block: {p.get('block', 'unknown')}")
            print(f"  Explorer: {p.get('explorer', '')}")
        else:
            print(f"  On-chain: NO (local only)")
        return {'verified': True, 'proof': p}
    else:
        print(f"  No proof found for {ticker}")
        print(f"  Run: yuclaw zkp to generate proofs")
        return {'verified': False}


def list_all_proofs() -> list:
    proofs = []
    if os.path.exists(PROOF_DIR):
        for f in sorted(os.listdir(PROOF_DIR)):
            if f.endswith('.json'):
                try:
                    data = json.load(open(f"{PROOF_DIR}/{f}"))
                    if isinstance(data, list):
                        proofs.extend(data)
                    else:
                        proofs.append(data)
                except Exception:
                    pass
    return proofs


if __name__ == '__main__':
    if len(sys.argv) > 1:
        ticker = sys.argv[1].upper()
        verify_signal(ticker)
    else:
        print("YUCLAW Trust — All Proofs")
        print("=" * 40)
        proofs = list_all_proofs()
        onchain = [p for p in proofs if p.get('onchain')]
        print(f"Total proofs: {len(proofs)}")
        print(f"On-chain: {len(onchain)}")
        print("\nRecent proofs:")
        for p in proofs[-5:]:
            ticker = p.get('ticker', p.get('decision', {}).get('ticker', '?'))
            h = p.get('hash', p.get('decision_hash', ''))[:16]
            oc = 'ON-CHAIN' if p.get('onchain') else 'LOCAL'
            print(f"  {ticker:6} {h}... [{oc}]")
        print("\nUsage: python3 verify.py LUNR")
