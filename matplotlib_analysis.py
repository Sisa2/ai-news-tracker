import pandas as pd
import matplotlib.pyplot as plt
#from pandas_analysis import df
import mysql.connector
import os
from dotenv import load_dotenv

import matplotlib.pyplot as plt

from pandas_analysis import (
    top_articles,
    yearly_articles,
    monthly_popularity,
    most_commented
)



load_dotenv()

connection = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    port=int(os.getenv("DB_PORT")),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME")
)

cursor = connection.cursor(dictionary=True)

query = "SELECT * FROM articles"

cursor.execute(query)

rows = cursor.fetchall()

df = pd.DataFrame(rows)

# Basic visualisation

top_articles.plot(kind="bar", x="title", y="points")

most_commented.plot(
                    kind="barh",
                     x="title",
                     y="comments",
                     title= "Top 5 most commented AI News Articles",
                     figsize=(10, 6),
                     color="darkorange"
                    )

# Scatter Plot: Points vs Comments

df.plot(
    kind="scatter",
    x="points",
    y="comments",
    title="Relationship Between Article Points and Comments",
    figsize=(10, 6)
)



# Subplots: 

fig, ax = plt.subplots(1,2, figsize=(14,6))
plt.subplots(1,2)

df.nlargest(5, "points").plot(
    kind="bar",
    x="title",
    y="points",
    ax=ax[0],
    title="Top 5 Articles by Points",
    legend=False
)

df.nlargest(5, "comments").plot(
    kind="barh",
    x="title",
    y="comments",
    ax=ax[1],
    title="Top 5 Articles by Comments",
    legend=False
)

ax[1].annotate(
    "Highest comments",
    (most_commented.iloc[0]["comments"], 0)
)
# Horizontal line: Average number of comments
ax[1].axhline(df["comments"].mean())

# Vertical line: Average number of points
ax[1].axvline(df["points"].mean())


plt.tight_layout()
plt.show()
cursor.close()
connection.close()