# explore_data_set
This project focuses on analyzing and visualizing differences between AI-generated and human-written essays using data visualization techniques in Python.

## 📂 Project Overview
The dataset contains essays labeled as:
- **0 → Human-written**
- **1 → code outputs of screeshots**

The project explores patterns such as:
- Text length distribution  
- Label distribution  
- Word frequency  
- Outliers and trends  

---

## ⚙️ Technologies Used
- Python 🐍  
- Pandas  
- Matplotlib  
- Seaborn  
- Plotly  

---

## 📊 Features & Visualizations

### 1. Data Loading & Exploration
- Load dataset using Pandas  
- Display dataset structure and columns  

### 2. Text Length Analysis
- Created a new feature: `text_length`  
- Helps understand essay size patterns  

### 3. Visualizations
- 📌 Countplot (AI vs Human essays)  
- 📌 Histograms (basic + styled + KDE)  
- 📌 Boxplots (outlier detection)  
- 📌 Styled plots using Seaborn & Matplotlib  
- 📌 Interactive plots using Plotly  
- 📌 Top 20 most frequent words  

---

## 📈 Key Insights
- AI-generated essays tend to have different length distributions compared to human-written ones  
- Text length can be a useful feature for classification  
- Word frequency analysis reveals common patterns in writing  

---

## 🗂️ Project Structure
├── StylingMethods.py # Basic dataset loading
├── Visualization1.py # Countplot + text length
├── visualizationplots.py # Advanced visualizations
├── train_v2_drcat_02.csv.zip
└── README.md
csv file:https://www.kaggle.com/datasets/thedrcat/daigt-v2-train-dataset

---

## 🎯 Conclusion
This project demonstrates how exploratory data analysis (EDA) and visualization techniques can help identify patterns between AI-generated and human-written content.

   

