import requests
from bs4 import BeautifulSoup
import json

def scrape_page(url):
    """Récupère le HTML et toutes les images d'une page"""
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Extraire les images
    images = [{"src": img.get("src"), "alt": img.get("alt")} for img in soup.find_all("img")]
    
    return soup, images

def clean_html(soup, actions):
    """Applique des actions sur le HTML (supprimer images, textes, sections...)"""
    for action in actions:
        if action["type"] == "remove_images":
            for img in soup.find_all("img"):
                img.decompose()
        elif action["type"] == "remove_text":
            selector = action.get("selector")
            if selector:
                for tag in soup.select(selector):
                    tag.decompose()
        elif action["type"] == "remove_class":
            class_name = action.get("class_name")
            if class_name:
                for tag in soup.find_all(class_=class_name):
                    tag.decompose()
    return soup

if __name__ == "__main__":
    url = "https://www.pathe.tn/fr"

    # Exemple de prompt JSON pour l'action
    prompt_actions = [
        {"type": "remove_images"},
        {"type": "remove_class", "class_name": "header__logo"},
        {"type": "remove_text", "selector": "h1.headline"}
    ]

    # Étape 1 : Scraper la page
    soup, images = scrape_page(url)
    print("Images trouvées :", images)

    # Étape 2 : Nettoyer / modifier le HTML selon le prompt JSON
    soup_cleaned = clean_html(soup, prompt_actions)

    # Sauvegarder le HTML nettoyé
    with open("html_cleaned.html", "w", encoding="utf-8") as f:
        f.write(str(soup_cleaned))
    print("HTML nettoyé sauvegardé dans 'html_cleaned.html'")
