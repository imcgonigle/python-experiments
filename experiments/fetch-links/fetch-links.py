import requests
from bs4 import BeautifulSoup
import pandas as pd

def extract_links(url):
    # Fetch the content of the URL
    response = requests.get(url)
    if response.status_code != 200:
        print("Failed to retrieve the webpage. Status code:", response.status_code)
        return

    # Parse the webpage content
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract all the links
    links = []
    for link in soup.find_all('a'):
        text = link.get_text(strip=True)
        href = link.get('href')
        target = link.get('target', '')  # Some links may not have a target attribute
        links.append({'Text': text, 'URL': href, 'Target': target})

    # Create a DataFrame for better readability
    df = pd.DataFrame(links)

    # Print the table
    print(df.to_string(index=False))
    
# Example usage
url = "https://ianmcgonigle.com"  # Replace with your desired URL
extract_links(url)

