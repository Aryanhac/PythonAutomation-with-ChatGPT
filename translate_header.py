

import requests
from bs4 import BeautifulSoup
from googletrans import Translator

# Get the webpage
url = 'https://example.com'
page = requests.get(url)

# Parse the webpage
soup = BeautifulSoup(page.content, 'html.parser')

# Extract the header elements
headers = soup.find_all('h1')

# Initialize the translator
translator = Translator()

# Translate the headers into Spanish
translated_headers = [translator.translate(header.text, dest='es').text for header in headers]

# Create an HTML file with the translated headers
with open('translated_headers.html', 'w') as f:
    f.write('<html><body>')
    for header in translated_headers:
        f.write(f'<h1>{header}</h1>')
    f.write('</body></html>')