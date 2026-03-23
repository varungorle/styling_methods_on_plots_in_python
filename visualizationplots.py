import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from collections import Counter
import re

# -------------------------------
# Load Dataset
# -------------------------------
df = pd.read_csv("train_v2_drcat_02.csv.zip")

# -------------------------------
# Add Text Length Column
# -------------------------------
df['text_length'] = df['text'].apply(len)

# -------------------------------
# 1. Histogram (Basic)
# -------------------------------
plt.hist(df['text_length'], bins=50)
plt.title("Text Length Distribution")
plt.xlabel("Length")
plt.ylabel("Frequency")
plt.show()

# -------------------------------
# 2. Styled Histogram
# -------------------------------
plt.figure(figsize=(10,5))
plt.hist(df['text_length'], bins=50, color='purple', edgecolor='black')

plt.title("Styled Text Length Histogram")
plt.xlabel("Text Length")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()

# -------------------------------
# 3. Seaborn Histogram
# -------------------------------
sns.histplot(df['text_length'], bins=50, kde=True)
plt.title("Seaborn Histogram with KDE")
plt.show()

# -------------------------------
# 4. Boxplot (Outliers)
# -------------------------------
sns.boxplot(x='label', y='text_length', data=df)
plt.title("Text Length by Label")
plt.show()

# -------------------------------
# 5. Styled Boxplot
# -------------------------------
sns.set_style("darkgrid")

sns.boxplot(x='label', y='text_length', data=df, palette="Set2")
plt.title("Styled Boxplot")
plt.show()

# -------------------------------
# 6. Styled Countplot
# -------------------------------
sns.set_style("whitegrid")
sns.set_palette("pastel")

sns.countplot(x='label', data=df)
plt.title("Styled Countplot (AI vs Human)")
plt.show()

# -------------------------------
# 7. Matplotlib Global Style
# -------------------------------
plt.style.use("ggplot")

plt.hist(df['text_length'], bins=50)
plt.title("GGPlot Style Histogram")
plt.show()

# -------------------------------
# 8. Top 20 Words
# -------------------------------
all_words = " ".join(df['text']).lower()
words = re.findall(r'\b\w+\b', all_words)

word_counts = Counter(words).most_common(20)

words, counts = zip(*word_counts)

plt.figure(figsize=(12,6))
plt.bar(words, counts)

plt.xticks(rotation=45)
plt.title("Top 20 Words")
plt.xlabel("Words")
plt.ylabel("Frequency")
plt.show()

# -------------------------------
# 9. Plotly Interactive Histogram
# -------------------------------
fig = px.histogram(df, x="text_length", title="Interactive Histogram")
fig.show()

# -------------------------------
# 10. Plotly Styled Histogram
# -------------------------------
fig = px.histogram(
    df,
    x="text_length",
    color="label",
    template="plotly_dark"
)
fig.show()