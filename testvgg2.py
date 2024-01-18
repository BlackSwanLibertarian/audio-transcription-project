import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    try:
        # Send a request to the URL
        response = requests.get(url)

        # Check if the request was successful
        if response.status_code == 200:
            # Parse the content of the page
            soup = BeautifulSoup(response.content, 'html.parser')

            # Extract and print the text of all paragraphs
            for paragraph in soup.find_all('p'):
                print(paragraph.get_text())
        else:
            print(f"Error: Unable to access the page. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
url = 'https://bounded-regret.ghost.io/emergent-deception-optimization/'  # Replace with the desired URL
scrape_website(url)
