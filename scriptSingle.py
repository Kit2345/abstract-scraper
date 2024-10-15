import requests
from bs4 import BeautifulSoup
# Print a greeting message
print("Hi")
# Send a GET request to ResearchGate
url = "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8499625/"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}

allAbstracts = []
keywords = "mitigation"

try:
        # Send the request
        page_to_scrape = requests.get(url, headers=headers, timeout=5)
        # Check if the request was successful
        page_to_scrape.raise_for_status()  # Raises an HTTPError for bad responses (4xx, 5xx)
        # Parse the content of the page
        soup = BeautifulSoup(page_to_scrape.content, 'html.parser')

        h2_tags = soup.find("h2")

        allAbstracts = []

        for tag in h2_tags: 
            if tag.getText() in ["Abstract", "Summary"]:
                parent_div = tag.findParent("div")

                if parent_div:
                    text = parent_div.getText()
                    allAbstracts.append(text)


except requests.exceptions.HTTPError as http_err:
    print(f"HTTP error occurred: {http_err}")
except requests.exceptions.ConnectionError as conn_err:
    print(f"Connection error occurred: {conn_err}")
except requests.exceptions.Timeout as timeout_err:
    print(f"Timeout error occurred: {timeout_err}")
except requests.exceptions.RequestException as req_err:
    print(f"Error occurred: {req_err}")