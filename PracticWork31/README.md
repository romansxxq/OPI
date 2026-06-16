# Практична робота №31

## Розробка тестових випадків для аналізу варіантів

---

## 1. Опис функції

```text
Function: calculate_discount(price, is_member, is_holiday)
Description: Обчислює фінальну ціну товару з урахуванням знижок
```

### Умови:

* **C1:** Користувач є учасником програми лояльності?
* **C2:** Зараз святковий день?

---

## 2. Decision Table

| Conditions | Rule 1   | Rule 2   | Rule 3   | Rule 4   |
| ---------- | -------- | -------- | -------- | -------- |
| C1         | Y        | Y        | N        | N        |
| C2         | Y        | N        | Y        | N        |
| ---------- | -------- | -------- | -------- | -------- |
| A1 (20%)   | X        |          |          |          |
| A2 (10%)   |          | X        | X        |          |
| A3 (0%)    |          |          |          | X        |

### Пояснення:

* Якщо **member + holiday → 20%**
* Якщо **member або holiday → 10%**
* Інакше → 0%

---

## 3. Класи еквівалентності

### Condition C1 (is_member)

| Class   | Values | Representative | Boundary |
| ------- | ------ | -------------- | -------- |
| Valid   | True   | True           | —        |
| Invalid | False  | False          | —        |

### Condition C2 (is_holiday)

| Class   | Values | Representative | Boundary |
| ------- | ------ | -------------- | -------- |
| Valid   | True   | True           | —        |
| Invalid | False  | False          | —        |

---

## 4. Реалізація функції

```python
def calculate_discount(price, is_member, is_holiday):
    if is_member and is_holiday:
        return price * 0.8
    elif is_member or is_holiday:
        return price * 0.9
    else:
        return price
```

---

## 5. Тестові кейси

```python
import pytest

# Rule 1: C1=Y, C2=Y → 20%
def test_rule1_member_and_holiday():
    result = calculate_discount(100, True, True)
    assert result == 80

# Rule 2: C1=Y, C2=N → 10%
def test_rule2_member_only():
    result = calculate_discount(100, True, False)
    assert result == 90

# Rule 3: C1=N, C2=Y → 10%
def test_rule3_holiday_only():
    result = calculate_discount(100, False, True)
    assert result == 90

# Rule 4: C1=N, C2=N → 0%
def test_rule4_no_discount():
    result = calculate_discount(100, False, False)
    assert result == 100
```

---

## 6. Boundary tests

```python
def test_price_zero():
    assert calculate_discount(0, True, True) == 0

def test_price_negative():
    assert calculate_discount(-100, True, True) == -80
```

---

## 7. Аналіз покриття

| Rule | Conditions | Action | Test       | Status  |
| ---- | ---------- | ------ | ---------- | ------- |
| 1    | Y,Y        | 20%    | test_rule1 | COVERED |
| 2    | Y,N        | 10%    | test_rule2 | COVERED |
| 3    | N,Y        | 10%    | test_rule3 | COVERED |
| 4    | N,N        | 0%     | test_rule4 | COVERED |

### Boundary:

* price = 0 → COVERED
* price < 0 → COVERED

---

## 8. Прогалини

* Немає перевірки великих значень (наприклад 1e9)
* Немає перевірки типів (string, None)

---

## 9. Висновок

Було побудовано decision table, створено тестові кейси та досягнуто повного покриття всіх варіантів.

---
