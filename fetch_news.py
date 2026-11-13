import requests 

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