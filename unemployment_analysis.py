import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("Unemployment in India.csv")

# Rename columns (clean names)
df.columns = ["Region", "Date", "Frequency", "Estimated Unemployment Rate", 
              "Estimated Employed", "Estimated Labour Participation Rate", "Area"]

# Convert Date column
df["Date"] = pd.to_datetime(df["Date"])

# Show data
print(df.head())

# -------------------------------
# Visualization 1: Unemployment over time
plt.figure()
sns.lineplot(x="Date", y="Estimated Unemployment Rate", data=df)
plt.title("Unemployment Rate Over Time")
plt.xticks(rotation=45)
plt.show()

# -------------------------------
# Visualization 2: Region-wise unemployment
plt.figure()
sns.barplot(x="Region", y="Estimated Unemployment Rate", data=df)
plt.xticks(rotation=90)
plt.title("Unemployment Rate by Region")
plt.show()

# -------------------------------
# Visualization 3: Heatmap
pivot = df.pivot_table(values="Estimated Unemployment Rate",
                       index="Region", columns="Area")

plt.figure()
sns.heatmap(pivot, annot=True, cmap="coolwarm")
plt.title("Unemployment Heatmap")
plt.show()