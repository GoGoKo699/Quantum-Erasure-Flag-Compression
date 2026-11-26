# Project understanding map

The first 12 milestones build the shared framework from a replaced carrier to logical recovery and flag cost. The remaining 18 start with pairs of conflicting events, construct the physical code, and connect decoding to one-shot, repeated-use and finite-noise comparisons. The final milestones place these comparisons in the context of encoder design. [Watrous bridge](WATROUS_BRIDGE.md) · [Worked syndromes](WORKED_EXAMPLE.md)

## Phase I · Background and preliminaries

### M01 Logical data and a reference

**Central question.** What must survive when the decoder restores an unknown logical qubit?

**Understanding target.** Explain why a logical channel equal to the identity also restores correlations with an inaccessible reference. Use one half of a Bell pair to describe the operational test.

**Dependencies.** Start here.

**Conceptual connection.** This gives an input-independent meaning to exact correction and supplies the state used later in the fidelity comparison.

**Sources.** [Watrous §§2.1.2–2.1.3](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf) · [Model and exact graph criterion](../science/model.md)

### M02 Discard and replace

**Central question.** What does a physical replacement do to correlated quantum data?

**Understanding target.** Express replacement on site $`q`$ as a partial trace followed by insertion of $`I_q/2`$. Explain the equivalent uniform average over local Pauli operations and the meaning of a known subset $`S_v`$.

