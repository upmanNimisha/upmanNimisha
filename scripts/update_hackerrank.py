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

print("Status:", response.status_code)
print("Page length:", len(response.text))

html = response.text

soup = BeautifulSoup(html, "html.parser")

print("\n" + "=" * 60)
print("HACKERRANK PROFILE DATA")
print("=" * 60)

# --------------------------------------------------
# Find Badges section
# --------------------------------------------------

badges_section = soup.select_one(".hacker-badges")

if badges_section:
    print("\n✅ Badges section found!")

    print("\nVisible badge text:")
    print("-" * 60)

    text = badges_section.get_text(" ", strip=True)

    print(text[:5000])

else:
    print("\n❌ Badges section not found")


# --------------------------------------------------
# Find individual badges
# --------------------------------------------------

print("\n" + "=" * 60)
print("INDIVIDUAL BADGES")
print("=" * 60)

badges = soup.select(".hacker-badge")

print("Number of badge elements:", len(badges))

for i, badge in enumerate(badges, 1):

    text = badge.get_text(" ", strip=True)

    print(f"\nBadge {i}:")
    print(text)


# --------------------------------------------------
# Save HTML
# --------------------------------------------------

with open("hackerrank_page.html", "w", encoding="utf-8") as f:
    f.write(html)

print("\nHTML saved successfully.")
