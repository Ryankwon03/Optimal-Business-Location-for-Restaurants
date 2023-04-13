import requests
from bs4 import BeautifulSoup
import csv

# Send a GET request to the website
page = requests.get("https://www.laalmanac.com/population/po24la_zip.php")

# Parse the HTML content of the page using BeautifulSoup
soup = BeautifulSoup(page.content, "html.parser")

# Find the table with the data and extract its headers and rows
table = soup.find("table")
headers = table.find_all("th")
rows = table.find_all("tr")

# Create a CSV file to save the data
with open("la_population.csv", "w", newline="") as f:
    writer = csv.writer(f)

    # Write the headers to the CSV file
    header_row = []
    cnt = 0
    for header in headers:
        cnt = cnt + 1
        if(header.get_text() == "Population of One Race Alone †"):
            continue
        if(cnt >= 12):
            break
        header_row.append(header.get_text(strip=True))
        print(header.get_text())
    writer.writerow(header_row)

    # Loop through each row and extract its columns
    for row in rows:
        cols = row.find_all("td")

        # Check if the row has columns (not a header or footer row)
        if len(cols) > 0:
            # Extract the text content of each column
            row_data = []
            for col in cols:
                row_data.append(col.get_text(strip=True))
            # Write the row to the CSV file
            writer.writerow(row_data)