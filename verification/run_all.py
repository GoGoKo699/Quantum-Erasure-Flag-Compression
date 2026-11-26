#!/usr/bin/env python3
"""Verify the finite erasure flag examples using exact arithmetic."""

from collections import Counter, defaultdict
from fractions import Fraction
from functools import cache
from itertools import combinations, combinations_with_replacement, product


RAYS = (
    (0, 0, 1, 0), (0, 1, -1, 0), (0, 1, 0, 0), (0, 1, 1, 0),
    (1, -1, -1, 0), (1, -1, 0, 0), (1, -1, 1, 0), (1, 0, -1, 0),
    (1, 0, 0, 0), (1, 0, 1, 0), (1, 1, -1, 0), (1, 1, 0, 0),
    (1, 1, 1, 0), (0, 0, 0, 1),
)
VERTICES = tuple(range(len(RAYS)))
APEX = 13
AXES = (0, 2, 8)
ANCHORS = (*AXES, APEX)

FRACTIONAL_DUAL = (3, 3, 3, 3, 2, 3, 2, 3, 3, 3, 2, 3, 2, 11)
FRACTIONAL_PRIMAL = (
    ((13,), 11), ((0, 1, 7, 10), 5), ((0, 3, 4, 7), 5),
    ((1, 2, 5, 6), 4), ((1, 2, 10, 11), 2), ((2, 3, 4, 5), 3),
    ((2, 3, 11, 12), 1), ((3, 9, 11, 12), 2), ((5, 6, 8, 9), 4),
    ((7, 8, 10, 11), 1), ((8, 9, 11, 12), 5), ((0, 4, 6, 10, 12), 1),
    ((2, 4, 6, 10, 12), 1), ((4, 6, 8, 10, 12), 1),
)

# Alternative CSS code: four generator strings on five consecutive active sites.
ACTIVE_SITES = (2, 3, 4, 5, 6)
ACTIVE_GENERATORS = ("XIXXI", "IXXXX", "ZZZII", "IZZZZ")


def dot(left, right):
    return sum(a * b for a, b in zip(left, right))


def orthogonal(first, second):
    return dot(RAYS[first], RAYS[second]) == 0


def geometry():
    edges = {pair for pair in combinations(VERTICES, 2) if orthogonal(*pair)}
    blocks = [((first,), (second,)) for first, second in combinations(AXES, 2)]
    for ray in VERTICES[:-1]:
        if sum(coordinate != 0 for coordinate in RAYS[ray]) == 2:
            shore = tuple(other for other in VERTICES[:-1] if orthogonal(ray, other))
            blocks.append(((ray, APEX), shore))

    covered_edges = set()
    supports = [0] * len(VERTICES)
    for index, (left, right) in enumerate(blocks):
        assert not set(left) & set(right)
        assert set(left) & set(ANCHORS) and set(right) & set(ANCHORS)
        covered_edges.update(tuple(sorted(pair)) for pair in product(left, right))
        for side, shore in enumerate((left, right)):
            for event in shore:
                supports[event] |= 1 << (2 * index + side)

    assert len(edges) == 37 and edges == covered_edges
    assert len(blocks) == 9
    assert [s.bit_count() for s in supports] == [4, 2, 4, 2, 3, 2, 3, 2, 4, 2, 3, 2, 3, 6]
    for first, second in combinations_with_replacement(VERTICES, 2):
        support = supports[first] | supports[second]
        assert any(support & (3 << (2 * block)) == 0 for block in range(len(blocks)))
    partition_a = supports[0] | supports[2]
    partition_b = supports[8] | supports[13]
    assert partition_a | partition_b == (1 << (2 * len(blocks))) - 1
    return edges, supports, len(blocks)


def check_coloring(edges):
    assert all(edge in edges for edge in combinations(ANCHORS, 2))
    color_classes = ((0, 1, 7, 10), (2, 3, 4, 5), (6, 8, 9, 12), (11,), (13,))
    assert sorted(v for group in color_classes for v in group) == list(VERTICES)
    assert all(
        pair not in edges
        for group in color_classes
        for pair in combinations(group, 2)
    )

    coverage = [0] * len(VERTICES)
    for vertices, weight in FRACTIONAL_PRIMAL:
        assert all(edge not in edges for edge in combinations(vertices, 2))
        for vertex in vertices:
            coverage[vertex] += weight
    assert min(coverage) >= 11
    assert sum(weight for _, weight in FRACTIONAL_PRIMAL) == sum(FRACTIONAL_DUAL) == 46
    for size in range(1, len(VERTICES) + 1):
        for vertices in combinations(VERTICES, size):
            if all(edge not in edges for edge in combinations(vertices, 2)):
                assert sum(FRACTIONAL_DUAL[v] for v in vertices) <= 11
    fractional = Fraction(sum(FRACTIONAL_DUAL), 11)
    assert 4 < fractional <= 5
    return fractional


