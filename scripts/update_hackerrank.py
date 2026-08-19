import requests
from bs4 import BeautifulSoup

url = "https://www.hackerrank.com/profile/upman_mat"

response = requests.get(
    url,
    headers={
        "User-Agent": "Mozilla/5.0"
    },
    timeout=30
)

html = response.text
soup = BeautifulSoup(html, "html.parser")

print("Status:", response.status_code)

badges = soup.select(".hacker-badge")

print("\n" + "=" * 60)
print("DYNAMIC HACKERRANK DATA")
print("=" * 60)

for badge in badges:

    badge_box = badge.select_one(".ui-badge")

    if not badge_box:
        continue

    # Badge name
    title = badge.select_one(".badge-title")

    if title:
        name = title.get_text(strip=True)
    else:
        name = "Unknown"

    # Level
    classes = badge_box.get("class", [])

    level = "Unknown"

    for cls in classes:
        if cls.startswith("level-"):
            level = cls.replace("level-", "").capitalize()

    # Number of stars
    stars = len(badge.select(".badge-star"))

    print(f"\n{name}")
    print(f"Level : {level}")
    print(f"Stars : {stars}")

print("\n" + "=" * 60)
