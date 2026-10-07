# 0/1 Knapsack using Dynamic Programming

## Question

A passenger is travelling by train with a limited luggage allowance of W kg. Each item has a weight and a usefulness value. The passenger can either carry or leave each item and cannot carry fractions of an item.

**Task:** Implement 0/1 Knapsack using Dynamic Programming to maximize the total usefulness of the luggage while satisfying the weight constraint.

**Display:**

* Maximum achievable usefulness
* Selected luggage items
* DP table
* Time and space complexity

---

## Aim

To implement the **0/1 Knapsack problem using Dynamic Programming** and find the maximum usefulness of luggage within the given weight limit.

---

## Algorithm

1. Store the weight and value of each item.
2. Set the maximum luggage capacity `W`.
3. Create a DP table.
4. For each item, check whether its weight can fit.
5. If it fits, choose the maximum of:

   * Not selecting the item.
   * Selecting the item.
6. The last value in the DP table gives the maximum usefulness.
7. Trace the table backwards to find the selected items.
8. Display the DP table and complexity.

---

## Program

```python
weights = [3, 4, 2, 1]
values = [5, 9, 3, 2]
W = 5

dp = [[0] * (W + 1) for i in range(len(weights) + 1)]

for i in range(1, len(weights) + 1):
    for w in range(W + 1):
        if weights[i - 1] <= w:
            dp[i][w] = max(
                dp[i - 1][w],
                values[i - 1] + dp[i - 1][w - weights[i - 1]]
            )
        else:
            dp[i][w] = dp[i - 1][w]

print("Maximum usefulness:", dp[len(weights)][W])

w = W
items = []

for i in range(len(weights), 0, -1):
    if dp[i][w] != dp[i - 1][w]:
        items.append(i)
        w -= weights[i - 1]

print("Selected items:", items[::-1])

print("DP Table:")
for row in dp:
    print(row)

print("Time: O(nW)")
print("Space: O(nW)")
```

---

## Output

```text
Maximum usefulness: 11
Selected items: [2, 4]

DP Table:
[0, 0, 0, 0, 0, 0]
[0, 0, 0, 5, 5, 5]
[0, 0, 0, 5, 9, 9]
[0, 0, 3, 5, 9, 9]
[0, 2, 3, 5, 9, 11]

Time: O(nW)
Space: O(nW)
```

### Explanation of Selected Items

* Item 2 → Weight = 4, Value = 9
* Item 4 → Weight = 1, Value = 2

Total weight:

```text
4 + 1 = 5 kg
```

Total usefulness:

```text
9 + 2 = 11
```

Therefore, **items 2 and 4 give the maximum usefulness of 11 within the 5 kg limit.**

---

## Time Complexity

**O(nW)**

Where:

* `n` = number of items
* `W` = maximum luggage capacity

## Space Complexity

**O(nW)**

The DP table requires `n × W` space.

---

## Result

The 0/1 Knapsack problem was successfully implemented using Dynamic Programming. For the given input, the maximum achievable usefulness is **11**, by selecting **items 2 and 4** within the luggage capacity of **5 kg**.

---

# Viva Questions and Answers

### 1. What is the 0/1 Knapsack problem?

It is a problem where we select items to get the **maximum value within a limited weight**.

### 2. Why is it called 0/1 Knapsack?

Because each item has only two choices:

**0 → Do not take the item**
**1 → Take the item**

### 3. Which technique is used?

**Dynamic Programming** is used.

### 4. What does `dp[i][w]` mean?

It represents the **maximum usefulness using the first `i` items with capacity `w`**.

### 5. What is the time and space complexity?

**Time:** `O(nW)`
**Space:** `O(nW)`
