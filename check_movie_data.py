import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_name = "IMDb Movies India.csv"
df = pd.read_csv(file_name, encoding='latin-1')
df = df.dropna(subset=['Rating'])

print("Number of movies with rating:", len(df))
print("Average rating overall:", df['Rating'].mean().round(2))
plt.figure(figsize=(10, 6))
sns.histplot(df['Rating'], bins=20, kde=True, color='teal')
plt.title('Distribution of IMDb Ratings (Indian Movies)', fontsize=16)
plt.xlabel('Rating (out of 10)', fontsize=12)
plt.ylabel('Number of Movies', fontsize=12)
plt.grid(True, alpha=0.3)
plt.show()

df['Genre'] = df['Genre'].fillna('Unknown')
df_genre = df.assign(Genre=df['Genre'].str.split(', ')).explode('Genre')
df_genre['Genre'] = df_genre['Genre'].str.strip()

genre_avg = df_genre.groupby('Genre')['Rating'].mean().sort_values(ascending=False).head(15)

plt.figure(figsize=(12, 7))
sns.barplot(x=genre_avg.values, y=genre_avg.index, palette='viridis')
plt.title('Average IMDb Rating by Genre (Top 15)', fontsize=16)
plt.xlabel('Average Rating', fontsize=12)
plt.ylabel('Genre', fontsize=12)
plt.grid(True, alpha=0.3)
plt.show()

df['Year'] = df['Year'].astype(str).str.extract(r'(\d{4})').astype(float)
year_avg = df.groupby('Year')['Rating'].mean()

plt.figure(figsize=(12, 6))
year_avg.plot(kind='line', marker='o', color='purple')
plt.title('Average IMDb Rating Over the Years', fontsize=16)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Average Rating', fontsize=12)
plt.grid(True, alpha=0.3)
plt.show()

director_avg = df.groupby('Director')['Rating'].agg(['mean', 'count'])
director_avg = director_avg[director_avg['count'] >= 5]  
top_directors = director_avg.sort_values('mean', ascending=False).head(10)

plt.figure(figsize=(10, 6))
sns.barplot(x=top_directors['mean'], y=top_directors.index, palette='magma')
plt.title('Top 10 Directors by Average IMDb Rating (min 5 movies)', fontsize=16)
plt.xlabel('Average Rating', fontsize=12)
plt.ylabel('Director', fontsize=12)
plt.grid(True, alpha=0.3)
plt.show()

print("All graphs shown! Close each window to see the next one.")