"""
Property-based verification of merge_sort using hypothesis.
Practical work #33 — Formal verification methods.

Verification model:
  Algorithm:         merge_sort(lst: list) -> list
  Input constraints:
    - lst is a list of integers
    - length: 0 <= len(lst) <= 200
    - element range: -10^6 <= element <= 10^6
  Expected properties:
    P1: Output length equals input length
    P2: Output is sorted in non-descending order
    P3: Output is a permutation of the input (same elements, same counts)
    P4: Sorting an already-sorted list is idempotent (result == input)
    P5: Concatenation commutativity — sort(a + b) == sort(b + a)
  Forbidden states:
    - result length differs from input length (elements lost or duplicated)
    - any pair result[i] > result[i+1] (ordering violated)
"""

import pytest
from hypothesis import given, settings, HealthCheck
import hypothesis.strategies as st
from collections import Counter

from merge_sort import merge_sort

# ── shared strategy ──────────────────────────────────────────────────────────
int_list = st.lists(
    st.integers(min_value=-10**6, max_value=10**6),
    min_size=0,
    max_size=200,
)


# ── P1: length preservation ──────────────────────────────────────────────────
@given(lst=int_list)
@settings(max_examples=300, suppress_health_check=[HealthCheck.too_slow])
def test_p1_length_preserved(lst):
    """P1: len(result) == len(input)"""
    result = merge_sort(lst)
    assert len(result) == len(lst), (
        f"Length changed: input {len(lst)}, output {len(result)}"
    )


# ── P2: output is sorted ─────────────────────────────────────────────────────
@given(lst=int_list)
@settings(max_examples=300, suppress_health_check=[HealthCheck.too_slow])
def test_p2_output_is_sorted(lst):
    """P2: for all i: result[i] <= result[i+1]"""
    result = merge_sort(lst)
    for i in range(len(result) - 1):
        assert result[i] <= result[i + 1], (
            f"Order violated at index {i}: {result[i]} > {result[i+1]}"
        )


# ── P3: permutation (multiset equality) ──────────────────────────────────────
@given(lst=int_list)
@settings(max_examples=300, suppress_health_check=[HealthCheck.too_slow])
def test_p3_is_permutation_of_input(lst):
    """P3: Counter(result) == Counter(input)  [same elements, same counts]"""
    result = merge_sort(lst)
    assert Counter(result) == Counter(lst), (
        "Result is not a permutation of the input"
    )


# ── P4: idempotency ──────────────────────────────────────────────────────────
@given(lst=int_list)
@settings(max_examples=300, suppress_health_check=[HealthCheck.too_slow])
def test_p4_idempotent(lst):
    """P4: merge_sort(merge_sort(lst)) == merge_sort(lst)"""
    once = merge_sort(lst)
    twice = merge_sort(once)
    assert twice == once, "Sorting an already-sorted list changed it"


# ── P5: commutativity of concatenation ───────────────────────────────────────
@given(a=int_list, b=int_list)
@settings(max_examples=200, suppress_health_check=[HealthCheck.too_slow])
def test_p5_concatenation_commutative(a, b):
    """P5: sort(a + b) == sort(b + a)"""
    assert merge_sort(a + b) == merge_sort(b + a), (
        "sort(a+b) != sort(b+a) — concatenation order should not matter"
    )
