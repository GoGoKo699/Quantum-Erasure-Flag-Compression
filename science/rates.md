# Exact flag costs under repetition

## One use

The three coordinate axes form a triangle. In a putative three-coloring name their colors X, Y, and Z. In each coordinate plane the two rays with exactly two nonzero coordinates are orthogonal. They must use the two axis colors for that plane, since both are orthogonal to the remaining axis.

For a body ray $(1,a,b,0)$, with $a,b\in\{1,-1\}$, its orthogonal two-coordinate rays lie in the XY, XZ, and YZ planes. Their directions have respective three-dimensional coordinates $(1,-a,0)$, $(1,0,-b)$, and $(0,1,-ab)$. Choose $a,b$ so the first two of these rays have colors X and Z. Negating both signs changes the first two colors to Y and X, and leaves the third ray unchanged. If the third ray has color Y, the original body ray sees all three colors. If it has color Z, the new body ray sees all three colors. Thus three colors fail. Four suffice by giving all body rays one fresh color. The apex adjoins every ray, so the full graph has chromatic number five. The listed four-dimensional rays and the clique of axes and apex give orthogonal rank four.

## Independent uses of the fixed encoding

Use $m$ independent copies of the event channel and the tensor product of the supplied code. The monitor communicates once about the whole event string. The decoder may act jointly on all data and flag systems. Each event-channel Kraus span contains the identity. Consequently the conflict graph is the OR power $G_{14}^{\lor m}$, in which two event strings conflict if any coordinate is an edge. In a conflicting coordinate choose a nonscalar cross product and choose identity products in all other coordinates. When all coordinate pairs are nonedges, every elementary tensor of cross products acts as a scalar, and the full span does also.

The quantum cost is exactly $2m$ qubits. Tensor products of the flag rays realize dimension $4^m$, and products of labels in the four-vertex clique form a clique of that size. The optimal classical cost per use tends to
```math
\lim_{m\to\infty}\frac{\lceil\log_2\chi(G_{14}^{\lor m})\rceil}{m}
=\log_2(46/11)\approx 2.0641.
```

To see why fractional coloring gives the rate, let $\chi_f(G)$ denote the minimum total weight on independent sets needed to cover each vertex to weight at least one. The dual maximizes the sum of nonnegative vertex weights subject to weight at most one on every independent set. An independent set of an OR product projects to an independent set in each coordinate. Multiplying optimal covers and optimal dual weights establishes multiplicativity of $\chi_f$ on these products. The inequality $\chi\ge\chi_f$ gives the lower rate. For a graph with $N$ vertices and fractional coloring weight $C$, draw independent sets with probabilities given by their weights divided by $C$. Each vertex has probability at least $1/C$ of being covered on a draw. Taking $\lceil C(1+\ln N)\rceil$ draws makes the probability of missing any vertex less than one. A resulting cover gives a coloring by assigning each vertex to one set that covers it. With $N=14^m$, the factor contributes a vanishing rate. These costs use zero error and fixed length. The event distribution within its full support does not change them.

## Fractional coloring certificate

The vertex weights in label order, scaled by 11, are
```text
3 3 3 3 2 3 2 3 3 3 2 3 2 11
```
They sum to 46. Every independent set has weight at most 11, which is verified by enumerating subsets of the 14 listed rays. An independent set is accepted when every pair in it has nonzero dot product. For the matching cover, assign these scaled weights to the indicated sets and zero to the others.

| Independent set | Weight times 11 |
| --- | ---: |
| 13 | 11 |
| 0, 1, 7, 10 | 5 |
| 0, 3, 4, 7 | 5 |
| 1, 2, 5, 6 | 4 |
| 1, 2, 10, 11 | 2 |
| 2, 3, 4, 5 | 3 |
| 2, 3, 11, 12 | 1 |
| 3, 9, 11, 12 | 2 |
| 5, 6, 8, 9 | 4 |
| 7, 8, 10, 11 | 1 |
| 8, 9, 11, 12 | 5 |
| 0, 4, 6, 10, 12 | 1 |
| 2, 4, 6, 10, 12 | 1 |
| 4, 6, 8, 10, 12 | 1 |

Each vertex receives weight 11. The primal and dual therefore both give $46/11$. The graph invariants and zero-error coding connection are attributed in [related work](related-work.md).
