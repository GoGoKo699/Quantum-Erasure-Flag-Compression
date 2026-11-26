# Learn the project

An event monitor knows which carriers in an encoded block were replaced. The decoder receives the damaged block and a short message from the monitor. The task is to restore the encoded qubit, including any entanglement it had with a reference. Start with one syndrome to see how a quantum flag can tell the decoder which correction to apply.

- [Worked example](WORKED_EXAMPLE.md) follows a phase error in one two-qubit pair, then changes the syndrome to show how the flag measurement changes.
- [Watrous bridge](WATROUS_BRIDGE.md) connects the project's channel, measurement and fidelity conventions to John Watrous's *The Theory of Quantum Information* (Cambridge University Press, 2018).
- [30-milestone map](MILESTONES.md) follows the scientific arguments from physical replacement to the exact flag costs, repeated uses and the role of the encoder.
- [Science](../science/README.md) gives the claims and proofs. [Verification](../verification/README.md) reproduces the finite certificates.
