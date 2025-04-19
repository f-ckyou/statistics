
## 🔹 1. **Percentiles**

> A **percentile** is a value **below which a given percentage of observations in a dataset falls**.

For example:
- The **20th percentile (P20)** is the value below which **20%** of the data lies.
- The **90th percentile (P90)** means 90% of the values are **less than or equal to** this value.

### 🧮 Formula (for position):
$
\text{Percentile Position (P-k)} = \frac{k}{100} \times (n + 1)
$
Where:
- `k` is the percentile (e.g., 25 for 25th percentile)
- `n` is the number of data points

> We interpolate if the position is not a whole number.

---

## 🔹 2. **Quartiles**

### 📘 Definition:
**Quartiles** split data into **four equal parts**:

| Quartile | Name              | Description                          |
|----------|-------------------|--------------------------------------|
| Q1       | 1st Quartile (25%)| 25% of the data is below this value  |
| Q2       | Median (50%)      | Middle value                         |
| Q3       | 3rd Quartile (75%)| 75% of the data is below this value  |

- Q2 is simply the **median** of the dataset.
- Q1 = 25th percentile = median of the **lower half**
- Q3 = 75th percentile = median of the **upper half**

---

## 🔹 3. **IQR (Interquartile Range)**

### 📘 Definition:
The **IQR** is the **range of the middle 50% of the data**.  
$
\text{IQR} = Q3 - Q1
$

It measures **how concentrated the central values are**.  
Very useful for detecting **outliers** and **skewness**.

### 🔍 Outlier Rule:
Any value:
$
< Q1 - 1.5 \times IQR \quad \text{or} \quad > Q3 + 1.5 \times IQR
$
… is considered an **outlier**.

---

## 📊 Example: Let’s understand with data

```python
data = [3, 7, 8, 5, 12, 14, 21, 13, 18]
```

### Step-by-step:

1. **Sort data**:
```
[3, 5, 7, 8, 12, 13, 14, 18, 21]
```

2. **Q2 (median)** = 12 (middle value)

3. **Lower half** (before median): [3, 5, 7, 8] → Q1 = (5 + 7)/2 = 6  
   **Upper half** (after median): [13, 14, 18, 21] → Q3 = (14 + 18)/2 = 16

4. **IQR** = Q3 - Q1 = 16 - 6 = **10**

---


## 📦 Summary Table:

| Concept     | Meaning                              | Key Formula                    |
|-------------|---------------------------------------|--------------------------------|
| Percentile  | Value below which x% of data lies     | \( \frac{k}{100} (n + 1) \)    |
| Quartiles   | Divides data into 4 equal parts       | Q1, Q2, Q3                     |
| IQR         | Spread of middle 50%                  | IQR = Q3 - Q1                  |
| Outliers    | Outside Q1-1.5×IQR or Q3+1.5×IQR      | Use IQR rule                   |

---
