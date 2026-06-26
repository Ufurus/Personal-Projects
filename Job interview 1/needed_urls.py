import requests
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin, urlparse
urls = set()

def get_all_subpages(base_url):
    domain_name = urlparse(base_url).netloc
    try:
        response = requests.get(base_url)
        soup = bs(response.text, 'html.parser')

        for a_tag in soup.find_all("a", href=True):
            href = a_tag.get("href")
            full_url = urljoin(base_url, href).split('#')[0]
            clean_url = full_url.rstrip('/')

            if len(urls) == 3:
                break

            if (clean_url.endswith('gdp-by-country') or clean_url.endswith('world-population')
                    or clean_url.endswith('countries-of-the-world')):
                if domain_name in clean_url and clean_url not in urls:
                    urls.add(full_url)

    except Exception as e:
        print(f"Error: {e}")

    return urls

target_url = 'https://www.worldometers.info/'
all_links = get_all_subpages(target_url)

def world_population_by_country(url):
    domain_name = urlparse(url).netloc
    try:
        response = requests.get(url)
        soup = bs(response.text, 'html.parser')

        for a_tag in soup.find_all("a", href=True):
            href = a_tag.get("href")
            full_url = urljoin(url, href).split('#')[0]
            clean_url = full_url.rstrip('/')

            if clean_url not in urls:
                if clean_url.endswith('population-by-country'):
                    urls.add(full_url)

    except Exception as e:
        print(f"Error: {e}")

population_link = ''

for link in all_links:
    if 'population' in link:
        population_link = link

world_population_by_country(population_link)

print(urls)
