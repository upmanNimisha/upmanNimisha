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

html = response.text

print("Status:", response.status_code)
print("Length:", len(html))

# Find useful sections around words related to profile stats
keywords = [
    "starRating",
    "star_rating",
    "stars",
    "badge",
    "badges",
    "solved",
    "problemSolved",
    "challengesSolved",
    "score",
    "rating"
]

for keyword in keywords:
    print("\n" + "=" * 70)
    print("SEARCHING:", keyword)
    print("=" * 70)

    matches = list(re.finditer(keyword, html, re.IGNORECASE))

    print("Matches:", len(matches))

    # Show first 3 useful contexts
    for match in matches[:3]:
        start = max(0, match.start() - 300)
        end = min(len(html), match.end() + 500)

        print("\n--- MATCH ---")
        print(html[start:end])

with open("hackerrank_page.html", "w", encoding="utf-8") as f:
    f.write(html)
