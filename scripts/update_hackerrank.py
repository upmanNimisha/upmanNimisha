
import requests

url = "https://www.hackerrank.com/profile/upman_mat"

response = requests.get(
    url,
    headers={
        "User-Agent": "Mozilla/5.0"
    },
    timeout=30
)

print("Status:", response.status_code)
print("Length:", len(response.text))

with open("hackerrank_page.html", "w", encoding="utf-8") as f:
    f.write(response.text)
