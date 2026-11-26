# From Watrous to erasure flag compression

How much can a monitor say about an error when the receiver can already measure the stabilizer syndrome? A replacement event specifies the sites that lost their states. The syndrome is measured on the damaged data. Together the report and the syndrome must determine a correction that restores arbitrary logical coherence.

The educational anchor is **John Watrous, *The Theory of Quantum Information***, Cambridge University Press, 2018. The sections below use the author's standard-layout 2018 prepublication manuscript. The Waterloo source page gives the chapter PDFs and errata. [Author's source page](https://cs.uwaterloo.ca/~watrous/TQI/)

## Targeted readings

| Project use | Sections in the author's manuscript | Connection |
|---|---|---|
| Logical quantum data and an untouched reference, M01 | [Sections 2.1.2–2.1.3](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf) | Density operators, partial trace, and purification explain what full recovery must preserve. |
| Replacement events and channel representations, M02 and M06 | [Sections 2.2.1–2.2.3](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf) | Kraus and Stinespring representations describe the same channel. The Kraus span is enough to test exact recovery for a code. |
| Syndrome and flag measurements, M05, M08, M20 | [Sections 2.3.1–2.3.2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf), [Sections 3.1.1–3.1.2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.3.pdf) | Effects give outcome probabilities. Orthogonal support allows a measurement to distinguish alternatives with certainty. |
| Correction with environmental information, M12–M15 | [Section 4.1.1, pp. 205–208](https://cs.uwaterloo.ca/~watrous/TQI/TQI.4.pdf) | A measurement of a Stinespring environment can supply information for channel correction. Here that role is played by a monitor with access to a specified event label. |
| Entanglement fidelity and perturbations, M11, M24–M25 | [Sections 3.2.3 and 3.3](https://cs.uwaterloo.ca/~watrous/TQI/TQI.3.pdf) | Watrous's mapping fidelity supplies the purification-based comparison. The completely bounded trace norm quantifies receiver effects of channel perturbations. |
| Incompatible recoveries after disjoint losses, M26 | [Section 7.2.2, remark following Theorem 7.28](https://cs.uwaterloo.ca/~watrous/TQI/TQI.7.pdf) | Two perfect decoders on disjoint sets would implement perfect copying of an unknown pure state. |

## Translate the notation

| In Watrous | In the project | Meaning |
|---|---|---|
| $`u`$, $`u^*`$, $`uu^*`$ | $`\lvert\psi\rangle`$, $`\langle\psi\rvert`$, $`\lvert\psi\rangle\langle\psi\rvert`$ | A vector, its adjoint, and its pure-state projector. |
| $`A_a`$ in a Kraus sum | $`E_{v,a}`$ | An operator for a channel branch conditional on event $`v`$. |
| $`\mu(a)`$ | A syndrome projector or a flag effect | The positive operator whose expectation gives the corresponding outcome probability. |
| $`\mathrm{Tr}_{\mathcal Z}`$ | $`\mathrm{Tr}_{S_v}`$ when modeling a replacement | Discard the systems at the specified positions before inserting fresh maximally mixed carriers. |
| $`F(\Phi,\rho)`$ in Definition 3.30 | $`F_e(\Phi)`$ at $`\rho=I/2`$ | Here $`F_e`$ is the **square** of Watrous's mapping fidelity. |
| Completely bounded trace norm | $`\lVert\cdot\rVert_\diamond`$ | Distance convention used to compare channels while retaining a reference. |

## From representations to correctability

Let $`V`$ encode a logical qubit and put $`P=VV^\dagger`$. If one physical qubit is replaced by $`I/2`$, averaging equally over its four Pauli operations realizes the same channel. Inside the larger encoded block this acts as
```math
\mathcal D_q(A)=\frac14\sum_{Q\in\{I,X,Y,Z\}}Q_q A Q_q^\dagger
=\frac{I_q}{2}\otimes\mathrm{Tr}_q A,
```
with the tensor factors in their original order. A particular Kraus term is a representation of the data noise. The monitor directly observes the set of replaced positions, so its report can depend on the event label alone. [Project model](../science/model.md)

The Knill–Laflamme criterion tests whether $`PE_{v,a}^\dagger E_{w,b}P`$ is proportional to $`P`$ for every pair of relevant Kraus operators. A scalar cross term says the overlap of the two error images is the same for every logical input, including all superpositions. If the monitor appends a pure flag $`f_v`$, the new cross term is
```math
\langle f_v\mid f_w\rangle\,PE_{v,a}^\dagger E_{w,b}P.
```
Orthogonal flags therefore remove the cross term exactly where it prevents recovery. The project turns the requirement into a graph on event labels, constructs a stabilizer code whose graph has a known separation, and gives an explicit recovery measurement. These steps use the project proofs and primary results alongside Watrous's general channel formalism. [Exact criterion](../science/model.md) · [Construction](../science/construction.md)

## Read the fidelity convention before comparing protocols

For a qubit, prepare a maximally entangled state $`\lvert\Phi^+\rangle`$ of the logical input and an untouched reference. For the net logical channel $`\Lambda`$ the project uses
```math
F_e(\Lambda)=\langle\Phi^+\rvert
(\Lambda\otimes\mathrm{id})(\lvert\Phi^+\rangle\langle\Phi^+\rvert)
\lvert\Phi^+\rangle.
```

Watrous's Definition 3.30 takes the root fidelity of the same outputs at $`\rho=I/2`$. Squaring that quantity gives the displayed overlap. The two conventions agree on perfect recovery. Using the squared convention makes $`F_e`$ affine in the channel, which permits averaging over probabilities of Pauli branches. The four logical Pauli actions on one half of $`\Phi^+`$ generate an orthonormal Bell basis, which supplies the finite-error comparison. [Project fidelity and robustness](../science/robustness.md)

Continue with the two [worked syndromes](WORKED_EXAMPLE.md) or the [30-milestone map](MILESTONES.md).
