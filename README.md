# Quantum Erasure Flag Compression

How much information must a monitor send to recover an unknown encoded qubit when replacement locations are hidden from the decoder?

We give an explicit 18-qubit CSS code and 14 correlated replacement events. A monitor encodes the event into a two-qubit flag. The decoder measures the stabilizer syndrome, uses it to choose a measurement of the flag, and applies a logical correction. The procedure recovers every input, including states entangled with a reference.

| Result | Scope |
| :--- | :--- |
| **Two flag qubits or five classical symbols** | Exact recovery for the supplied code. Five symbols require three fixed-length bits. |
| **$`7167/7168`$ entanglement fidelity with two classical bits** | Exact optimum for uniform events and simultaneous maximally mixed replacements on the supplied code. |
| **One classical bit after re-encoding** | A five-active-site CSS encoder uses the same channel and the same maximum check weight and chain span. One bit is optimal when the encoder may be changed. |

For independent repetitions with the original encoder on each block, the minimum fixed-length flag rates per event are

```math
R_{\mathrm q}=2\ \text{qubits},\qquad R_{\mathrm c}=\log_2(46/11)\ \text{bits}.
```

The model gives the monitor the event label alone. The decoder receives the replacement qubits without location markers. Communication is one-way, without preshared entanglement. Exact recovery uses perfect syndrome operations and a noiseless flag link. The robustness analysis treats imperfect flags under specified noise models.

## Read the science

- [Model and exact flag costs](science/model.md) defines which pairs of events require distinguishable messages.
- [Code and decoder](science/construction.md) gives the CSS construction, the syndrome-dependent flag measurement and the one-bit re-encoding.
- [Flag rates](science/rates.md) derives the fixed-length rates for independent uses.
- [Finite fidelity and robustness](science/robustness.md) gives the classical optima and compares them with noisy quantum flags.
- [Related work](science/related-work.md) identifies the inherited graph and error-correction results.

## Learn and verify

The educational anchor is John Watrous’s *The Theory of Quantum Information* (2018). The [learning route](learning/README.md) links to the source bridge, worked examples and 30 milestones. The [verification guide](verification/README.md) explains the finite checks.

```bash
python3 verification/run_all.py
```

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
