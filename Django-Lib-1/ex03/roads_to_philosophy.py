import sys
import requests
from bs4 import BeautifulSoup

def get_first_link(soup):
    content_div = soup.find(id="mw-content-text")
    for paragraph in content_div.find_all("p", recursive=False):
        for link in paragraph.find_all("a", recursive=False):
            href = link.get("href")
            if href and href.startswith("/wiki/") and not any(c in href for c in [":", "(", ")", "Help"]):
                return "https://en.wikipedia.org" + href
    return None

def follow_to_philosophy(start_url):
    visited = []
    current_url = start_url

    while True:
        if current_url in visited:
            print("It leads to an infinite loop!")
            return
        
        visited.append(current_url)
        
        response = requests.get(current_url)
        if response.status_code != 200:
            print(f"Erreur de connexion à la page : {current_url}")
            return
        
        soup = BeautifulSoup(response.content, 'html.parser')
        title = soup.find(id="firstHeading").text
        print(title)
        
        if title == "Philosophy":
            print(f"{len(visited)} roads from {visited[0]} to philosophy!")
            return
        
        first_link = get_first_link(soup)
        if not first_link:
            print("It leads to a dead end!")
            return
        
        current_url = first_link

def main():
    if len(sys.argv) != 2:
        print("Usage: python roads_to_philosophy.py <terme_de_recherche>")
        sys.exit(1)
    
    search_term = sys.argv[1].replace(" ", "_")
    start_url = f"https://en.wikipedia.org/wiki/{search_term}"
    
    try:
        follow_to_philosophy(start_url)
    except Exception as e:
        print(f"Erreur : {e}")

if __name__ == "__main__":
    main()
