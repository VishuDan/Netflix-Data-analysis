
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("C:\\Users\\vdand\\Downloads\\netflix_titles.csv\\netflix_titles.csv")

# Show basic info
print(df.head())

# Count Movies vs TV Shows
type_count = df["type"].value_counts()
print(type_count)

# Plot content type
plt.figure()
type_count.plot(kind="bar")
plt.title("Movies vs TV Shows on Netflix")
plt.xlabel("Type")
plt.ylabel("Count")
plt.show()

# Top 10 countries
top_countries = df["country"].value_counts().head(10)

plt.figure()
top_countries.plot(kind="barh")
plt.title("Top 10 Countries Producing Content")
plt.show()