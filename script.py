import requests
from bs4 import BeautifulSoup
import pandas as pd  

# Print a greeting message
print("Hi")
# Send a GET request to ResearchGate
# url = "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8499625/"
# url = "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9971900/"

urls = ["https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10585315/", "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8499625/", "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7524012/", "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9971900/", "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10558031/"]


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}

keywords = ["mitigate", "climate anxiety", "climate change", "mental health", "global warming"]
allData = []

for url in urls:
    try:
        # Send the request
        page_to_scrape = requests.get(url, headers=headers, timeout=5)
        # Check if the request was successful
        page_to_scrape.raise_for_status()  # Raises an HTTPError for bad responses (4xx, 5xx)
        # Parse the content of the page
        soup = BeautifulSoup(page_to_scrape.content, 'html.parser')
                
        h2_tags = soup.find_all("h2")
        abstract = ""
        currentData = [url]

        for tag in h2_tags: 
            if tag.get_text(strip=True) == "Abstract" or tag.get_text(strip=True) == "Summary":
                # print("Yes - Abstract or Summary found")
                parent_div = tag.find_parent("div")
                text = ""

                if parent_div:
                    paragraphs = parent_div.find_all("p")

                    for paragraph in paragraphs: 
                        text += " " + paragraph.getText(strip=True)
                    abstract += " " + text
                
            #     else:
            #         print("doesnt contain parent div")
            
            # else:
            #     print(f"doesnt contain Abstract or Summary")
        
        for keyword in keywords: 

            if keyword.lower() in abstract.lower():
                # print(f"{keyword} is in abstract")
                currentData.append("yes")

            else: 
                # print(f"{keyword} is not in abstract")
                currentData.append("no")

        currentData.append(abstract)
        allData.append(currentData)
        # print(f"currentData: {currentData}")

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


# print(f"all data: {allData}")
 
# Create the pandas DataFrame 
df = pd.DataFrame(allData, columns = ["url", "mitigate", "climate anxiety", "climate change", "mental health", "global warming", "Abstract Text"]) 

# Dataframe to CSV
df.to_csv('abstracts.csv', index=False)