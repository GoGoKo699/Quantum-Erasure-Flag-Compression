# The 18-qubit example

Place nine pairs on a line. Pair $i$ has carriers $2i$ and $2i+1$. Fourteen event labels correspond to the following real rays. Each entry stands for the unit vector in the indicated direction.

| Label | Ray | Label | Ray |
| --- | --- | --- | --- |
| 0 | `(0,0,1,0)` | 7 | `(1,0,-1,0)` |
| 1 | `(0,1,-1,0)` | 8 | `(1,0,0,0)` |
| 2 | `(0,1,0,0)` | 9 | `(1,0,1,0)` |
| 3 | `(0,1,1,0)` | 10 | `(1,1,-1,0)` |
| 4 | `(1,-1,-1,0)` | 11 | `(1,1,0,0)` |
| 5 | `(1,-1,0,0)` | 12 | `(1,1,1,0)` |
| 6 | `(1,-1,1,0)` | 13 | `(0,0,0,1)` |

For pair $i$, an event in column L replaces carrier $2i$, and an event in R replaces $2i+1$. Every other event leaves that pair unchanged. The full event replaces all its indicated carriers by maximally mixed qubits.

| Pair | L | R |
| --- | --- | --- |
| 0 | 0 | 2 |
| 1 | 0 | 8 |
| 2 | 2 | 8 |
| 3 | 1, 13 | 3, 4, 8, 12 |
| 4 | 3, 13 | 1, 6, 8, 10 |
| 5 | 5, 13 | 0, 10, 11, 12 |
| 6 | 7, 13 | 2, 6, 9, 12 |
| 7 | 9, 13 | 2, 4, 7, 10 |
| 8 | 11, 13 | 0, 4, 5, 6 |

The first three rows contain the pairs of coordinate axes of the three-dimensional rays. For each of the six rays $r$ with two nonzero coordinates, the subsequent rows put $r$ and label 13 on one side and the three-dimensional rays orthogonal to $r$ on the other. All cross edges are orthogonality edges. The six rows cover the orthogonality edges involving a two-coordinate ray. They also cover every edge incident to 13 because each three-dimensional ray has an orthogonal two-coordinate ray. Two rays with three nonzero entries can never be orthogonal, and a coordinate axis is never orthogonal to a three-coordinate ray. This accounts for every edge.

Any two labels jointly miss some pair, including when the labels are equal. A pair of labels containing at most one three-dimensional coordinate axis misses one of the first three pairs. Two distinct three-dimensional axes jointly miss a row whose two-coordinate ray has its zero in the third axis coordinate. Its right side contains that third axis as its only axis. Each event touches at most one carrier in a given pair.

## Code and conflict graph

Use stabilizers
```math
X_{2i}X_{2i+1}\quad (0\le i\le8),\qquad
Z_{2i}Z_{2i+1}Z_{2i+2}Z_{2i+3}\quad (0\le i\le7).
```
The checks commute and are independent. The two basis codewords are the nine-fold products of $|\Phi^+\rangle$ and $|\Psi^+\rangle$. Logical $\bar Z$ is $Z_{2i}Z_{2i+1}$ for any $i$. One representative of $\bar X$ is the product of $X$ on the nine left sites. The checks have weight at most four and occupy contiguous intervals of at most four carriers.

A Pauli supported on the union of two event supports commutes with the inner $XX$ checks precisely when its Z parity is even in each pair. Commuting with the adjacent $ZZZZ$ checks requires the X parities of all pairs to be equal. The common untouched pair forces these X parities to be zero. The remaining X components are products of the $XX$ stabilizers. An even Z parity on a pair contributes $\bar Z$ just when both sites carry a Z component. It follows that every individual event is correctable and that a pair of events conflicts exactly when some row has them on opposite shores. A single $Z$ on each of the two opposite sites gives a cross product that realizes the conflict.

Thus the conflict graph is the Yu–Oh orthogonality graph with a universal vertex, $G_{14}$. Its minimum classical alphabet is five, and the listed rays realize quantum dimension four. Optimality of dimension four follows from the four mutually orthogonal rays at labels 0, 2, 8, and 13. See [rates and graph certificates](rates.md).

## Syndrome-conditioned decoder

