# Reproduce the finite results

Run from the repository root with Python 3.10 or later. The script uses only the standard library.

```sh
python3 verification/run_all.py
```

| Check | Expected result |
| --- | --- |
| Nine-block code | 18 physical qubits, 14 replacement events and 37 conflicting event pairs |
| Graph parameters | Chromatic number 5, fractional chromatic number 46/11 and orthogonal rank 4 |
| Alternative CSS encoding | Its four conflicts all involve event 8, so one classical bit suffices |
| Optimal entanglement fidelity with 1 through 5 classical symbols | 12693/14336, 28247/28672, 28631/28672, 7167/7168, 1 |
| Heralded erasure of the whole quantum flag | Threshold 2/1643 against perfect two-bit classical flags |
| Depolarization of the whole quantum flag | Threshold 1/1516 against perfect two-bit classical flags |

The code reconstructs the nine complete bipartite subgraphs from the unnormalized flag vectors. It compares their union with the orthogonality graph, checks that every event pair leaves a physical block untouched and checks that the four anchor events cover all sites. It verifies an independent-set primal and dual for the fractional coloring using integer weights. The fractional lower bound and an explicit five-coloring give the integral chromatic number. The four-clique and the flag vectors give the orthogonal rank.

For uniformly chosen events and simultaneous replacement at every affected site, each event gives an exact Pauli mixture. The script enumerates its Pauli branches, records stabilizer syndrome and logical class, and checks that the observed conflicts reproduce the graph. It computes the maximum-likelihood error for every candidate message group, then searches all partitions by dynamic programming. The counts use a common integer denominator. For the alternative encoding the script checks the stabilizers and logical operators, then solves the erasure support conditions by binary row elimination.

The noise thresholds apply to the 18-qubit encoding and the same uniform event law. Heralded flag erasure sends a distinct erasure outcome. Depolarization replaces the flag by the maximally mixed state with probability `p` and supplies no separate outcome. The depolarization check uses sets of rays compatible with each syndrome and exact rational Schur complements to certify the receiver's optimal decisions at the crossing.
