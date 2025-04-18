
## 📦 **What is Data?**

> **Data** is information — facts, figures, or details collected for reference or analysis.

It could be numbers, text, images, audio, video, etc., that represent real-world phenomena. In computing and statistics, data is what we use to analyze, make decisions, or train machines.

---

## 📚 **Types of Data**

There are two main categories:

---

### 1. **Qualitative (Categorical) Data**
> Describes **qualities** or **categories** — **non-numeric**.

| Type         | Description                              | Example                        |
|--------------|------------------------------------------|--------------------------------|
| **Nominal**  | No order/ranking                         | Gender (Male, Female), Colors  |
| **Ordinal**  | Has order, but no exact difference       | Rating (Good, Average, Poor)   |

---

### 2. **Quantitative (Numerical) Data**
> Data that is **measurable**, in **numbers**.

| Type         | Description                              | Example                        |
|--------------|------------------------------------------|--------------------------------|
| **Discrete** | Countable values                         | Number of students (1, 2, 3…)  |
| **Continuous**| Measurable, infinite values possible     | Height, weight, temperature    |

---

### 🧠 Quick Trick to Remember:

- **Qualitative** = **Quality**
- **Quantitative** = **Quantity**

---

## 🌐 **Sources of Data**

### 📄 1. **Primary Data**
> Data you **collect yourself** directly from the source.

- **Methods:** Surveys, interviews, experiments, observations
- **Example:** You ask 100 students about their favorite subject.

✅ **Advantage:** Accurate, specific  
❌ **Disadvantage:** Time-consuming and costly

---

### 🌍 2. **Secondary Data**
> Data that’s already been **collected by someone else**.

- **Sources:** Books, research papers, government records, websites, open datasets
- **Example:** Using World Bank or Kaggle datasets

✅ **Advantage:** Easy to get, saves time  
❌ **Disadvantage:** May not perfectly fit your needs

---

## 🔁 Summary Table:

| Data Type       | Subtypes     | Examples                    |
|------------------|--------------|-----------------------------|
| Qualitative       | Nominal, Ordinal | Gender, Satisfaction level   |
| Quantitative      | Discrete, Continuous | Age, Height, Temperature     |

| Source Type    | Examples                                      |
|----------------|-----------------------------------------------|
| Primary        | Surveys, interviews, experiments              |
| Secondary      | Reports, research studies, online datasets    |

---


## 📊 What is **Structured Data**?

> **Structured data** is data that is **organized** into a **clear format**, usually **rows and columns** — like a table or spreadsheet.

---

### ✅ Characteristics of Structured Data:

| Feature              | Description                                     |
|----------------------|-------------------------------------------------|
| 🧱 **Tabular format**    | Stored in rows and columns                    |
| 📑 **Well-defined schema** | Every field has a specific data type         |
| 🔎 **Easily searchable** | Can query using SQL or data frames             |
| 🛢️ **Stored in**         | Databases (SQL), Excel, CSV files, etc.       |

---

### 📌 Examples of Structured Data:
- Student records in a school database  
  (Name | Age | Grade | ID)
- Sales data in a spreadsheet  
  (Product | Price | Quantity | Date)
- CSV files with labeled columns

---

### 🧠 In Python:
Structured data is handled using:
```python
import pandas as pd
df = pd.read_csv("data.csv")
print(df.head())
```

---

## 📂 What is **Unstructured Data**?

> **Unstructured data** is **not organized** in a pre-defined format. It’s raw, messy, and doesn’t fit easily into tables.

---

### ⚠️ Characteristics of Unstructured Data:

| Feature              | Description                                   |
|----------------------|-----------------------------------------------|
| 📂 **No fixed format**   | Doesn’t follow tabular structure              |
| 🧠 **Harder to analyze** | Needs preprocessing or advanced tools        |
| 🤖 **Used in AI/ML**     | Often used in natural language and image processing |
| 🗄️ **Stored in**         | Documents, images, audio, video, web pages   |

---

### 📌 Examples of Unstructured Data:
- Text from tweets, emails, or books
- Audio recordings
- Images and videos
- Web pages and PDFs

---

### 🧠 In Python:
Unstructured data is often handled with:
- **Text** → `nltk`, `spaCy`
- **Images** → `OpenCV`, `Pillow`
- **Audio** → `librosa`
- **Documents** → `pdfminer`, `PyMuPDF`, etc.

---

## 🔁 Summary Comparison:

| Feature            | Structured Data                  | Unstructured Data                |
|--------------------|----------------------------------|----------------------------------|
| Format             | Tabular (rows & columns)         | Free-form (text, media, etc.)    |
| Storage            | SQL DB, CSV, Excel               | Text files, images, videos       |
| Easy to Analyze?   | ✅ Yes                           | ❌ No (needs preprocessing)      |
| Tools in Python    | `pandas`, `numpy`, `sqlalchemy`  | `nltk`, `OpenCV`, `PyMuPDF`, etc.|
| Examples           | Bank records, employee database  | Emails, YouTube videos, tweets   |

---
