# Related work

## Exact recovery with side information

[Knill and Laflamme](https://doi.org/10.1103/PhysRevA.55.900) give the exact error-correction conditions. Here the event-labelled noise branches carry flag states at the decoder. Applying their conditions to the joint data and flag yields a graph whose edges specify where flag supports must be orthogonal. This formulation also applies to non-Pauli event channels on a fixed, individually correctable code. [Gregoratti and Werner](https://arxiv.org/abs/quant-ph/0209025) treat correction using classical information produced by a measurement on the environment. The monitor here receives a classical event label and has a limited one-way message to the decoder. [Fanizza, Kianvash and Giovannetti](https://doi.org/10.1103/PhysRevLett.125.020503) use nonorthogonal quantum flags in channel extensions to bound quantum capacity.

## Zero-error computation and the graph example

[Meng and Ramamoorthy](https://arxiv.org/abs/2402.01549) derive classical chromatic and quantum orthogonal-representation costs for one-way zero-error computation with classical side information. In the stabilizer setting considered here, the measured syndrome is that side information and the remaining logical Pauli is the function value. Their result supplies the message-size relation for that classical function. Our code construction gives it an operational QEC implementation with an arbitrary reference-entangled input. The exact decoder acts on the recovered payload through the selected logical Pauli correction.

[Mančinska and Roberson](https://arxiv.org/abs/1801.03542) supply the Yu–Oh orthogonality example with a universal vertex. It has ordinary chromatic number five and orthogonal rank four. The lower bound of four follows from the clique consisting of the three coordinate-axis rays and the universal vertex. The [known fractional chromatic number](https://doi.org/10.1515/spma-2025-0060) is $`46/11`$. The finite verification includes rational certificates for it. Ordinary orthogonal rank and entanglement-assisted quantum chromatic number describe different communication resources. The flags used here require only an unassisted four-dimensional channel.

## Nearby recovery interfaces

- [Quantum Erasure Recovery Compiler](https://github.com/GoGoKo699/Quantum-Erasure-Recovery-Compiler) receives the erasure mask and minimizes the number or cost of recovery gates. Here the monitor message is charged and hides the realized mask from the data interface.
- [Correlated Erasure Capacity](https://github.com/GoGoKo699/Correlated-Erasure-Capacity) studies rates with complete location flags and optimized channel codes. The rate in this project measures monitor communication for independent uses of a fixed data encoder.
- [Quantum Delayed Syndrome Decoder](https://github.com/GoGoKo699/Quantum-Delayed-Syndrome-Decoder) starts with supplied nonorthogonal error records and a delay before the syndrome becomes available. Its streaming interface asks how much coherent memory to retain. Here a monitor chooses a flag for the whole event, and the decoder must recover the unknown logical qubit exactly.
