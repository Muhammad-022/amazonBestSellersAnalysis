
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_csv('best-selling-books.csv')


print("First 5 rows of the dataset:")
print(df.head())
print("\nShape of the dataset:")
print(df.shape)
print("\nColumn names:")
print(df.columns)
print("\nSummary statistics:")
print(df.describe())


df.drop_duplicates(inplace=True)

print("\nData after cleaning:")
print(df.head())


author_counts = df['Author(s)'].value_counts()
print("\nTop authors by number of books on the list:")
print(author_counts.head(10))


# Bar chart of top 10 authors
plt.figure(figsize=(10,6))
sns.barplot(x=author_counts.head(10).values, 
            y=author_counts.head(10).index, 
            palette="viridis")
plt.title("Top 10 Authors by Number of Books")
plt.xlabel("Number of Books")
plt.ylabel("Author(s)")
plt.tight_layout()
plt.savefig("top_authors_chart.png") 
plt.show()

# Histogram of Approximate Sales
plt.figure(figsize=(10,6))
sns.histplot(df['Approximate sales in millions'], bins=15, kde=True, color='skyblue')
plt.title("Distribution of Book Sales (in millions)")
plt.xlabel("Approximate Sales in Millions")
plt.ylabel("Number of Books")
plt.tight_layout()
plt.savefig("sales_distribution_chart.png")
plt.show()


author_counts.head(10).to_csv("top_authors.csv", index=True)
print("\nAnalysis complete! Top authors chart and sales distribution chart displayed.")
