import requests
from bs4 import BeautifulSoup
import pandas as pd
import xml.etree.ElementTree as ET
import time
import random
import argparse

# Configure argparse for user input, including sitemap URL and output file
parser = argparse.ArgumentParser(description='Fetch titles from sitemaps.')
parser.add_argument('--sitemap', type=str, required=True, help='The URL of the sitemap to fetch from')  # Sitemap URL
parser.add_argument('--count', type=int, default=10, help='Number of URLs to fetch (default is 10)')  # Number of URLs
parser.add_argument('--all', action='store_true', help='Fetch all URLs from the sitemap')  # Fetch all URLs
parser.add_argument('--output', type=str, default='sitemap_titles', help='Output file name without extension (default is "sitemap_titles")')  # Output file name
args = parser.parse_args()

# Download and parse the sitemap
sitemap_url = args.sitemap
response = requests.get(sitemap_url)
sitemap_content = response.content

# Extract all URLs from the sitemap
root = ET.fromstring(sitemap_content)
namespaces = {'ns': 'http://www.sitemaps.org/schemas/sitemap/0.9'}

urls = [url.find('ns:loc', namespaces).text for url in root.findall('ns:url', namespaces)]
total_urls = len(urls)

# Determine how many URLs to fetch based on user input
if args.all:
    url_count = total_urls  # Fetch all URLs if --all is specified
else:
    url_count = min(args.count, total_urls)  # Fetch a limited number, based on --count

# Display the total number of URLs and how many will be fetched
print(f"Total number of URLs in the sitemap: {total_urls}")
print(f"Number of URLs to fetch: {url_count}")

# Collect titles and URLs in a list
data = []

for index, url in enumerate(urls[:url_count], start=1):  # Fetch only the specified number of URLs
    print(f"Fetching: {url} ({index} of {url_count})")
    page_response = requests.get(url)
    soup = BeautifulSoup(page_response.content, 'html.parser')
    
    # Get the page title
    title = soup.title.string if soup.title else 'No title'
    
    # Create Site Title and Page Title
    site_title = title
    page_title = title.split('|')[0].strip()  # Remove everything after "|"
    
    print(f"Site Title: {site_title}")
    print(f"Page Title: {page_title}")
    
    # Add to data
    data.append({'URL': url, 'Site Title': site_title, 'Page Title': page_title})
    
    # Delay between each request (0–0.5 seconds)
    sleep_time = random.uniform(0, 0.5)
    print(f"Waiting {sleep_time:.2f} seconds before the next request...\n")
    time.sleep(sleep_time)

# Create a DataFrame
df = pd.DataFrame(data)

# Save as Excel and CSV using the specified output file name
output_file = args.output
df.to_excel(f'{output_file}.xlsx', index=False)
df.to_csv(f'{output_file}.csv', index=False)

print(f"Excel and CSV files with page titles and URLs have been created as '{output_file}.xlsx' and '{output_file}.csv'!")