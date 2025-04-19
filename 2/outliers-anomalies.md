

## 🔍 What Are Outliers & Anomalies?

### 📌 **Outlier**
An **outlier** is a data point that **differs significantly** from other observations. It lies **far away** from the rest of the data.

> E.g. In a dataset of student test scores: [45, 46, 47, 50, 100], the `100` might be an outlier.

### 📌 **Anomaly**
An **anomaly** is a **data point or event** that is **unexpected** — it may or may not be a mistake. Anomalies could signal:
- Errors in data entry
- Fraud
- New trends or discoveries
- Sensor malfunction

> In essence, every **outlier** is a candidate for being an **anomaly**, but **not all anomalies are outliers**.

---

## 🧠 Why Detect and Handle Outliers?

- They **skew** statistical measures (mean, variance, correlation)
- Can lead to **biased models**
- May represent **real and interesting patterns** (fraud, disease, innovation, etc.)
- Help in **data cleaning**, **robust modeling**, or **insight discovery**

---

## 🔢 Types of Outliers

1. **Global Outliers** – Far from all data
2. **Contextual Outliers** – Normal in one context, abnormal in another (e.g. 25°C in summer vs winter)
3. **Collective Outliers** – A group behaves strangely together

---

## 🛠️ Methods to Detect Outliers


### ✅ 1. **Statistical Methods**

#### 📌 Z-score (Standard Score)
- Measures how many standard deviations a point is from the mean
- Formula:  
  $
  Z = \frac{(X - \mu)}{\sigma}
  $
- Threshold: Usually **|Z| > 3** is considered an outlier

```python
def detect_outliers_z(data):
    mean = sum(data) / len(data)
    std = (sum((x - mean)**2 for x in data) / len(data)) ** 0.5
    return [x for x in data if abs((x - mean)/std) > 3]
```

---

#### 📌 IQR Method (Interquartile Range)
- Find **Q1 (25%)**, **Q3 (75%)**
- IQR = Q3 - Q1
- Outliers:  
  - Less than **Q1 - 1.5×IQR**  
  - Greater than **Q3 + 1.5×IQR**

```python
def detect_outliers_iqr(data):
    data = sorted(data)
    q1 = data[len(data)//4]
    q3 = data[(3*len(data))//4]
    iqr = q3 - q1
    lower = q1 - 1.5 * iqr
    upper = q3 + 1.5 * iqr
    return [x for x in data if x < lower or x > upper]
```

---

### ✅ 2. **Visualization Methods**

| Method        | Purpose                              |
|---------------|--------------------------------------|
| Box Plot      | Shows IQR, median, and outliers      |
| Histogram     | See skewed values                    |
| Scatter Plot  | Spot anomalies in 2D                 |
| KDE Plot      | See density dips for rare values     |

```python
import seaborn as sns
import matplotlib.pyplot as plt

sns.boxplot(data=[45, 46, 47, 50, 100])
plt.show()
```

---

### ✅ 3. **Machine Learning Methods**

- **Isolation Forest**
- **DBSCAN (Density-Based Spatial Clustering)**
- **Autoencoders (for high-dimensional anomaly detection)**
- **One-Class SVM**

```python
from sklearn.ensemble import IsolationForest

clf = IsolationForest()
pred = clf.fit_predict([[x] for x in data])
outliers = [x for x, p in zip(data, pred) if p == -1]
```

---

## 🧹 How to Handle Outliers?

### 🔄 1. **Remove Them**
Best when:
- Caused by error
- Small dataset
- Very far from main data

```python
cleaned = [x for x in data if x not in outliers]
```

---

### 🧱 2. **Cap or Floor (Winsorization)**
Limit values to a certain percentile (e.g. 5th & 95th)

```python
import numpy as np

q1, q3 = np.percentile(data, [5, 95])
winsorized = [min(max(x, q1), q3) for x in data]
```

---

### 🔧 3. **Transform the Data**
Use **log**, **square root**, or **Box-Cox** transformations to reduce the influence of outliers.

```python
import numpy as np
transformed = np.log([x+1 for x in data])  # +1 to avoid log(0)
```

---

### 📊 4. **Use Robust Algorithms**
- **Median-based methods** (e.g., median absolute deviation)
- **Tree-based models** like Random Forest
- **Robust regression** (e.g., Huber regressor)

---

## ⚠️ Important Tips

- Never remove outliers **blindly** — understand the **domain** and **context**.
- Visualize before and after handling.
- Maintain a separate record of **removed/moderated** values.

---

## ✅ Summary

| Step                | Tool / Method                    |
|---------------------|----------------------------------|
| Detection           | Z-score, IQR, Visualizations     |
| Handling            | Remove, Cap, Transform           |
| Advanced Detection  | Isolation Forest, Autoencoders   |
| Prevention          | Robust stats / models            |

---
