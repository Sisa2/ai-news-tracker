import pandas as pd 
import mysql.connector 
import os 
from dotenv import load_dotenv

load_dotenv()

connection = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    port=int(os.getenv("DB_PORT")),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME")
)

cursor = connection.cursor(dictionary = True)

query = "SELECT  * FROM articles"

cursor.execute(query)
rows = cursor.fetchall()

df = pd.DataFrame(rows)

# will print the first 10
#  print(df.head(10))
'''
print("DataFrame shape:", df.shape)
print("DataFrame columns:", df.columns)

# df.info()

print(df[["title", "author", "points"]])

# print(df[df["points"] > 2000])
greater_2000 = df[df["points"] > 2000]
print(greater_2000[["title", "points"]])
'''

# Sorting and cutting top 5 
sorted_articles = df.sort_values(by="points", ascending=False)
print(sorted_articles[["title", "points"]].head(5))

# Average 
average_points = df["points"].mean()
print("Average article points:", average_points)

#Total comments 
total_comments = df["comments"].sum()
print("Total comments:", total_comments)


# Most comments
most_commented = df.loc[df["comments"].idxmax()]
print("Most commented article:")
print(most_commented[["title", "author", "comments"]])

cursor.close()
connection.close()