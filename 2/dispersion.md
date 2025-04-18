

# 📊 Measures of Dispersion – **Detailed Explanation + Python**

> While measures of central tendency (mean, median, mode) tell us *where* the data is centered, **measures of dispersion** tell us *how spread out or scattered* the data is.

---

## 🔹 Why Dispersion Matters?

Two datasets can have the same mean but very different variability:

- Dataset A: [10, 10, 10, 10, 10] → Mean = 10, no spread  
- Dataset B: [1, 5, 10, 15, 19] → Mean = 10, but high spread

Understanding dispersion helps in:
- Comparing consistency
- Risk analysis
- Data distribution shape
- Detecting outliers

---

## 🔹 Common Measures of Dispersion

| Measure                  | What it Tells You                                   |
|--------------------------|-----------------------------------------------------|
| **Range**                | Total spread (Max - Min)                            |
| **Variance**             | Average squared distance from the mean              |
| **Standard Deviation**   | Square root of variance (spread in original units)  |
| **Interquartile Range**  | Spread of the middle 50% of data                    |
| **Mean Absolute Deviation (MAD)** | Average of absolute differences from mean |

---

## 1. 🟡 **Range**

**Definition**:  
$
\text{Range} = \text{Max} - \text{Min}
$

**Python**:
```python
data = [4, 8, 6, 5, 3, 9, 12]
data_range = max(data) - min(data)
print("Range:", data_range)
```

---

## 2. 🟢 **Variance**

**Definition**:  
Average of squared differences from the mean.

- **Population Variance**:  
$
\sigma^2 = \frac{1}{N} \sum (x_i - \mu)^2
$

- **Sample Variance** (default in Python):  
$
s^2 = \frac{1}{n - 1} \sum (x_i - \bar{x})^2
$

**Python**:
```python
import statistics

sample_data = [4, 8, 6, 5, 3, 9, 12]
print("Sample Variance:", statistics.variance(sample_data))
print("Population Variance:", statistics.pvariance(sample_data))
```

---

## 3. 🔵 **Standard Deviation**

**Definition**:  
Square root of the variance — tells you average distance from mean in original units.

$
\text{SD} = \sqrt{\text{Variance}}
$

**Python**:
```python
print("Sample SD:", statistics.stdev(sample_data))
print("Population SD:", statistics.pstdev(sample_data))
```

---

## 4. 🟠 **Interquartile Range (IQR)**

**Definition**:  
Difference between 75th percentile (Q3) and 25th percentile (Q1). Covers the middle 50% of data.

$
\text{IQR} = Q3 - Q1
$

**Python**:
```python
import numpy as np

q1 = np.percentile(sample_data, 25)
q3 = np.percentile(sample_data, 75)
iqr = q3 - q1

print("Q1:", q1)
print("Q3:", q3)
print("IQR:", iqr)
```

---

## 5. 🔴 **Mean Absolute Deviation (MAD)**

**Definition**:  
Average of absolute deviations from the mean.

$
\text{MAD} = \frac{1}{n} \sum |x_i - \bar{x}|
$

**Python**:
```python
mean_val = statistics.mean(sample_data)
mad = sum(abs(x - mean_val) for x in sample_data) / len(sample_data)
print("MAD:", mad)
```

---

## 🧠 Summary Table

| Measure         | Function (statistics)     | Meaning                                 |
|------------------|---------------------------|-----------------------------------------|
| Range            | `max(data) - min(data)`   | Spread from min to max                  |
| Sample Variance  | `statistics.variance()`   | Average squared diff (n-1 denominator)  |
| Population Var   | `statistics.pvariance()`  | Average squared diff (n denominator)    |
| Sample SD        | `statistics.stdev()`      | Spread in original units                |
| Population SD    | `statistics.pstdev()`     | Same as above but for full population   |
| IQR              | `np.percentile()`         | Spread of central 50%                   |
| MAD              | Manual / NumPy / SciPy    | Average absolute deviation from mean    |

---

### ✅ Real-Life Application Examples

- **Standard deviation**: Used in finance to measure risk.
- **IQR**: Used in box plots to detect outliers.
- **Variance**: Used in ML to understand data spread.
- **MAD**: More robust when data has outliers.

---