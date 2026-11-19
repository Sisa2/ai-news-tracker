import pandas as pd

data = {
    "title": ["AI in healthcare", "New AI model", "Future of robotics"],
    "points": [250, 180, 320]
}

df = pd.DataFrame(data)

print(df["points"])

#Print points that are greater than 200
#print(df[df["points"]>200])

#Print points on an order 
print(df.sort_values(by="points", ascending=False))