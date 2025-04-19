
## 🔹 What is **Skewness**?

### 📘 Definition:
**Skewness** measures the **asymmetry** (lopsidedness) of a distribution around its **mean**.

---

### 🔸 Types of Skewness:

| Type              | Description                                                         | Shape |
|-------------------|---------------------------------------------------------------------|--------|
| **Zero Skewness** | Perfectly symmetrical distribution (e.g., normal distribution)       | 🔵     |
| **Positive Skew** | Tail on the **right** (more smaller values, fewer large ones)       | ➡️     |
| **Negative Skew** | Tail on the **left** (more larger values, fewer small ones)         | ⬅️     |

### 🧠 Example:

- Test scores where a few students score **much higher** = **positively skewed**
- Incomes where a few people earn **very little** = **negatively skewed**

---

### 🧮 Formula (Sample Skewness):
$
\text{Skewness} = \frac{n}{(n-1)(n-2)} \sum \left( \frac{x_i - \bar{x}}{s} \right)^3
$

Where:
- $ n $ = number of observations  
- $ \bar{x} $ = sample mean  
- $ s $ = sample standard deviation  
- $ x_i $ = individual value

> A value:
> - Close to **0** → symmetrical
> - **> 0** → right-skewed
> - **< 0** → left-skewed

---

## 🔹 What is **Kurtosis**?

### 📘 Definition:
**Kurtosis** measures the **"tailedness"** of the distribution — how heavy or light the tails are compared to a normal distribution.

---

### 🔸 Types of Kurtosis:

| Type          | Description                                              | Visual |
|---------------|----------------------------------------------------------|--------|
| **Mesokurtic** | Normal distribution (benchmark, kurtosis = 3)           | 📊     |
| **Leptokurtic**| Heavy tails, sharp peak (kurtosis > 3) → more outliers  | 🔺     |
| **Platykurtic**| Light tails, flatter peak (kurtosis < 3) → fewer outliers | 🔻     |

> Often, we calculate **excess kurtosis**:
$
\text{Excess Kurtosis} = \text{Kurtosis} - 3
$
- Excess > 0 → leptokurtic  
- Excess < 0 → platykurtic

---

### 🧮 Formula (Sample Kurtosis):
$
\text{Kurtosis} = \frac{n(n+1)}{(n-1)(n-2)(n-3)} \sum \left( \frac{x_i - \bar{x}}{s} \right)^4 - \frac{3(n-1)^2}{(n-2)(n-3)}
$


---

## 📌 Summary Table

| Concept   | Meaning                                   | Interpretation                 |
|-----------|--------------------------------------------|--------------------------------|
| Skewness  | Asymmetry of distribution                  | < 0 (Left), 0 (Symmetric), > 0 (Right) |
| Kurtosis  | Tailedness or sharpness of the peak        | < 3 (Flat), 3 (Normal), > 3 (Sharp)    |
| Excess Kurtosis | Kurtosis minus 3                    | Easier to compare with normal dist.   |

---
