import requests

url = "https://example.com/wp-json/wp/v2/posts"

response = requests.get(url)
response.raise_for_status()

data = response.json()

for item in data:
    print(f"{item['id']} - {item['title']['rendered']}")
