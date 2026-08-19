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
print("Page length:", len(html))

print("\n" + "=" * 70)
print("BADGE HTML")
print("=" * 70)

badges = soup.select(".hacker-badge")

print("Number of badges:", len(badges))

for i, badge in enumerate(badges, 1):

    print("\n" + "-" * 70)
    print(f"BADGE {i}")
    print("-" * 70)

    print(badge.prettify()[:5000])


print("\n" + "=" * 70)
print("SQL RELATED IMAGES")
print("=" * 70)

images = soup.find_all("img")

for img in images:

    src = img.get("src", "")
    alt = img.get("alt", "")

    if "sql" in str(src).lower() or "sql" in str(alt).lower():

        print("\nSRC:", src)
        print("ALT:", alt)
        print("CLASS:", img.get("class"))
        print("TITLE:", img.get("title"))


with open("hackerrank_page.html", "w", encoding="utf-8") as f:
    f.write(html)

print("\nHTML saved successfully.")
