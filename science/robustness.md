# Finite fidelity and noisy flags

Use the full 18-qubit paired encoding, a uniform law on the 14 events, and simultaneous replacements at every site of the chosen event. Fidelity means the entanglement fidelity $`F_e`$ of the logical channel on half of a Bell pair. The encoder is fixed throughout the comparison. The replacement channel adds no other faults.

## Optimal classical fidelity

Let $`p(v,s,L)`$ denote the joint probability of event $`v`$, measured syndrome $`s`$, and residual logical Pauli class $`L`$ relative to a fixed syndrome correction. These probabilities are exactly enumerated by assigning the weight $`1/(14\,4^{|S_v|})`$ to each Pauli supported on $`S_v`$. The syndrome can be computed from the adjacent X parity differences and pair Z parities. One reference correction chooses the X parity solution with $`x_0=0`$ and places the indicated physical Z components on left sites. Then the residual logical class is specified by the actual first-pair X parity and the parity of the Z components on right sites. Physical phases are irrelevant.

For a set $`A`$ of labels assigned one classical symbol, define
```math
W(A)=\sum_s\max_L\sum_{v\in A}p(v,s,L).
```
The optimum over $`c`$ symbols is the maximum of $`\sum_j W(A_j)`$ over partitions into at most $`c`$ cells. To prove this, first read the classical symbol and the orthogonal syndrome subspace. The input is already a mixture over these orthogonal sectors. Inside a sector the remaining channel is a mixture of logical Paulis. For any further logical decoder, the entanglement fidelities for the four possible Pauli inputs sum to one. They are diagonal entries of the decoder's normalized Choi state in the Bell basis. Hence choosing the most likely inverse Pauli attains the optimum even among general quantum decoders. For any fixed decoder the objective is linear in the classical encoder's output probabilities, so deterministic encoders suffice. Shared classical randomness averages the performances of ordinary protocols and cannot improve the optimum.

For finite computation, set $`D(0,\varnothing)=0`$ and $`D(0,T)=-\infty`$ for nonempty $`T`$. Taking $`W(\varnothing)=0`$, apply
```math
D(j,T)=\max_{A\subseteq T}\{W(A)+D(j-1,T\setminus A)\}.
```
The result is $`D(c,V)`$, where $`V`$ is the event alphabet. All Pauli branch weights are integer multiples of $`1/(14\,4^6)`$. The [verifier](../verification/README.md) performs the syndrome enumeration and partition recurrence with integer weights.

| Number of available symbols | Optimal fidelity |
| ---: | ---: |
| 1 | 12693/14336 |
| 2 | 28247/28672 |
| 3 | 28631/28672 |
| 4 | 7167/7168 |
| 5 | 1 |

For example, an optimal four-symbol partition is $`\{0,13\}`$, $`\{1,7,10,11\}`$, $`\{2,3,4,12\}`$, $`\{5,6,8,9\}`$. Thus even with uniform probabilities and arbitrary local decoding, perfect two-bit transmission costs $`1/7168`$ in entanglement fidelity relative to the noiseless two-qubit flag.

## Heralded loss of the whole flag

Suppose the quantum link independently erases the entire four-dimensional flag with probability $`q`$ and reports whether the flag survived. The monitor has no extra channel to the receiver. Conditioned on survival, the syndrome-conditioned decoder attains fidelity one. Conditioned on flag loss, the receiver has only the corrupted data, so the one-symbol optimum in the table applies. The best fidelity with this link is therefore exactly
```math
F_e^{\mathrm{flag}}(q)
=1-\frac{1643}{14336}q.
```
It beats the perfect two-bit classical link precisely for $`q<2/1643`$, with equality at the threshold. This comparison singles out heralded loss of the whole flag, with its erasure indicator available to the decoder.

## Unheralded depolarization of the ray flags

Keep the stated four-dimensional ray encoding and replace the transmitted flag with $`I/4`$ with probability $`q`$, with no erasure indicator. The best decoder for these given ray flags beats a perfect two-bit classical link exactly when $`q<1/1516`$. This threshold concerns the given flag states. Optimizing the flag states for the noisy channel is a separate problem.

After a syndrome and its reference correction, the possible logical classes differ only by logical Z. Let $`A_s`$ and $`B_s`$ be the unnormalized flag states for the two classes, with $`a_s=\mathrm{Tr} A_s\le b_s=\mathrm{Tr}B_s`$. Their supports are orthogonal. A decoder with arbitrary joint operations on flag and logical data can be tested against each Pauli error on an input Bell pair. For a given flag state, those four fidelities sum to one by the Bell basis argument above. Each fidelity is also a positive linear functional of the incoming flag state. They therefore define four positive effects that sum to the identity. This realizes the same fidelity as a flag POVM followed by a Pauli correction. The best correction is accordingly the binary Helstrom decision for the two nonzero classes.

After depolarization, the minority-minus-majority difference is
```math
(1-q)(A_s-B_s)-q(b_s-a_s)I/4.
```
The optimum minority decision projects onto its positive eigenspace. On the minority's support, the [exact verifier](../verification/README.md) checks positive definiteness at $`q=1/1516`$ using rational arithmetic. Positivity there and at zero gives the full interval by linearity. Outside that support the difference is nonpositive. Thus for $`0\le q\le1/1516`$ one can measure the projection onto the minority support and assign its complement to the majority. At a syndrome with zero minority mass the decoder always chooses the majority.

Writing $`r_s=\mathrm{rank} A_s`$, the resulting infidelity is
```math
q\sum_s\left(a_s+(b_s-a_s)r_s/4\right)
= q\frac{379}{1792}.
```
At $`q=1/1516`$ this equals the perfect two-bit classical infidelity $`1/7168`$. Depolarization parameters are ordered by further channel composition, so the optimized fidelity cannot rise beyond the threshold. The verifier computes the coefficient and tests the positive eigenspace certificate.

## General flag perturbations

For a flag channel that changes every ideal ray density matrix by trace distance at most $`\eta`$, the ideal decoder has average entanglement fidelity at least $`1-\eta`$. Tensoring the conditional data and reference output with the flag preserves trace distance, and both averaging and the decoder are contractive. The fidelity is the probability of projection onto the Bell state. This bound gives a strict separation from a perfect two-bit classical link whenever $`\eta<1/7168`$. More detailed thresholds depend on how the flag channel acts on the particular ray states and on the data-noise model.
