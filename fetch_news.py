import requests 
import mysql.connector
import os 
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

# The API endpoint
url = "https://hn.algolia.com/api/v1/search"  

# Sends our search parameters
params = {
    "query": "AI",
    "tags": "story",
    "hitsPerPage": 20
}

# the requests.get sends an HTTP GET request
# Stores the server's response
response = requests.get(url, params=params, timeout=20)

print("Status code:", response.status_code)

data = response.json()
articles = data["hits"]
print("Articles retrieved:", len(articles))

for article in articles[:5]:
    print("\nTitle:", article["title"])
    print("Author:", article["author"])
    print("Points:", article["points"])
    print("Comments:", article["num_comments"])
    print("URL:", article["url"])
    print("Created at:", article["created_at"])


# Connect to MariaDB
connection = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    port=int(os.getenv("DB_PORT")),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME")
)

insert_query = """
INSERT INTO articles (
    article_id,
    title,
    author,
    points,
    comments,
    url,
    created_at
)
VALUES (%s, %s, %s, %s, %s, %s, %s)
ON DUPLICATE KEY UPDATE
    title = VALUES(title),
    author = VALUES(author),
    points = VALUES(points),
    comments = VALUES(comments),
    url = VALUES(url),
    created_at = VALUES(created_at)
"""

cursor = connection.cursor()

for article in articles:
    article_data = (
        article["objectID"],
        article["title"],
        article["author"],
        article["points"],
        article["num_comments"],
        article["url"],
        datetime.fromisoformat(
            article["created_at"].replace("Z", "+00:00")
        ).replace(tzinfo=None)
    )

    cursor.execute(insert_query, article_data)


    # Save changes to the database
connection.commit()

# Close the cursor and database connection
cursor.close()
connection.close()

print("Articles successfully saved to MariaDB!")