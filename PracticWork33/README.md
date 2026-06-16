# Практична робота №33
## Верифікація коду за допомогою формальних методів

**Алгоритм:** Сортування злиттям (Merge Sort)  
**Інструмент:** Python · `hypothesis` 6.155.3 · `pytest` 9.1.0  
**Дата:** 16.06.2026  
**Тестувальник:** Роман Матвійчук

---

## Крок 1. Вибір алгоритму та формальний контракт

### Обґрунтування вибору

Сортування злиттям обрано через наявність чітких математичних властивостей (довжина, порядок, перестановка), рекурсивну структуру (що потребує інваріантів) та практичну значущість — помилки у сортуванні є критичними для будь-якого застосунку.

### Реалізація з анотованим контрактом

```python
def merge_sort(lst: list) -> list:
    """
    Sorts a list of integers in non-descending order using merge sort.

    Preconditions:
    - lst is a list (may be empty)
    - every element of lst is an integer or float

    Postconditions:
    - result has the same length as input:
        len(result) == len(lst)
    - result is sorted in non-descending order:
        for all i in range(len(result) - 1): result[i] <= result[i+1]
    - result is a permutation of lst (same elements, same counts):
        Counter(result) == Counter(lst)

    Invariants (merge step):
    - at every recursive call the sublists being merged are individually sorted
    - the merged output preserves all elements from both halves without loss
      or duplication
    """
    if len(lst) <= 1:
        return list(lst)
    mid = len(lst) // 2
    left  = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])
    return _merge(left, right)


def _merge(left: list, right: list) -> list:
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:   # <= гарантує стабільність і збереження дублів
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result
```

---

## Крок 2. Верифікаційна модель

```
Algorithm: merge_sort(lst: list) -> list

Input constraints:
  - lst — список цілих чисел (тип: list[int])
  - довжина: 0 <= len(lst) <= 200
  - діапазон елементів: -10^6 <= element <= 10^6
  - порожній список є валідним входом

Expected properties:
  P1: Збереження довжини
      len(result) == len(lst)

  P2: Відсортованість виходу
      for all i in range(len(result) - 1): result[i] <= result[i+1]

  P3: Перестановка входу (мультимножинна рівність)
      Counter(result) == Counter(lst)

  P4: Ідемпотентність
      merge_sort(merge_sort(lst)) == merge_sort(lst)

  P5: Комутативність конкатенації
      merge_sort(a + b) == merge_sort(b + a)

Forbidden states:
  - len(result) != len(lst)          [втрата або дублювання елементів]
  - result[i] > result[i+1] для будь-якого i  [порушення порядку]
  - Counter(result) != Counter(lst)  [зміна мультимножини елементів]
```

---

## Крок 3. Property-based тести з hypothesis

### Файл `test_merge_sort.py`

```python
"""
Property-based verification of merge_sort using hypothesis.

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
    once  = merge_sort(lst)
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
```

### Результат запуску (коректна реалізація)

```
============================= test session starts ==============================
platform linux -- Python 3.12.3, pytest-9.1.0, pluggy-1.6.0
hypothesis profile 'default'
collected 5 items

test_merge_sort.py::test_p1_length_preserved           PASSED   [ 20%]
test_merge_sort.py::test_p2_output_is_sorted           PASSED   [ 40%]
test_merge_sort.py::test_p3_is_permutation_of_input    PASSED   [ 60%]
test_merge_sort.py::test_p4_idempotent                 PASSED   [ 80%]
test_merge_sort.py::test_p5_concatenation_commutative  PASSED   [100%]

============================== 5 passed in 1.75s ===============================
```

---

### Демонстрація виявлення дефекту

Для ілюстрації можливостей hypothesis було навмисно введено дефект у функцію `_merge`:

**Дефектна реалізація (`_merge_buggy`):**

```python
def _merge_buggy(left: list, right: list) -> list:
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        elif left[i] > right[j]:
            result.append(right[j])
            j += 1
        else:
            # БАГ: при рівності лівий елемент відкидається
            result.append(right[j])
            i += 1   # left[i] пропущено — втрата дубліката
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result
```

**Результат запуску тестів проти дефектної реалізації:**

```
collected 3 items

test_merge_sort_buggy2.py::test_p1_length_preserved        FAILED   [ 33%]
test_merge_sort_buggy2.py::test_p2_output_is_sorted        PASSED   [ 66%]
test_merge_sort_buggy2.py::test_p3_is_permutation_of_input FAILED   [100%]

FAILURES
────────────────────────────────────────────────────────
test_p1_length_preserved:
  lst = [0, 0]
  assert 1 == 2
  Falsifying example: test_p1_length_preserved(lst=[0, 0])

test_p3_is_permutation_of_input:
  lst = [0, 0]
  AssertionError: assert Counter({0: 1}) == Counter({0: 2})
  Falsifying example: test_p3_is_permutation_of_input(lst=[0, 0])
```