**Dependencies.** [M01](#m01-logical-data-and-a-reference).

**Conceptual connection.** The monitor knows the subset label. The decoder receives the replacement carriers in their original positions and can measure the data.

**Sources.** [Watrous §§2.2.1–2.2.3](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf) · [Model and exact graph criterion](../science/model.md)

### M03 Pauli strings and commutation

**Central question.** How can two physical error strings differ at the logical level?

**Understanding target.** Track the $`X`$ and $`Z`$ components of a Pauli string using binary supports. Explain how a single anticommutation contributes a minus sign and how signs multiply across tensor factors.

**Dependencies.** [M02](#m02-discard-and-replace).

**Conceptual connection.** These rules convert the action of replacement branches into parity checks that can be computed exactly.

**Sources.** [Watrous §1.1.2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.1.pdf) · [Nine-pair construction and decoder](../science/construction.md)

### M04 Code space and logical operators

**Central question.** How do stabilizer constraints leave room for a logical qubit?

**Understanding target.** Identify the code space as the common positive eigenspace of independent commuting checks. Distinguish stabilizers, anticommuting operators, and commuting operators that act nontrivially on the code.

**Dependencies.** [M01](#m01-logical-data-and-a-reference), [M03](#m03-pauli-strings-and-commutation).

**Conceptual connection.** The same physical Pauli pattern can be a stabilizer for one encoding and a logical error for another.

**Sources.** [Nine-pair construction and decoder](../science/construction.md)

### M05 Syndrome and residual correction

**Central question.** Why can identical check outcomes require different recoveries?

**Understanding target.** Compare errors with the same commutation signs against all stabilizer checks. Explain why their product commutes with the checks, and classify their residual action relative to a tentative correction.

**Dependencies.** [M03](#m03-pauli-strings-and-commutation), [M04](#m04-code-space-and-logical-operators).

**Conceptual connection.** Measuring the syndrome supplies receiver-side information and leaves only the remaining logical ambiguity for the flag to resolve.

**Sources.** [Watrous §§2.3.1–2.3.2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf) · [Worked syndromes](WORKED_EXAMPLE.md) · [Nine-pair construction and decoder](../science/construction.md)

### M06 The exact recovery test

**Central question.** What do pairwise error overlaps say about correctability?

**Understanding target.** Interpret the Knill–Laflamme condition $`PE^\dagger FP=\lambda P`$ as the independence of the error-image overlap from the logical input. Understand why checking a Kraus span is sufficient and what an unequal logical action looks like.

**Dependencies.** [M02](#m02-discard-and-replace), [M04](#m04-code-space-and-logical-operators), [M05](#m05-syndrome-and-residual-correction).

**Conceptual connection.** Cross terms between different replacement events determine whether the same recovery can handle both.

**Sources.** [Watrous §2.2.2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf) · [Model and exact graph criterion](../science/model.md)

### M07 Event knowledge and error knowledge

**Central question.** What does the monitor learn about each use?

**Understanding target.** Distinguish the event label $`v`$ and the complete operator basis of errors supported on $`S_v`$. Explain why a simulator may enumerate Pauli branches while the monitor's message still depends only on $`v`$.

**Dependencies.** [M02](#m02-discard-and-replace), [M06](#m06-the-exact-recovery-test).

**Conceptual connection.** The exact problem needs a flag suitable for every branch in the known event, with probabilities entering the separate finite-fidelity comparison.

**Sources.** [Model and exact graph criterion](../science/model.md) · [Finite fidelity and noise](../science/robustness.md)

### M08 Exact state discrimination

**Central question.** When can a measurement distinguish two possible corrections with certainty?

**Understanding target.** Show how a projection identifies which of two orthogonal subspaces contains a flag. Extend the argument to mixed states by taking the support of each state and to correction classes by spanning their flags.

**Dependencies.** [M01](#m01-logical-data-and-a-reference), [M05](#m05-syndrome-and-residual-correction).

**Conceptual connection.** The decoder's syndrome narrows the relevant alternatives and can change which projections it uses.

**Sources.** [Watrous §§2.3.1–2.3.2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf) · [Watrous §§3.1.1–3.1.2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.3.pdf) · [Worked syndromes](WORKED_EXAMPLE.md)

### M09 Colorings and orthogonal representations

**Central question.** How do graphs express selective distinguishability?

**Understanding target.** Define a clique, an independent set, a proper coloring and an orthogonal representation. Explain the dimension lower bound supplied by a clique.

**Dependencies.** [M08](#m08-exact-state-discrimination).

**Conceptual connection.** These graph quantities express the smallest classical alphabet and the smallest quantum flag space.

**Sources.** [Model and exact graph criterion](../science/model.md) · [One-shot and repeated-use costs](../science/rates.md)

### M10 One-shot dimensions and coding rates

**Central question.** What is counted when flags are sent together over many uses?

**Understanding target.** Translate an alphabet of size $`m`$ into $`\lceil\log_2 m\rceil`$ fixed-length bits. Explain how normalizing the logarithm of dimension by the number of uses defines a rate, and why no fractional physical carrier is implied.

**Dependencies.** [M09](#m09-colorings-and-orthogonal-representations).

**Conceptual connection.** This prepares the distinction between the one-shot integer budget and the regularized rate.

**Sources.** [One-shot and repeated-use costs](../science/rates.md)

### M11 Finite error and entanglement fidelity

**Central question.** What can be measured when recovery is imperfect?

**Understanding target.** Define entanglement fidelity as the overlap with the ideal output Bell state for a logical qubit. Explain the square in the project convention and why branch fidelity averages linearly.

**Dependencies.** [M01](#m01-logical-data-and-a-reference), [M05](#m05-syndrome-and-residual-correction).

**Conceptual connection.** Logical Pauli alternatives map the reference test state into orthogonal Bell states, allowing a lower bound on lost fidelity.

**Sources.** [Watrous §3.2.3](https://cs.uwaterloo.ca/~watrous/TQI/TQI.3.pdf) · [Finite fidelity and noise](../science/robustness.md)

### M12 The complete operational problem

**Central question.** Which resources and promises define the comparison?

**Understanding target.** Specify a supplied encoder, a positive-probability event family, a monitor that observes $`v`$, a one-way unassisted message, and a receiver that applies a trace-preserving recovery to the damaged block and flag. Identify what changes when encoder design or flag noise is allowed.

**Dependencies.** [M06](#m06-the-exact-recovery-test), [M07](#m07-event-knowledge-and-error-knowledge), [M08](#m08-exact-state-discrimination), [M09](#m09-colorings-and-orthogonal-representations), [M10](#m10-one-shot-dimensions-and-coding-rates), [M11](#m11-finite-error-and-entanglement-fidelity).

**Conceptual connection.** These assumptions connect operator correction, graph costs and the distinct finite-noise comparison.

**Sources.** [Watrous §4.1.1](https://cs.uwaterloo.ca/~watrous/TQI/TQI.4.pdf) · [Model and exact graph criterion](../science/model.md) · [One-shot and repeated-use costs](../science/rates.md) · [Finite fidelity and noise](../science/robustness.md)

## Phase II · Narrative and innovation

### M13 Conflicting events

**Central question.** Which pairs of events cannot share a recovery without additional information?

**Understanding target.** Construct the event graph by connecting labels $`v,w`$ when some cross error product has a nonscalar restriction to the code. Explain why every individual event must first be correctable.

**Dependencies.** [M06](#m06-the-exact-recovery-test), [M07](#m07-event-knowledge-and-error-knowledge), [M12](#m12-the-complete-operational-problem).

**Conceptual connection.** The graph isolates the cross-event information the flag must preserve.

**Sources.** [Model and exact graph criterion](../science/model.md)

### M14 The classical alphabet

**Central question.** Why does the classical flag cost equal a chromatic number?

**Understanding target.** Show how a collision within a conflicting pair prevents exact correction. Use the independent sets of a proper coloring as jointly recoverable classes, and explain why choosing one possible symbol for each event covers the case of randomized encoders.

**Dependencies.** [M09](#m09-colorings-and-orthogonal-representations), [M13](#m13-conflicting-events).

**Conceptual connection.** The graph gives a decoder-achievable budget and a converse that allows arbitrary classical messages of that size.

**Sources.** [Model and exact graph criterion](../science/model.md)

### M15 The quantum flag space

**Central question.** How can a flag be nonorthogonal to some other flags and still be exact?

**Understanding target.** Compute the cross term for a flagged channel and use the overlap factor $`\langle f_v\mid f_w\rangle`$. Explain why mixed flags require orthogonal supports on edges and why one pure vector per support suffices for the dimension optimum.

**Dependencies.** [M06](#m06-the-exact-recovery-test), [M08](#m08-exact-state-discrimination), [M13](#m13-conflicting-events), [M14](#m14-the-classical-alphabet).

**Conceptual connection.** This derives the quantum dimension from orthogonal rank and permits a syndrome-specific measurement.

**Sources.** [Model and exact graph criterion](../science/model.md)

### M16 Four-dimensional flags

**Central question.** How are the fourteen candidate flag states built?

**Understanding target.** Locate the thirteen rays in a three-dimensional subspace and the apex perpendicular to it. Identify the four orthogonal axis-and-apex rays and use them to certify the lower bound of four dimensions.

**Dependencies.** [M09](#m09-colorings-and-orthogonal-representations), [M15](#m15-the-quantum-flag-space).

**Conceptual connection.** The flag vectors define the target graph that the physical erasure design must realize.

**Sources.** [Nine-pair construction and decoder](../science/construction.md) · [One-shot and repeated-use costs](../science/rates.md)

### M17 From bicliques to replacement sites

**Central question.** How can a desired graph determine which physical carriers are reset?

**Understanding target.** Assign a two-site pair to a complete bipartite subgraph. Map each shore to a site, and identify the nine pairs built from the three axis edges and six other bicliques. Explain why every pair of labels leaves some block untouched.

**Dependencies.** [M02](#m02-discard-and-replace), [M13](#m13-conflicting-events), [M16](#m16-four-dimensional-flags).

**Conceptual connection.** A shared two-sided pair realizes a potential ambiguity while an untouched pair fixes the global parity of the error.

**Sources.** [Nine-pair construction and decoder](../science/construction.md) · [Reproduce the checks](../verification/README.md)

### M18 The nine-pair code

**Central question.** How are one logical qubit and seventeen checks arranged on eighteen sites?

**Understanding target.** Use the two Bell states $`\Phi^+`$ and $`\Psi^+`$ as pair codewords. Derive the pair $`XX`$ check and neighboring four-site $`ZZZZ`$ checks. Identify a logical $`Z`$ representative on any pair and one logical $`X`$ representative using one site in every pair.

**Dependencies.** [M03](#m03-pauli-strings-and-commutation), [M04](#m04-code-space-and-logical-operators), [M17](#m17-from-bicliques-to-replacement-sites).

**Conceptual connection.** A single affected side cannot produce the pair's logical phase by itself.

**Sources.** [Nine-pair construction and decoder](../science/construction.md)

### M19 The physical conflict graph

**Central question.** Why do the check operators certify exactly the intended edges?

**Understanding target.** For a cross error product, use commutation with pair checks to fix its $`Z`$ parity and with neighboring checks to relate its $`X`$ parities. Use the untouched pair to eliminate odd common $`X`$ parity. Construct a nonscalar cross term from the opposite sites of an occupied two-sided pair.

**Dependencies.** [M06](#m06-the-exact-recovery-test), [M13](#m13-conflicting-events), [M17](#m17-from-bicliques-to-replacement-sites), [M18](#m18-the-nine-pair-code).

**Conceptual connection.** This proves both directions of the match between the encoded noise and the orthogonality graph.

**Sources.** [Nine-pair construction and decoder](../science/construction.md) · [Reproduce the checks](../verification/README.md)

### M20 A syndrome-dependent decoder

**Central question.** What does the receiver do on a single damaged block?

**Understanding target.** Measure the checks, select a tentative representative, and group all compatible labels according to their residual logical action. Project the flag onto the mutually orthogonal spans for those classes and apply the corresponding correction. Explain why an independent early measurement would reduce a four-dimensional flag to four useful classical symbols.

**Dependencies.** [M05](#m05-syndrome-and-residual-correction), [M08](#m08-exact-state-discrimination), [M15](#m15-the-quantum-flag-space), [M18](#m18-the-nine-pair-code), [M19](#m19-the-physical-conflict-graph).

**Conceptual connection.** Following the two worked syndromes shows how the same register supports a coordinate measurement and a rotated subspace measurement.

**Sources.** [Worked syndromes](WORKED_EXAMPLE.md) · [Syndrome-conditioned decoder](../science/construction.md#syndrome-conditioned-decoder) · [Early measurement argument](../science/construction.md#reading-the-flag-after-the-syndrome)

### M21 Exact one-shot costs

**Central question.** Why do five classical symbols and a four-dimensional flag suffice, and why are both optimal?

**Understanding target.** Combine the four-clique and explicit flag vectors for the quantum dimension. Use the verified coloring certificate and the obstruction to four classical colors to count three fixed-length bits.

**Dependencies.** [M09](#m09-colorings-and-orthogonal-representations), [M10](#m10-one-shot-dimensions-and-coding-rates), [M14](#m14-the-classical-alphabet), [M15](#m15-the-quantum-flag-space), [M16](#m16-four-dimensional-flags), [M19](#m19-the-physical-conflict-graph), [M20](#m20-a-syndrome-dependent-decoder).

**Conceptual connection.** The counts now apply to exact correction of the same physical channel with the supplied code and a fixed-length flag.

**Sources.** [One-shot and repeated-use costs](../science/rates.md) · [Reproduce the checks](../verification/README.md)

### M22 Product replacement events

**Central question.** Which pairs of event sequences conflict under independent repetitions?

**Understanding target.** Use the tensor-product code and the availability of identity in each replacement Kraus span. Isolate a conflict in one coordinate by choosing identity in the others, and show why scalar cross terms in every coordinate remain scalar.

**Dependencies.** [M10](#m10-one-shot-dimensions-and-coding-rates), [M13](#m13-conflicting-events), [M19](#m19-the-physical-conflict-graph), [M21](#m21-exact-one-shot-costs).

**Conceptual connection.** The resulting OR product permits joint compression across many uses.

**Sources.** [One-shot and repeated-use costs](../science/rates.md)

### M23 Exact regularized rates

**Central question.** How do the one-shot graph quantities determine rates over many uses?

**Understanding target.** Explain why fractional chromatic number controls fixed-length coloring of OR powers. Use the rational value $`46/11`$ for the classical rate and tensor flags plus enlarged cliques for the quantum rate.

**Dependencies.** [M09](#m09-colorings-and-orthogonal-representations), [M10](#m10-one-shot-dimensions-and-coding-rates), [M21](#m21-exact-one-shot-costs), [M22](#m22-product-replacement-events).

**Conceptual connection.** The separate rates are two qubits and $`\log_2(46/11)`$ bits per event for the repeated supplied encoder.

**Sources.** [One-shot and repeated-use costs](../science/rates.md) · [Reproduce the checks](../verification/README.md)

### M24 A colliding pair forces finite error

**Central question.** What can a four-symbol classical flag achieve if exactness is relaxed?

**Understanding target.** Find an edge whose labels share a symbol. Compare a pair of positive-probability Pauli branches that give the same syndrome and differ logically by $`\overline Z`$. Use the orthogonal Bell tests to see why a decoder cannot achieve unit fidelity on both. Explain how maximizing the probability of the corrected class for each symbol and syndrome gives the exact four-symbol optimum $`7167/7168`$.

**Dependencies.** [M07](#m07-event-knowledge-and-error-knowledge), [M11](#m11-finite-error-and-entanglement-fidelity), [M19](#m19-the-physical-conflict-graph), [M21](#m21-exact-one-shot-costs).

**Conceptual connection.** Aggregating branch weights yields a fixed finite infidelity gap under a uniform event distribution.

**Sources.** [Optimal classical fidelity](../science/robustness.md#optimal-classical-fidelity) · [Worked syndromes](WORKED_EXAMPLE.md)

### M25 Reading a finite robustness guarantee

**Central question.** What survives if the flag preparation or transmission changes slightly?

**Understanding target.** Use the trace distance between actual and ideal conditional flag states to bound the change in the output Bell overlap under the same decoder. Explain why heralded loss permits a separate fallback decoder, and why unheralded depolarization requires a decision on two mixed flag states. Keep the flag budget and uniform-event benchmark visible.

**Dependencies.** [M08](#m08-exact-state-discrimination), [M11](#m11-finite-error-and-entanglement-fidelity), [M20](#m20-a-syndrome-dependent-decoder), [M24](#m24-a-colliding-pair-forces-finite-error).

**Conceptual connection.** The estimate turns a finite classical collision penalty into a robustness guarantee for a specified quantum decoder.

**Sources.** [Watrous §§3.1.1, 3.3](https://cs.uwaterloo.ca/~watrous/TQI/TQI.3.pdf) · [Heralded loss](../science/robustness.md#heralded-loss-of-the-whole-flag) · [Unheralded depolarization](../science/robustness.md#unheralded-depolarization-of-the-ray-flags)

### M26 Why every encoder needs some flag

**Central question.** Can another encoder remove the monitor message entirely?

**Understanding target.** Group the four axis-and-apex supports into two pairs. Explain why exact recovery with no flag would imply correctability of each paired union, whose surviving complements are disjoint. Use the resulting two perfect decoders to reach the no-cloning contradiction.

**Dependencies.** [M01](#m01-logical-data-and-a-reference), [M02](#m02-discard-and-replace), [M06](#m06-the-exact-recovery-test), [M17](#m17-from-bicliques-to-replacement-sites), [M19](#m19-the-physical-conflict-graph).

**Conceptual connection.** This argument supplies a code-independent lower bound across the same physical replacement events.

**Sources.** [Watrous §7.2.2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.7.pdf) · [Nine-pair construction and decoder](../science/construction.md)

### M27 A redesigned encoder with a one-bit flag

**Central question.** How can the same physical channel have a different optimal flag budget?

**Understanding target.** Use the alternative CSS code on carriers 2 through 6 and identify the active replacement sets. Test the two classes defined by whether the label is 8. Verify that no same-class union contains a support of a logical Pauli, so the one-bit flag suffices.

**Dependencies.** [M03](#m03-pauli-strings-and-commutation), [M04](#m04-code-space-and-logical-operators), [M06](#m06-the-exact-recovery-test), [M14](#m14-the-classical-alphabet), [M21](#m21-exact-one-shot-costs), [M26](#m26-why-every-encoder-needs-some-flag).

**Conceptual connection.** Together with the no-flag obstruction, the witness fixes the minimum when arbitrary re-encoding is allowed.

**Sources.** [Encoder choice](../science/construction.md#encoder-choice) · [Reproduce the checks](../verification/README.md)

### M28 What check locality constrains

**Central question.** Which design choices must be held fixed in a hardware comparison?

**Understanding target.** Compare the active sites, check weights and chain spans of the two encoders. Both meet the same upper bounds of four on weight and span. Explain why fixing those upper bounds still allows the second encoding to concentrate the logical state into five active sites.

**Dependencies.** [M17](#m17-from-bicliques-to-replacement-sites), [M18](#m18-the-nine-pair-code), [M21](#m21-exact-one-shot-costs), [M27](#m27-a-redesigned-encoder-with-a-one-bit-flag).

**Conceptual connection.** A meaningful code-design comparison states the locality, weight, and active-site constraints alongside flag cost.

**Sources.** [Code checks](../science/construction.md#code-and-conflict-graph) · [Encoder choice](../science/construction.md#encoder-choice)

### M29 Foundations, construction and verification

**Central question.** Which ingredients are inherited, and what has the project added?

**Understanding target.** Trace the roles of the exact recovery criterion, zero-error function coding with side information, and the ray graph. Identify the physical code construction, reference-preserving decoder and no-flag obstruction, and explain which claims the finite checks check directly.

**Dependencies.** [M13](#m13-conflicting-events), [M15](#m15-the-quantum-flag-space), [M19](#m19-the-physical-conflict-graph), [M20](#m20-a-syndrome-dependent-decoder), [M23](#m23-exact-regularized-rates), [M25](#m25-reading-a-finite-robustness-guarantee), [M26](#m26-why-every-encoder-needs-some-flag), [M27](#m27-a-redesigned-encoder-with-a-one-bit-flag).

**Conceptual connection.** This makes the mathematical dependencies and what can be reproduced in a small computation explicit.

**Sources.** [Related work](../science/related-work.md) · [Nine-pair construction and decoder](../science/construction.md) · [One-shot and repeated-use costs](../science/rates.md) · [Reproduce the checks](../verification/README.md)

### M30 The complete scientific story

**Central question.** When does a quantum flag need fewer dimensions than a classical alphabet?

**Understanding target.** Reconstruct the route from replacement events through cross terms, graph realization, syndrome-dependent decoding and exact rates. State the one-shot counts, the scope of the finite-noise comparison and how the answer changes with encoder redesign.

**Dependencies.** [M12](#m12-the-complete-operational-problem), [M21](#m21-exact-one-shot-costs), [M23](#m23-exact-regularized-rates), [M25](#m25-reading-a-finite-robustness-guarantee), [M26](#m26-why-every-encoder-needs-some-flag), [M27](#m27-a-redesigned-encoder-with-a-one-bit-flag), [M28](#m28-what-check-locality-constrains), [M29](#m29-foundations-construction-and-verification).

**Conceptual connection.** One operational account now links physical noise, the decoder's local information and the cost of the monitor's message.

**Sources.** [Model and exact graph criterion](../science/model.md) · [Nine-pair construction and decoder](../science/construction.md) · [One-shot and repeated-use costs](../science/rates.md) · [Finite fidelity and noise](../science/robustness.md)
