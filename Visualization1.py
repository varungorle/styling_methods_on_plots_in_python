import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("train_v2_drcat_02.csv.zip")

# Create text length column
df['text_length'] = df['text'].apply(len)

# Display first few rows of text length
print(df[['text_length']].head())

# Plot label distribution
sns.countplot(x='label', data=df)
plt.title("AI vs Human Essays")
plt.show()