def rank_gf2(rows):
    pivots = {}
    for row in rows:
        while row:
            column = row.bit_length()
            if column not in pivots:
                pivots[column] = row
                break
            row ^= pivots[column]
    return len(pivots)


def check_alternate_code(supports, qubits):
    def pauli_row(paulis):
        x = sum(1 << site for site, pauli in zip(ACTIVE_SITES, paulis) if pauli in "XY")
        z = sum(1 << site for site, pauli in zip(ACTIVE_SITES, paulis) if pauli in "ZY")
        return x, z

    generators = [pauli_row(paulis) for paulis in ACTIVE_GENERATORS]
    for paulis in ACTIVE_GENERATORS:
        occupied = [site for site, pauli in zip(ACTIVE_SITES, paulis) if pauli != "I"]
        assert len(occupied) <= 4 and occupied[-1] - occupied[0] + 1 <= 4
    spectators = [(0, 1 << site) for site in range(qubits) if site not in ACTIVE_SITES]
    rows = generators + spectators + [pauli_row("IIZZI"), pauli_row("IXXII")]
    assert len(rows) == qubits + 1
    assert all(0 <= mask < 1 << qubits for row in rows for mask in row)
    parity_rows = [z | (x << qubits) for x, z in rows]
    assert rank_gf2(parity_rows) == len(rows)
    for first, second in combinations(range(len(rows)), 2):
        x, z = rows[first]
        other_x, other_z = rows[second]
        parity = ((x & other_z).bit_count() + (z & other_x).bit_count()) % 2
        assert parity == int((first, second) == (qubits - 1, qubits))

    def correctable(support):
        mask = support | (support << qubits)
        restricted = [row & mask for row in parity_rows]
        return rank_gf2(restricted[:-2]) == rank_gf2(restricted)

    assert all(correctable(support) for support in supports)
    edges = {
        (a, b) for a, b in combinations(VERTICES, 2)
        if not correctable(supports[a] | supports[b])
    }
    assert edges == {(0, 8), (1, 8), (2, 8), (8, 13)}
    assert all(8 in edge for edge in edges)
    return edges


def pauli_branches(support, blocks):
    sites = [site for site in range(2 * blocks) if support & (1 << site)]
    for paulis in product(range(4), repeat=len(sites)):
        x_parity = z_parity = right_z_parity = 0
        for site, pauli in zip(sites, paulis):
            block, side = divmod(site, 2)
            if pauli & 1:
                x_parity ^= 1 << block
            if pauli & 2:
                z_parity ^= 1 << block
                right_z_parity ^= side
        adjacent_x = (x_parity ^ (x_parity >> 1)) & ((1 << (blocks - 1)) - 1)
        yield (adjacent_x, z_parity), (x_parity & 1, right_z_parity)


def check_syndromes(supports, blocks, edges):
    """Build exact integer probability tables for uniform events and resets."""
    maximum_support = max(support.bit_count() for support in supports)
    denominator = len(supports) * 4**maximum_support
    table = defaultdict(dict)
    for event, support in enumerate(supports):
        weight = 4 ** (maximum_support - support.bit_count())
        multiplicities = Counter(pauli_branches(support, blocks))
        for (syndrome, logical), multiplicity in multiplicities.items():
            assert event not in table[syndrome]
            table[syndrome][event] = (logical, weight * multiplicity)

    reconstructed = set()
    for compatible in table.values():
        assert len({logical[0] for logical, _ in compatible.values()}) == 1
        for first, second in combinations(sorted(compatible), 2):
            if compatible[first][0] != compatible[second][0]:
                reconstructed.add((first, second))
    assert reconstructed == edges
    assert sum(weight for group in table.values() for _, weight in group.values()) == denominator
    return table, denominator


def split_logical_classes(compatible):
    return tuple(
        tuple(sorted((event, weight) for event, (logical, weight) in compatible.items()
                     if logical[1] == label))
        for label in range(2)
    )


def optimal_classical_errors(table, denominator, alphabet_sizes):
    """Minimize exact syndrome-averaged failure over all label partitions."""
    group_errors = [0] * (1 << len(VERTICES))

    # An observed syndrome needs at most a binary logical-Z decision. Compress
    # identical distributions before calculating the loss for each message.
    ambiguous = Counter()
    for compatible in table.values():
        left, right = split_logical_classes(compatible)
        if left and right:
            ambiguous[tuple(sorted((left, right)))] += 1

    for group in range(1, len(group_errors)):
        for (left, right), multiplicity in ambiguous.items():
            mass_left = sum(weight for event, weight in left if (group >> event) & 1)
            mass_right = sum(weight for event, weight in right if (group >> event) & 1)
            group_errors[group] += multiplicity * min(mass_left, mass_right)

    chosen_group = {}

    @cache
    def optimum(events, remaining_labels):
        if remaining_labels == 1 or group_errors[events] == 0:
            chosen_group[events, remaining_labels] = events
            return group_errors[events]

        anchor = events & -events
        others = events ^ anchor
        best = group_errors[events]
        group_choice = events
        subset = others
        while subset:
            subset = (subset - 1) & others
            group = subset | anchor
            candidate = group_errors[group]
            if candidate < best:
                candidate += optimum(events ^ group, remaining_labels - 1)
                if candidate < best:
                    best, group_choice = candidate, group
                    if best == 0:
                        break
        chosen_group[events, remaining_labels] = group_choice
        return best

    for labels in alphabet_sizes:
        events = len(group_errors) - 1
        error_mass = optimum(events, labels)
        partition = []
        while events:
            group = chosen_group[events, labels]
            partition.append(tuple(event for event in VERTICES if (group >> event) & 1))
            events ^= group
            labels -= 1
        yield Fraction(error_mass, denominator), partition


