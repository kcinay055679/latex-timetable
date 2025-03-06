from bs4 import BeautifulSoup

# Suppose your HTML is stored in a file called "input.html"
with open("index.html", "r", encoding="utf-8") as f:
    html_content = f.read()

soup = BeautifulSoup(html_content, 'html.parser')

# Find the table body and iterate through each row
tbody = soup.find("tbody")
with open("output.txt", "w", encoding="utf-8") as outfile:
    for row in tbody.find_all("tr"):
        cells = row.find_all("td")
        # Ensure that there are at least two cells for first and last names
        if len(cells) >= 2:
            first_name = cells[0].get_text(strip=True)
            last_name = cells[1].get_text(strip=True)
            outfile.write(f"{first_name} {last_name}\n")