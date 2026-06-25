import numpy as np

# --- 1. Parameters ---
N = 1000  # Total number of bits
SNR_dB = 10 # Signal-to-Noise Ratio in dB

# --- 2. Transmitter: Generate Bits and Map to Symbols ---
bits = np.random.randint(0, 2, N)
bit_pairs = bits.reshape((-1, 2))

# QPSK Mapping:
# Maps 2-bit sequences to a complex symbol (I, Q)
# The symbol energy is normalized to 1: sqrt((1/sqrt(2))^2 + (1/sqrt(2))^2) = 1
mapping = {
    (0, 0): (1/np.sqrt(2), 1/np.sqrt(2)),  # +1 + j1 (Phase 45 deg)
    (0, 1): (-1/np.sqrt(2), 1/np.sqrt(2)), # -1 + j1 (Phase 135 deg)
    (1, 1): (-1/np.sqrt(2), -1/np.sqrt(2)),# -1 - j1 (Phase 225 deg) - Note: Using 1,1 for 3rd quadrant
    (1, 0): (1/np.sqrt(2), -1/np.sqrt(2)), # +1 - j1 (Phase 315 deg)
}

I = []
Q = []
for b in bit_pairs:
    i_val, q_val = mapping[(b[0], b[1])]
    I.append(i_val)
    Q.append(q_val)

# Create the complex transmitted symbols (S = I + jQ)
I = np.array(I)
Q = np.array(Q)
symbols = I + 1j*Q

# --- 3. Channel: Add AWGN ---
SNR = 10**(SNR_dB/10)
# Noise power for unit energy symbols (E_s = 1) in complex baseband
# Noise variance per dimension (I and Q) is N0/2 = 1/(2*SNR)
noise_power_per_dim = 1/(2*SNR)

# Generate complex Gaussian noise: n = n_I + j*n_Q
noise = np.sqrt(noise_power_per_dim) * (np.random.randn(len(symbols)) + 1j * np.random.randn(len(symbols)))

# Received signal: R = S + N
rx = symbols + noise

# --- 4. Receiver: Demodulation and Bit Recovery ---
rx_I = np.real(rx)
rx_Q = np.imag(rx)

demod_bits = []

# Decision rule for QPSK: based on the sign of I and Q
for i, q in zip(rx_I, rx_Q):
    if i >= 0 and q >= 0:
        demod_bits.append([0, 0])
    elif i < 0 and q >= 0:
        demod_bits.append([0, 1])
    elif i < 0 and q < 0:
        demod_bits.append([1, 1]) # Matches mapping for (1,1)
    elif i >= 0 and q < 0:
        demod_bits.append([1, 0]) # Matches mapping for (1,0)

demod_bits = np.array(demod_bits)

# Flatten the arrays for comparison
original_bits = bits
demodulated_bits = demod_bits.flatten()

# --- 5. Performance Metrics ---
# Calculate the number of errors
errors = np.sum(original_bits != demodulated_bits)

# Calculate Bit Error Rate (BER)
BER = errors / N

# --- 6. Output ---
print(f"--- QPSK Simulation @ SNR = {SNR_dB} dB ---")
print(f"Total transmitted bits (N): {N}")
print(f"Total received symbol errors: {np.sum(np.any(bit_pairs != demod_bits, axis=1))}")
print(f"Total bit errors: {errors}")
print(f"Bit Error Rate (BER): {BER:.4f}")