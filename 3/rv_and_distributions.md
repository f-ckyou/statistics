
## 📌 **1. What is a Random Variable?**

A **Random Variable (RV)** is a function that assigns a real number to each outcome in a sample space.

### 🎲 Example:
Let’s say you toss a fair coin twice. The sample space is:
```
S = {HH, HT, TH, TT}
```
Define a random variable $ X $ as the number of **heads** in the outcome.

Then:
- $ X(HH) = 2 $
- $ X(HT) = 1 $
- $ X(TH) = 1 $
- $ X(TT) = 0 $

So $ X $ maps outcomes to numerical values:  
$
X \in \{0, 1, 2\}
$

---

## 📌 **2. Types of Random Variables**

### a. **Discrete Random Variable**
Takes **countable** values (usually integers).

#### 🎲 Example:
Number of goals in a football match: $ X \in \{0, 1, 2, 3, \dots\} $

---

### b. **Continuous Random Variable**
Takes values from an **uncountable** range (e.g., real numbers).

#### 🌡️ Example:
Temperature in a city on a given day: $ X \in \mathbb{R} $

---

## 📌 **3. Probability Distribution**

A **Probability Distribution** tells us **how probabilities are distributed** over values of the random variable.

### a. **For Discrete Random Variables** — *Probability Mass Function (PMF)*

It gives the probability that a discrete RV is exactly equal to some value.

$
P(X = x) = p(x)
$

#### 🎲 Example:
Roll a fair 6-sided die. Let $ X $ be the outcome:
$
P(X = x) = \frac{1}{6}, \quad x = 1, 2, 3, 4, 5, 6
$

Properties:
- $ 0 \leq P(X = x) \leq 1 $
- $ \sum_x P(X = x) = 1 $

Common Discrete distributions:
- Bernoulli distribution
- Binomial distribution
- Poisson distribution

---

### b. **For Continuous Random Variables** — *Probability Density Function (PDF)*

Instead of probabilities at points, it gives **density** over intervals.

$
P(a \leq X \leq b) = \int_a^b f(x) dx
$

#### 🌡️ Example:
Suppose $ X $ is uniformly distributed between 0 and 1:

$
f(x) = 
\begin{cases}
1, & \text{if } 0 \le x \le 1 \\
0, & \text{otherwise}
\end{cases}
$

Then $ P(0.2 \le X \le 0.5) = \int_{0.2}^{0.5} 1\, dx = 0.3 $

Properties:
- $ f(x) \geq 0 $
- $ \int_{-\infty}^{\infty} f(x)\, dx = 1 $

Common Continuous distributions:
- Normal (Gaussian) distribution
- Exponential distribution
- Uniform distribution

---

## 📌 **4. Cumulative Distribution Function (CDF)**

For **both discrete and continuous** RVs:

$
F(x) = P(X \leq x)
$

Properties:
- $ F(x) $ is non-decreasing.
- $ \lim_{x \to -\infty} F(x) = 0 $
- $ \lim_{x \to \infty} F(x) = 1 $

---

## 📌 **5. Expected Value (Mean)**

The **average** value of a random variable over many trials.

- **Discrete:**  
$
E[X] = \sum_x x \cdot P(X = x)
$

- **Continuous:**  
$
E[X] = \int_{-\infty}^{\infty} x \cdot f(x)\, dx
$

---

## 📌 **6. Variance and Standard Deviation**

They measure the **spread** of the distribution.

$
\text{Var}(X) = E[(X - E[X])^2]
$
<br>
$
\text{Std}(X) = \sqrt{\text{Var}(X)}
$

---

## 📌 **7. Common Probability Distributions**

### 🔹 Discrete:
| Distribution | Use Case |
|--------------|-----------|
| **Bernoulli(p)** | One trial (e.g., coin toss) |
| **Binomial(n, p)** | Number of successes in \( n \) Bernoulli trials |
| **Poisson(λ)** | Number of events in a fixed interval (rare events) |
| **Geometric(p)** | Number of trials until first success |

---

### 🔹 Continuous:
| Distribution | Use Case |
|--------------|-----------|
| **Uniform(a, b)** | Equal probability across interval |
| **Normal(μ, σ²)** | Bell-shaped distribution (central limit theorem) |
| **Exponential(λ)** | Time between Poisson events |
| **Beta(α, β)** | Probabilities or proportions |
| **Gamma(α, β)** | Wait time for α Poisson events |

---

## 🧠 Example Scenario

### Scenario:
A factory produces bulbs. 90% of the bulbs are not defective.

Let $ X = 1 $ if a bulb is **good**, and $ X = 0 $ if **defective**.

Then $ X \sim \text{Bernoulli}(0.9) $

- $ E[X] = 1 \cdot 0.9 + 0 \cdot 0.1 = 0.9 $
- $ \text{Var}(X) = 0.9(1 - 0.9) = 0.09 $

---

## ✅ Summary

| Concept | Purpose |
|--------|---------|
| Random Variable | Assign numbers to outcomes |
| PMF/PDF | Define how probability is distributed |
| CDF | Cumulative probability up to a point |
| Expectation | Mean or long-term average |
| Variance | Measure of spread |
| Distributions | Describe real-world phenomena mathematically |

