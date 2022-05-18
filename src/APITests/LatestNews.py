import  requests

r = requests.get("https://newsapi.org/v2/everything?qInTitle=stock%20market&from=2022-5-05&to=2022-5-15&sortBy=popularity&language=en&apiKey=890603a55bfa47048e4490069ebee18c")

content = r.json()
print(content['articles'][1]["title"])