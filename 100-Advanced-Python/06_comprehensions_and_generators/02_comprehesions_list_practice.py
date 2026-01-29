"""
inventory = [
    {"article": "A1", "stock": 50, "price": 100},
    {"article": "B2", "stock": 0,  "price": 200},
    {"article": "C3", "stock": 12, "price": 150},
    {"article": "D4", "stock": 5,  "price": 500},
]
Nice, this is a **great foundation example** 👌
You already understand the **what** and **why** of comprehensions — now let’s turn that into **muscle memory**.

Below is a **progressive practice set**: easy → medium → real-world → trick questions.
Don’t rush. Try solving each **before** peeking at the solution.

---

# 🧠 PRACTICE SET: Python Comprehensions

We’ll use this base data unless mentioned otherwise:

```python
inventory = [
    {"article": "A1", "stock": 50, "price": 100},
    {"article": "B2", "stock": 0,  "price": 200},
    {"article": "C3", "stock": 12, "price": 150},
    {"article": "D4", "stock": 5,  "price": 500},
]
```

---

## 🟢 LEVEL 1 — Warm-up (List Comprehensions)

### 1️⃣ Get all article names

**Expected output**

```python
["A1", "B2", "C3", "D4"]
```

👉 *Hint:* no condition needed.

---

### 2️⃣ Get articles that are **out of stock**

**Expected output**

```python
["B2"]
```

---

### 3️⃣ Get stocks **greater than 10**

**Expected output**

```python
[50, 12]
```

---

## 🟡 LEVEL 2 — Slightly Smarter Filters

### 4️⃣ Get articles whose **price > 150 AND stock > 0**

**Expected output**

```python
["D4"]
```

---

### 5️⃣ Convert article names to lowercase **only if in stock**

**Expected output**

```python
["a1", "c3", "d4"]
```

---

## 🟠 LEVEL 3 — Dictionary Comprehensions (VERY IMPORTANT)

### 6️⃣ Create a dictionary `{article: stock}` for in-stock items

**Expected output**

```python
{"A1": 50, "C3": 12, "D4": 5}
```

---

### 7️⃣ Create `{article: price}` **only for items costing >= 200**

**Expected output**

```python
{"B2": 200, "D4": 500}
```

---

## 🔵 LEVEL 4 — Set Comprehensions

### 8️⃣ Get **unique stock values** greater than 0

**Expected output**

```python
{50, 12, 5}
```

---

## 🔴 LEVEL 5 — Real-World Thinking (Important)

### 9️⃣ Calculate **total inventory value per item**

Formula:

```text
stock * price
```

**Expected output**

```python
[5000, 1800, 2500]
```

(only include items with stock > 0)

---

### 🔟 Build this structure:

```python
[
    {"article": "A1", "value": 5000},
    {"article": "C3", "value": 1800},
    {"article": "D4", "value": 2500},
]
```

---

## 🧠 BONUS — Tricky (Interview-style)

### 11️⃣ Replace stock with `"OUT_OF_STOCK"` when stock == 0

**Expected output**

```python
["A1", "OUT_OF_STOCK", "C3", "D4"]
```

👉 *Hint:* ternary inside comprehension

---

### 12️⃣ Nested comprehension (read carefully)

```python
warehouses = {
    "BLR": ["A1", "B2"],
    "DEL": ["C3", "D4"],
}
```

👉 Get **all article names** in a **single list**
**Expected output**

```python
["A1", "B2", "C3", "D4"]
```
---
"""

inventory = [
    {"article": "A1", "stock": 50, "price": 100},
    {"article": "B2", "stock": 0,  "price": 200},
    {"article": "C3", "stock": 12, "price": 150},
    {"article": "D4", "stock": 5,  "price": 500},
]


all_article_names = [item["article"] for item in inventory ]
print(all_article_names)

# OUTPUT : ['A1', 'B2', 'C3', 'D4']


out_of_stock_articles = [item["article"] for item in inventory if item["stock"] == 0 ]

print(out_of_stock_articles)
#OUTPUT : ['B2']


stocks_greater_than_10 = [i["stock"] for i in inventory if i["stock"] > 10]
print(stocks_greater_than_10)
# [50, 12]

price_and_stock  = [item["article"] for item in inventory if item["price"] > 150 and item["stock"] > 0]
print(price_and_stock)

#OUTPUT : ['D4']

lower_case_article_in_stock = [
    item["article"].lower()
    for item in inventory
    if item["stock"] > 0
]

print(lower_case_article_in_stock)

upper_case_article_stock_greater_10 = [
    item["article"].upper()
    for item in inventory
    if item["stock"] > 10
]

print(upper_case_article_stock_greater_10)

prefix_article = [
    f'ITEM-{item["article"].upper()}'
    for item in inventory
    if item["stock"] > 0
]

print(prefix_article)

inventory_value = [
    f'{item["article"]}={item["price"] * item["stock"]}'
    for item in inventory
    if item["stock"] > 0
]
print(inventory_value)

mixed_transformation = [
    item["article"].upper() if item["stock"] > 0 else "OUT_OF_STOCK"
    for item in inventory
]
print(mixed_transformation)





"""
ENTIRE OUTPUT : 
['A1', 'B2', 'C3', 'D4']
['B2']
[50, 12]
['D4']
['a1', 'c3', 'd4']
['A1', 'C3']
['ITEM-A1', 'ITEM-C3', 'ITEM-D4']
['A1=100', 'C3=150', 'D4=500']
['A1', 'OUT_OF_STOCK', 'C3', 'D4']
"""