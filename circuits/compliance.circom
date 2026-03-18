/*
 * yuclaw-trust/circuits/compliance.circom
 *
 * Zero-Knowledge Compliance Proof Circuit
 *
 * Proves that a trade was within risk limits without revealing:
 * - The strategy logic
 * - The exact position size
 * - The portfolio composition
 *
 * Public inputs: risk_limit_pct (e.g., 5% = 500 basis points)
 * Private inputs: position_size, portfolio_value, trade_pnl
 *
 * Circuit proves: position_size / portfolio_value <= risk_limit_pct / 10000
 * Equivalently: position_size * 10000 <= portfolio_value * risk_limit_pct
 */

pragma circom 2.0.0;

template LessThan(n) {
    signal input in[2];
    signal output out;

    component lt = Num2Bits(n);
    lt.in <== in[0] - in[1] + (1 << n);
    out <== 1 - lt.out[n];
}

template Num2Bits(n) {
    signal input in;
    signal output out[n+1];

    var lc = 0;
    for (var i = 0; i <= n; i++) {
        out[i] <-- (in >> i) & 1;
        out[i] * (out[i] - 1) === 0;
        lc += out[i] * (1 << i);
    }
    lc === in;
}

/*
 * Main compliance circuit.
 *
 * Proves: position_size * 10000 <= portfolio_value * risk_limit_bps
 * Without revealing position_size or portfolio_value.
 */
template ComplianceProof() {
    // Public input: risk limit in basis points (e.g., 500 = 5%)
    signal input risk_limit_bps;

    // Private inputs (hidden from verifier)
    signal input position_size;
    signal input portfolio_value;
    signal input trade_pnl;

    // Intermediate: compute both sides of the inequality
    signal position_scaled;
    signal limit_scaled;

    position_scaled <== position_size * 10000;
    limit_scaled <== portfolio_value * risk_limit_bps;

    // Prove: position_scaled <= limit_scaled
    // This is equivalent to: position_size / portfolio_value <= risk_limit_bps / 10000
    signal diff;
    diff <== limit_scaled - position_scaled;

    // diff must be non-negative (>= 0)
    // We prove this by showing diff fits in 64 bits (non-negative)
    component bits = Num2Bits(64);
    bits.in <== diff;

    // Also prove portfolio_value > 0 (non-trivial portfolio)
    signal pv_check;
    pv_check <== portfolio_value - 1;
    component pv_bits = Num2Bits(64);
    pv_bits.in <== pv_check;  // portfolio_value >= 1

    // Output: 1 if compliant
    signal output compliant;
    compliant <== 1;
}

component main {public [risk_limit_bps]} = ComplianceProof();
