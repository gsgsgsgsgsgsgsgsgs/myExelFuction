import requests
from bs4 import BeautifulSoup
import pandas as pd

def search_google(query, num_results):
    search_url = f"https://www.google.com/search?q={query}&num={num_results}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    response = requests.get(search_url, headers=headers, verify=False)

    if response.status_code != 200:
        raise Exception("Failed to retrieve search results")
    return response.text

def extract_links(html):
    soup = BeautifulSoup(html, 'html.parser')
    links = []
    for item in soup.find_all('div', attrs={'class': 'g'}):
        link = item.find('a', href=True)
        if link:
            links.append(link['href'])
    return links

def find_phrase_in_pages(links, phrase):
    data = []
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    for link in links:
        try:
            response = requests.get(link, headers=headers)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                post_content = soup.find('div', class_='post-content')  # Adjust class name based on actual HTML structure
                if post_content:
                    post_text = post_content.get_text().strip()
                    author = soup.find('div', class_='author').get_text().strip()  # Adjust class name for author
                    data.append({'Post': post_text, 'Author': author, 'Link': link})
        except requests.RequestException as e:
            print(f"Failed to retrieve {link}: {e}")
    return data

def save_to_excel(data, filename):
    df = pd.DataFrame(data)
    df.to_excel(filename, index=False)

if __name__ == "__main__":
    query = "אובחנתי בפוסט טראומה"
    num_results = 10  # Number of search results to retrieve
    html = search_google(query, num_results)
    links = extract_links(html)
    data = find_phrase_in_pages(links, query)
    save_to_excel(data, 'posts_data.xlsx')
