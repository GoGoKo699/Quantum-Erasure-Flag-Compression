# Correction with an event flag

Alice prepares an encoded quantum state. A channel draws an event $`v`$ from a finite alphabet with positive probabilities and applies a channel $`\mathcal N_v`$ to the encoded state. The monitor learns $`v`$. It sends a flag state $`\sigma_v`$ in one fixed-dimensional output system, with no shared entanglement, feedback, or access to the encoded input. Bob receives the corrupted data and the flag and applies one decoder. Exact recovery requires the identity channel on the whole logical input, including states entangled with a reference. The transmitted flag dimension is the cost. A $`c`$-symbol classical flag occupies $`\lceil\log_2 c\rceil`$ fixed-length bits, and a dimension-$`d`$ quantum flag occupies $`\lceil\log_2 d\rceil`$ qubits.

The code is fixed unless a result explicitly concerns encoder choice. In the replacement model, event $`v`$ has support $`S_v`$. The channel traces out its carriers and inserts maximally mixed qubits in the same positions. The receiver has the original carrier labels and no separate erasure record. A replacement of $`S`$ can be written as a uniform mixture of the $`4^{|S|}`$ Pauli errors supported in $`S`$.

## Exact flag theorem

Let $`P`$ project onto the code, and let $`\mathcal E_v`$ be the linear span of the Kraus operators of $`\mathcal N_v`$. Assume each event is exactly correctable on that code. Define a graph $`G`$ with vertex set given by the events. Join $`v,w`$ when there are $`E\in\mathcal E_v`$ and $`F\in\mathcal E_w`$ with
```math
PE^\dagger FP\notin\mathbb C P.
```
Bilinearity makes this equivalent to checking operators in any pair of spanning sets. The condition is invariant under the Kraus representation. The minimum exact classical alphabet is the chromatic number $`\chi(G)`$. The minimum exact quantum dimension is the complex orthogonal rank $`\xi_{\mathbb C}(G)`$, the least dimension in which one can assign unit rays that are orthogonal on every edge.

To prove the claim, spectral-decompose a flag as $`\sigma_v=\sum_j\lambda_{vj}|f_{vj}\rangle\langle f_{vj}|`$, retaining its positive eigenvalues. The Kraus operators of the flagged mixture are $`\sqrt{p_v\lambda_{vj}}(E_{v,a}\otimes|f_{vj}\rangle)`$. Taking a product between the adjoint of one operator and another gives, up to a positive factor,
```math
\langle f_{vj}|f_{wk}\rangle P E_{v,a}^\dagger E_{w,b}P.
```
By Knill–Laflamme, all these products must be scalar on the code, which requires orthogonal flag supports across edges. Within an event the Knill–Laflamme condition holds by hypothesis. The same calculation gives sufficiency. Choosing one ray from each feasible support preserves all required orthogonalities. A classical flag has support on a fixed basis and any symbol used by both endpoints would violate the edge condition. Choosing one available symbol per vertex therefore gives a coloring, and a coloring gives a feasible deterministic encoder.

If an event is itself uncorrectable, an independent flag carrying the event label cannot correct it. The theorem describes a fixed input encoding, a single flag, noiseless flag transport, and joint decoding after transmission. Exact recovery of a full-support mixture enforces all its Kraus-product conditions regardless of the nonzero event probabilities. The [literature comparison](related-work.md) traces the relationship to classical zero-error functions and to flagged quantum channels.

## Union rule for replacement errors

For replacement events on supports $`S`$ and $`T`$ the span of all cross products equals the space of operators supported on $`S\cup T`$. The two Pauli factors can allocate any desired product Pauli to one of the input supports at each site. Hence two individually correctable replacement labels conflict exactly when the code cannot correct a replacement of their union. For a stabilizer code a support is correctable exactly when every Pauli on that support that commutes with all the checks acts as a scalar on the code. The remaining supported Paulis have zero projection within the code.
