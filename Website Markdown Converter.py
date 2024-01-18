# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 11:05:44 2023

@author: raamc
"""

import requests
from bs4 import BeautifulSoup
import markdownify

def url_to_markdown(url):
    try:
        # Fetch the website content
        response = requests.get(url)
        response.raise_for_status()

        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Convert HTML to Markdown
        markdown_text = markdownify.markdownify(str(soup), heading_style="ATX")

        return markdown_text
    except requests.RequestException as e:
        return f"Error fetching URL: {e}"

# Example usage
url = input("Enter a website URL: ")
markdown = url_to_markdown(url)
print(markdown)
