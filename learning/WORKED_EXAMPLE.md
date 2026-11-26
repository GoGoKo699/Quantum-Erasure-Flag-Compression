# Read a quantum flag after measuring the syndrome

The nine-pair code uses a check $`X_{2i}X_{2i+1}`$ on each pair. Its checks between neighboring pairs are $`Z_{2i}Z_{2i+1}Z_{2i+2}Z_{2i+3}`$. Write $`\overline Z=Z_{2i}Z_{2i+1}`$ for the same logical action, whichever pair represents it. In each example exactly one pair check is negative, and all the checks between pairs are positive. Consider what the decoder can infer at that point. [Code and event table](../science/construction.md)

The checks between pairs show that the parities of the errors' $`X`$ components all agree. Every event leaves a pair untouched, so the common parity is zero. Each event replaces at most one site in any pair. Thus the observed syndrome is consistent with a single $`Z`$ on one side of the pair with the negative check and identity on the other sites. The two sides have the same syndrome because a $`Z`$ at either site anticommutes with the pair's $`XX`$ check.

## A syndrome with two candidate events

The first pair, with sites 0 and 1, is replaced on its left for label 0 and on its right for label 2. If this is the only pair with a negative check, the two possibilities are:

| Event label | Compatible Pauli on the data | Normalized flag in four dimensions | Residual after the tentative correction $`Z_0`$ |
|---|---|---|---|
| 0 | $`Z_0`$ | $`(0,0,1,0)`$ | $`I`$ |
| 2 | $`Z_1`$ | $`(0,1,0,0)`$ | $`\overline Z`$ |

The decoder measures the flag with projections onto these two coordinate lines and their orthogonal complement. The complement has probability zero for this syndrome. The first line means the tentative correction was sufficient. The second means the decoder must apply $`\overline Z`$ before decoding. If the same classical symbol were used for both labels, identical syndromes would demand incompatible corrections. Those two events form one edge of the conflict graph.

## A syndrome that needs only a correction class

Use the same pattern of check signs with the negative check now in pair 3, on sites 6 and 7. The candidate event labels on the left are 1 and 13, and those on the right are 3, 4, 8 and 12. If the decoder applies $`Z_6`$ tentatively, the labels on the left give logical identity and all the labels on the right give $`\overline Z`$.

Writing unnormalized flag vectors to display their spans, the two subspaces are
```math
\begin{aligned}
L&=\mathrm{span}\{(0,1,-1,0),(0,0,0,1)\},\\
R&=\mathrm{span}\{(0,1,1,0),(1,0,0,0)\}.
\end{aligned}
```
The first pair of vectors spans all left flags. Every right flag lies in the second span, and both spans are two-dimensional and orthogonal. A projective measurement with effects $`\Pi_L,\Pi_R`$ therefore selects the correct logical action. Within the right class, for example, the normalized flags for labels 4 and 8 have inner product $`1/\sqrt3`$. The decoder needs only their common correction.

The flag measurement depends on the syndrome. The same transmitted four-dimensional register can support these different measurements because the receiver chooses the projections after learning which logical alternatives remain. The complete decoder handles every syndrome by grouping its compatible labels according to their remaining logical correction. The recovery acts as the identity channel on the logical input, so it preserves any untouched reference. [General decoder](../science/construction.md) · [Learning map](MILESTONES.md)
