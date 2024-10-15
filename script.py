import requests
from bs4 import BeautifulSoup
# Print a greeting message
print("Hi")
# Send a GET request to ResearchGate
# url = "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8499625/"
# url = "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9971900/"

urls = ["https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10585315/", "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8499625/", "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7524012/", "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9971900/", "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10558031/"]


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}

allAbstracts = []
keywords = "mitigation"




for index, url in enumerate(urls):
    try:
        # Send the request
        page_to_scrape = requests.get(url, headers=headers, timeout=5)
        # Check if the request was successful
        page_to_scrape.raise_for_status()  # Raises an HTTPError for bad responses (4xx, 5xx)
        # Parse the content of the page
        soup = BeautifulSoup(page_to_scrape.content, 'html.parser')

        all_tags = soup.findAll(['h2', 'p'])
        
        for tag in all_tags: 
            # print(f"index: {index}")
            # print("tag:", tag)
            # print("attr:", tag.attrs)

            if "Abstract" in tag.getText():
                # print("Abstract", tag) 
                abstractP = index+1
                allAbstracts.append(all_tags[abstractP].getText())
                print(all_tags[abstractP].getText())



        #     # Print all <div> elements (for debugging)
        #     # CHECK CLASSES
        #     if 'class' in div.attrs:
        #         class_given = div.attrs['class']
        #         # print("class:", class_given)
                

        #     # CHECK IDs
        #     if 'id' in div.attrs:
        #         id_given = div.attrs['id']
        #         # print("id:", id_given)
            
            
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.ConnectionError as conn_err:
        print(f"Connection error occurred: {conn_err}")
    except requests.exceptions.Timeout as timeout_err:
        print(f"Timeout error occurred: {timeout_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Error occurred: {req_err}")



print(f"all abstracts: {allAbstracts}")

# for abstract in allAbstracts:
#     if keywords in abstract:
#         print(f"{keywords} is in {abstract}")