def rank_rational(rows):
    pivots = {}
    for row in rows:
        reduced = [Fraction(value) for value in row]
        for column, value in enumerate(reduced):
            if not value:
                continue
            if column in pivots:
                reduced = [a - value * b for a, b in zip(reduced, pivots[column])]
            else:
                pivots[column] = [entry / value for entry in reduced]
                break
    return len(pivots)


def minority_branches(table):
    for compatible in table.values():
        left, right = split_logical_classes(compatible)
        mass_left, mass_right = sum(w for _, w in left), sum(w for _, w in right)
        if mass_left <= mass_right:
            yield left, mass_left, mass_right
        else:
            yield right, mass_right, mass_left


def maximally_mixed_flag_error(table, denominator):
    """Error of the ideal-correcting receiver when the flag is replaced by I/4."""
    quarter_weight = 0
    for left, mass_left, mass_right in minority_branches(table):
        # Measure the minority support versus its orthogonal complement. The
        # completely mixed flag lands in the minority support with rank / 4.
        rank = rank_rational(RAYS[event] for event, _ in left)
        quarter_weight += 4 * mass_left + (mass_right - mass_left) * rank
    return Fraction(quarter_weight, 4 * denominator)


def positive_definite(matrix):
    """Check strict positivity of every successive Schur-complement pivot."""
    while matrix:
        pivot = matrix[0][0]
        if pivot <= 0:
            return False
        matrix = [
            [entry - row[0] * lead / pivot for entry, lead in zip(row[1:], matrix[0][1:])]
            for row in matrix[1:]
        ]
    return True


def check_depolarization_threshold(table, threshold):
    """Verify the Helstrom minority projector up to the fidelity crossing."""
    for left, mass_left, mass_right in minority_branches(table):
        if mass_left == 0:
            continue
        basis = []
        for event, _ in left:
            ray = RAYS[event]
            if rank_rational([*basis, ray]) > len(basis):
                basis.append(ray)

        def minority_operator_entry(first, second):
            weighted_overlap = sum(
                Fraction(weight * dot(first, RAYS[event]) * dot(second, RAYS[event]),
                         dot(RAYS[event], RAYS[event]))
                for event, weight in left
            )
            shift = threshold * (mass_right - mass_left) / 4
            return (1 - threshold) * weighted_overlap - shift * dot(first, second)

        matrix = [[minority_operator_entry(u, v) for v in basis] for u in basis]
        assert positive_definite(matrix)


def main():
    edges, supports, blocks = geometry()
    fractional = check_coloring(edges)
    print(f"Nine-block code, {len(edges)} conflicts, fractional chromatic number {fractional}")
    alternate_edges = check_alternate_code(supports, 2 * blocks)
    print(f"Alternate code conflicts: {sorted(alternate_edges)}")
    table, denominator = check_syndromes(supports, blocks, edges)
    results = list(optimal_classical_errors(table, denominator, range(1, 6)))
    errors = [error for error, _ in results]
    assert errors == [
        Fraction(1643, 14336), Fraction(425, 28672), Fraction(41, 28672),
        Fraction(1, 7168), Fraction(0),
    ]
    for labels, (error, _) in enumerate(results, start=1):
        print(f"{labels} classical symbols: optimal entanglement fidelity {1 - error}")
    print(f"One optimal four-message partition: {results[3][1]}")
    heralded_threshold = errors[3] / errors[0]
    mixed_error = maximally_mixed_flag_error(table, denominator)
    depolarization_threshold = errors[3] / mixed_error
    assert heralded_threshold == Fraction(2, 1643)
    assert mixed_error == Fraction(379, 1792)
    assert depolarization_threshold == Fraction(1, 1516)
    check_depolarization_threshold(table, depolarization_threshold)
    print(f"Heralded flag-erasure threshold: {heralded_threshold}")
    print(f"Maximally mixed flag branch infidelity for the stated decoder: {mixed_error}")
    print(f"Depolarization crossing verified by exact Helstrom check: {depolarization_threshold}")


if __name__ == "__main__":
    main()
