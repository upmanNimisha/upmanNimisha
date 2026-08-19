import requests
from bs4 import BeautifulSoup
from html import escape


# --------------------------------------------------
# 1. HackerRank profile
# --------------------------------------------------

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


# --------------------------------------------------
# 2. Extract badges
# --------------------------------------------------

badges = soup.select(".hacker-badge")

hackerrank_data = []

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

    # Make SQL display as SQL instead of Sql
    if name.lower() == "sql":
        name = "SQL"

    # Badge level
    classes = badge_box.get("class", [])

    level = "Unknown"

    for cls in classes:
        if cls.startswith("level-"):
            level = cls.replace("level-", "").capitalize()

    # Number of stars
    stars = len(badge.select(".badge-star"))

    hackerrank_data.append({
        "name": name,
        "level": level,
        "stars": stars
    })


# --------------------------------------------------
# 3. Print extracted data
# --------------------------------------------------

print("\n" + "=" * 60)
print("DYNAMIC HACKERRANK DATA")
print("=" * 60)

for badge in hackerrank_data:

    print(f"\n{badge['name']}")
    print(f"Level : {badge['level']}")
    print(f"Stars : {badge['stars']}")

print("\n" + "=" * 60)


# --------------------------------------------------
# 4. Generate SVG
# --------------------------------------------------

width = 700
row_height = 90
header_height = 90

height = header_height + (len(hackerrank_data) * row_height) + 30


svg = f'''<svg xmlns="http://www.w3.org/2000/svg"
width="{width}"
height="{height}"
viewBox="0 0 {width} {height}">

<rect width="100%" height="100%" rx="20"
      fill="#0d1117"
      stroke="#30363d"
      stroke-width="2"/>

<!-- Header -->

<text x="40" y="50"
      font-family="Arial, sans-serif"
      font-size="28"
      font-weight="bold"
      fill="#ffffff">
    HackerRank Journey
</text>
'''


# --------------------------------------------------
# 5. Add each badge to SVG
# --------------------------------------------------

for i, badge in enumerate(hackerrank_data):

    y = header_height + (i * row_height)

    name = escape(badge["name"])
    level = escape(badge["level"])
    stars = badge["stars"]

    star_text = "★" * stars

    svg += f'''
    <!-- Badge {i + 1} -->

    <text x="40" y="{y + 30}"
          font-family="Arial, sans-serif"
          font-size="20"
          font-weight="bold"
          fill="#ffffff">
        {name}
    </text>

    <text x="250" y="{y + 30}"
          font-family="Arial, sans-serif"
          font-size="22"
          fill="#f0c419">
        {star_text}
    </text>

    <text x="250" y="{y + 58}"
          font-family="Arial, sans-serif"
          font-size="15"
          fill="#8b949e">
        {level}
    </text>
    '''


# --------------------------------------------------
# 6. Close SVG
# --------------------------------------------------

svg += """
</svg>
"""


# --------------------------------------------------
# 7. Save SVG
# --------------------------------------------------

output_file = "assets/hackerrank.svg"

with open(output_file, "w", encoding="utf-8") as file:
    file.write(svg)

print(f"\nSVG generated successfully: {output_file}")
