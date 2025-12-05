from crawl4ai import Crawl4AI
from litellm import OpenAI  # ou un autre LLM que tu utilises

c4ai = Crawl4AI()
llm = OpenAI(model="gpt-4", api_key="TON_API_KEY")  # ou Mistral, Ollama, etc.

def generate_strategy(prompt: str):
    """
    Transforme l'objectif utilisateur en instructions de scraping.
    """
    instruction = llm(f"""
    Tu es un agent de scraping intelligent. 
    Voici l'objectif : {prompt}
    Génère une stratégie claire pour Crawl4AI, avec :
    - URL à scraper
    - Données à extraire
    - Format de sortie JSON
    """)
    return instruction

def execute_strategy(strategy: str):
    """
    Exécute la stratégie via Crawl4AI.
    """
    # Ici on parse la stratégie pour récupérer l'URL et les infos
    url = strategy.split("URL:")[-1].split("\n")[0].strip()
    data = c4ai.scrape(url, export_format="json")
    return data

if __name__ == "__main__":
    prompt = input("Objectif de scraping : ")
    strategy = generate_strategy(prompt)
    print("Stratégie générée :", strategy)
    data = execute_strategy(strategy)
    print("Résultat JSON :", data)
