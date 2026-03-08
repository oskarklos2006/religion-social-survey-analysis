# 🌍 Religion & Social Interactions — Survey Analysis

An international hackathon project analyzing how religious beliefs and affiliations influence social interactions, trust, and attitudes across multiple countries. Built collaboratively during a hackathon, this repository contains my personal contribution to the data analysis pipeline.

---

## 📌 Overview

Using a large-scale survey dataset of **10,000 responses across 400+ variables**, this project explores the relationship between religious identity and social behaviors such as trust, discrimination, political orientation, and perception of other religions.

The dataset covers respondents from **Poland, Germany, the US, and the UK**, with income normalized using PPP (Purchasing Power Parity) conversion for cross-country comparability.

---

## 🔍 Key Research Areas

- How does religious affiliation affect **social trust**?
- Do religious people perceive **other religions** differently?
- How does religion correlate with **political orientation** (left vs right)?
- What is the relationship between religion and **experienced discrimination**?
- How does **income and age** interact with religious belief?

---

## 📊 Dataset

The dataset was provided as part of an **international hackathon** and is not publicly available. It contains survey responses covering:

- Religious affiliation and strength of belief
- Social trust and perception of others
- Experienced discrimination (workplace, housing, public spaces)
- Political orientation and media trust
- Demographic information (age, gender, income, country)

---

## 🔧 Tech Stack

- **Python** — pandas, numpy
- **Visualization** — matplotlib, seaborn
- **Analysis** — statistical correlation, group-wise imputation, feature engineering

---

## 🧪 My Contribution

| File | Description |
|---|---|
| `oskar.ipynb` | Main analysis notebook — EDA, feature engineering, correlation analysis |
| `oskar2.ipynb` | Extended analysis — model preparation, income standardization |
| `convert_currencies.py` | PPP-based income conversion across countries |
| `split_by_religions.py` | Splits dataset by religious group for subgroup analysis |
| `standardize_dataset.py` | Data cleaning and standardization pipeline |

---

## 🌐 Analysis Highlights

- **Income normalization** — converted income brackets from PLN, USD, and GBP to a common EUR-based PPP index for fair cross-country comparison
- **Group-wise imputation** — missing values filled using median per country, religion, gender and age group
- **Feature engineering** — created composite scores for social trust, discrimination frequency, and religiosity strength
- **Subgroup analysis** — compared attitudes across 7 religious groups including Christianity, Islam, Judaism, Buddhism and Atheism

---

## 🚀 How to Run

1. Clone the repository:
```bash
git clone https://github.com/oskarklos2006/religion-social-survey-analysis.git
cd religion-social-survey-analysis
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Add your own dataset as `dataset.csv` in the root folder, then open the notebooks:
```bash
jupyter notebook oskar.ipynb
```

> ⚠️ The original dataset is not included as it was provided under hackathon confidentiality terms.

---

## 👤 Author

**Oskar Klos**  
[GitHub](https://github.com/oskarklos2006)