Measure the checks. Write the X and Z parity bits of a physical Pauli on pair $i$ as $x_i$ and $z_i$. The syndrome supplies all $z_i$ and all differences $\delta_i=x_i\oplus x_{i+1}$. Two Pauli explanations of the syndrome have the same X parities since their allowed label supports jointly miss a pair. The absolute X parity pattern can therefore be found by testing the two patterns compatible with the differences against allowed supports.

Choose one compatible physical Pauli as a reference and undo it. Every explanation for a given label differs from the reference by a stabilizer up to one logical Pauli class. The conditional label-to-class map is well defined by individual correctability. Distinct classes have pairwise orthogonal flag rays, since labels from classes with distinct logical action and the same syndrome are adjacent. Project the four-dimensional flag onto the orthogonal spans of the classes and apply the reported logical correction. The unused orthogonal complement may be assigned arbitrarily. After decoding, the resulting channel is the identity on the logical input. One may enumerate the possible Pauli explanations or use the pair parities directly. See [the optimal classical fidelity calculation](robustness.md#optimal-classical-fidelity).

## Reading the flag after the syndrome

A receiver who measures the flag independently of the data and keeps only a classical outcome cannot achieve exact recovery with any four-dimensional exact flag encoding for this example. The flag supports of the four clique labels are mutually orthogonal and fill the four-dimensional space, so each contains a single ray. An exact early measurement would have to distinguish those four flag states, because all four pairs conflict. Group its outcomes by which clique state can produce them. Outcomes produced by none have zero probability on every state, since the clique rays form a basis. Each group then has a positive effect supported on just one basis vector, and its total effect is the projector onto that vector. No outcomes inside a group carry further state-dependent information beyond the group apart from an independent random refinement. Exact correction after such a measurement would therefore require four classical symbols to suffice, in contradiction with the chromatic number. This argument permits arbitrary locally prepared measurement ancillas and classical outcome counts.

## Encoder choice

Without a flag, exact recovery is impossible for every encoder on these 18 carriers. The four axis and apex labels together replace every carrier. Partition the four labels into two groups of two. With no flag, the [union rule](model.md#union-rule-for-replacement-errors) forces the union of each group's supports to be correctable. The two surviving sets are disjoint. Exact decoding from each surviving set would clone an arbitrary logical qubit. The argument also rules out encoders given by channels. If such an encoder preceded an exactly correctable unflagged channel, include its Kraus operators in the Knill–Laflamme products on the logical input. Because the replacement errors span the identity, each nonzero encoder Kraus operator would be proportional to an isometry. Any one of those isometries would furnish an exactly correctable subspace, which the disjoint-survivor argument rules out.

A different encoding on the same channel reaches the lower bound of two flag symbols. It is also a CSS code and has check weight and span at most four. On consecutive carriers 2 through 6, use
```text
+XIXXI  +IXXXX  +ZZZII  +IZZZZ
```
and initialize the other 13 carriers in the single-site $+Z$ state. The four active checks commute and are independent. Logical Pauli representatives are $\bar X=X_3 X_4$ and $\bar Z=Z_4 Z_5$. Multiplying each by the corresponding pure-type stabilizers gives the following complete lists of supports.

| Logical coset | Supports |
| --- | --- |
| X | {3,4}, {2,3,5}, {2,4,6}, {5,6} |
| Z | {4,5}, {2,3,5}, {2,4,6}, {3,6} |

A support contains a nontrivial logical Pauli exactly when it contains a set from either list. For this CSS code a commuting Pauli has independently commuting X and Z components. If it acts nontrivially, at least one component acts nontrivially and is supported inside the original support.

The nonempty active replacement sets are event 0 on site 2, event 1 on site 6, event 2 on site 4, event 8 on sites 3 and 5, and event 13 on site 6. Send one bit indicating whether the event is 8. Every within-class union is a subset of one of $\{2,4\}$, $\{2,6\}$, $\{4,6\}$, or $\{3,5\}$, none of which contains a listed logical support. The [union rule](model.md#union-rule-for-replacement-errors) gives exact recovery for the two classes. The four conflicting pairs are $(0,8),(1,8),(2,8),(8,13)$. The zero-flag obstruction and this code establish a minimum of two classical symbols and quantum dimension two even within the stated CSS, check-weight, and span constraints. The alternative encoding concentrates the logical state into five active carriers. A task that fixes the original code space retains the five-symbol classical requirement.