Hypothesis автоматично мінімізував контрприклад до `[0, 0]` — найпростішого списку з двох рівних елементів.

---

## Крок 4. Верифікаційний звіт

```
Verification Report
===================
Algorithm:  merge_sort(lst: list) -> list
Tool:       hypothesis 6.155.3 (property-based testing)
            pytest 9.1.0
            Python 3.12.3 · Linux x86-64
Date:       16.06.2026
Tester:     Студент групи ___

Formal contract:
  Preconditions:
    - lst є списком (допустимий порожній)
    - кожен елемент lst є цілим числом або числом з рухомою крапкою

  Postconditions:
    - len(result) == len(lst)
    - ∀ i ∈ [0, len(result)-2]: result[i] <= result[i+1]
    - Counter(result) == Counter(lst)

  Invariants (крок злиття):
    - підсписки, що зливаються, є індивідуально відсортованими
    - злитий результат зберігає всі елементи обох половин без втрат

Verification model:
  Input constraints:
    - lst: list[int], len ∈ [0, 200], values ∈ [-10^6, 10^6]
  Expected properties: P1, P2, P3, P4, P5

Results (коректна реалізація):
┌──────┬────────────────────────────────────┬────────┬──────────────────────────────────────┐
│ Prop │ Test name                          │ Status │ Notes                                │
├──────┼────────────────────────────────────┼────────┼──────────────────────────────────────┤
│  P1  │ test_p1_length_preserved           │  PASS  │ 300 прикладів, контрприкладу не знайдено │
│  P2  │ test_p2_output_is_sorted           │  PASS  │ 300 прикладів, контрприкладу не знайдено │
│  P3  │ test_p3_is_permutation_of_input    │  PASS  │ 300 прикладів, контрприкладу не знайдено │
│  P4  │ test_p4_idempotent                 │  PASS  │ 300 прикладів, контрприкладу не знайдено │
│  P5  │ test_p5_concatenation_commutative  │  PASS  │ 200 пар списків, контрприкладу не знайдено │
└──────┴────────────────────────────────────┴────────┴──────────────────────────────────────┘

Defects (виявлено під час верифікації дефектної реалізації):

  D-01 [FAIL, P1 + P3, дефектна реалізація]:
    Input:    lst = [0, 0]
    Expected: result = [0, 0]  (Counter({0: 2}), len = 2)
    Actual:   result = [0]     (Counter({0: 1}), len = 1)
    Root cause: дефект реалізації — у _merge при рівності лівий елемент
                відкидається (i та j обидва просуваються, але в result
                записується лише right[j]), що призводить до втрати одного
                з дублікатів на кожному рекурсивному рівні.
    Action:   виправлено заміною умови з розгалуженого if/elif/else на
              if left[i] <= right[j] з просуванням лише i —
              у такий спосіб рівні елементи лівої половини завжди
              записуються до результату.
    Note:     P2 (відсортованість) не виявила цього дефекту, оскільки
              список з однаковими елементами залишається відсортованим
              навіть після втрати дублікатів. Це підкреслює важливість
              перевірки P3 (перестановка) як окремої незалежної властивості.

Counterexample analysis:
  Мінімізований контрприклад [0, 0] — найпростіший випадок, де виникає
  дефект (два рівних елементи). Hypothesis автоматично спростив його
  з довших списків до цього мінімуму.
  Інтерпретація: дефект відтворюється для будь-якого lst, що містить
  хоча б два однакових елементи, тобто є систематичним, а не поодиноким.

Conclusion:
  Trust level:  HIGH (для коректної реалізації)

  Verified properties:
    P1 — збереження довжини (300 прикладів, PASS)
    P2 — відсортованість виходу (300 прикладів, PASS)
    P3 — мультимножинна рівність / перестановка (300 прикладів, PASS)
    P4 — ідемпотентність (300 прикладів, PASS)
    P5 — комутативність конкатенації (200 пар, PASS)

  Unverified / failed:  відсутні (для фінальної реалізації)

  Remarks:
    — Верифікація охоплює цілі числа у межах [-10^6, 10^6]; поведінка
      для чисел з рухомою крапкою або NaN не перевірена.
    — Property-based тестування не є формальним доведенням — воно
      демонструє відсутність контрприкладу на 200–300 згенерованих
      прикладах, що дає HIGH, але не ABSOLUTE довіру.
    — Тести P1–P5 є незалежними: кожен виявляє окремий клас дефектів.
      Зокрема, D-01 показав, що P2 (порядок) не здатна виявити дефект
      втрати дублікатів — для цього необхідна P3 (перестановка).
    — Для абсолютного доведення потрібні інструменти SMT-верифікації
      (наприклад, Dafny або Coq).
```