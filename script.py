import requests
from bs4 import BeautifulSoup
# Print a greeting message
print("Hi")
# Send a GET request to Google
url = "https://www.google.com"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}
page_to_scrape = requests.get(url, headers=headers, timeout=5)
# Check if the request was successful
if page_to_scrape.status_code == 200:
    # Parse the content of the page
    soup = BeautifulSoup(page_to_scrape.content, 'html.parser')
    # Print all <div> elements (for debugging)
    all_divs = soup.findAll("div")
    for div in all_divs:
        print(div)
        print("1")
else:
    print("Failed to retrieve the page.")