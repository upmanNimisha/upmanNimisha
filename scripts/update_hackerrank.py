import requests
import re

url = "https://www.hackerrank.com/profile/upman_mat"

response = requests.get(
    url,
    headers={
        "User-Agent": "Mozilla/5.0"
    },
    timeout=30
)

print("=" * 50)
print("HACKERRANK TEST")
print("=" * 50)

print("Status Code:", response.status_code)
print("Page Length:", len(response.text))

html = response.text

# Check whether important words/data exist in the downloaded page
keywords = [
    "star",
    "stars",
    "badge",
    "badges",
    "SQL",
    "profile",
    "rating",
    "score",
    "challenge"
]

print("\nKeyword Check:")
print("-" * 50)

for keyword in keywords:
    count = len(re.findall(keyword, html, re.IGNORECASE))
    print(f"{keyword}: {count}")

print("\nFirst 1000 characters of page:")
print("-" * 50)
print(html[:1000])

# Save the complete page
with open("hackerrank_page.html", "w", encoding="utf-8") as f:
    f.write(html)

print("\nHTML file created successfully.")
print("=" * 50)
