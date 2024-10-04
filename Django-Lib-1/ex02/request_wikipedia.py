import sys
import requests
import json
import dewiki

def get_wikipedia_content(search_term):
    url = f"https://fr.wikipedia.org/w/api.php"
    params = {
        'action': 'query',
        'format': 'json',
        'prop': 'revisions',
        'titles': search_term,
        'rvprop': 'content',
        'rvslots': 'main',
        'formatversion': '2',
    }
    
    response = requests.get(url, params=params)
    
    if response.status_code != 200:
        raise ValueError("Erreur de connexion à l'API Wikipédia.")
    
    data = response.json()
    
    pages = data['query']['pages']
    if not pages or 'missing' in pages[0]:
        raise ValueError(f"Page '{search_term}' non trouvée.")
    
    content = pages[0]['revisions'][0]['slots']['main']['content']
    return dewiki.from_string(content)

def main():
    if len(sys.argv) != 2:
        print("Usage: python request_wikipedia.py <terme_de_recherche>")
        sys.exit(1)
    
    search_term = sys.argv[1].replace(" ", "_")
    try:
        content = get_wikipedia_content(search_term)
        with open(f"{search_term}.wiki", "w", encoding='utf-8') as f:
            f.write(content)
        print(f"Le contenu a été écrit dans {search_term}.wiki.")
    except Exception as e:
        print(f"Erreur : {e}")

if __name__ == "__main__":
    main()
