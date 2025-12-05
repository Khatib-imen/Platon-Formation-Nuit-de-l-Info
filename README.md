🕷️ Smart Web Automation Agent
Scraping + Compréhension d’Objectif + Actions Réelles en Temps Réel
<p align="center"> <img src="https://img.shields.io/badge/AI-Agent-black?style=for-the-badge"/> <img src="https://img.shields.io/badge/DeepSeek-Powered-blue?style=for-the-badge"/> <img src="https://img.shields.io/badge/Web_Automation-Active-green?style=for-the-badge"/> </p>
🌐 Description du Projet

Smart Web Automation Agent est un agent IA capable de :

🔍 Scraper automatiquement n’importe quel site web
🧠 Comprendre l’objectif d’un utilisateur en langage naturel
🕹️ Exécuter des actions réelles en temps réel sur le site via une extension navigateur
⚙️ Identifier dynamiquement les sélecteurs CSS correspondants
🎥 Afficher les résultats en démo live dans l'interface UI

Le tout sans règles codées manuellement :
➡️ C’est l’IA qui décide comment atteindre l’objectif.

🚀 Fonctionnalités Principales
✔️ 1. Scraper un site web

Entrer une URL

Extraction automatique du HTML complet

Nettoyage intelligent

Prévisualisation instantanée dans l’UI

✔️ 2. Compréhension intelligente d’objectif utilisateur

L’agent comprend ce que vous voulez faire :

Exemples :

“Supprimer toutes les images de chaussures”

“Effacer le mot promo”

“Retirer la phrase Nouveau produit”

“Masquer la bannière rouge”

“Enlever le footer”

“Supprimer les publicités”

L’IA extrait automatiquement :

🎯 L’intention réelle

🧩 Les éléments concernés

🧷 Les sélecteurs CSS

⚡ Le plan d’action

✔️ 3. Exécution en temps réel sur le site

Grâce à l’extension navigateur, l’agent peut :

🖼️ Supprimer des images spécifiques

📝 Retirer un mot ou une phrase partout sur la page

🎨 Modifier styles / couleurs / structure

🗑️ Masquer div, sections, menus, pub

🧱 Reorganiser des blocs

➡️ Le tout visible instantanément dans la fenêtre du navigateur.

🧠 Technologies Utilisées
🖥️ Backend

Python 3.12

Flask (API backend)

BeautifulSoup4 (analyse HTML)

requests

python-dotenv

🌐 IA / LLM

DeepSeek V3.1 Terminus via API

from openai import OpenAI
client = OpenAI(base_url="...", api_key="...")

🎨 Frontend

HTML / JavaScript vanilla

Interface utilisateur simple et légère

🧩 Extension Navigateur

Chrome Extension

Exécution directe des actions → DOM manipulé en live

🛠️ Installation & Exécution
📥 1. Cloner le projet
git clone https://github.com/Khatib-imen/Smart_Web_Automation_Agent.git
cd Smart_Web_Automation_Agent

🧬 2. Créer et activer l’environnement virtuel
Windows
python -m venv .venv
.venv\Scripts\activate

Mac / Linux
python3 -m venv .venv
source .venv/bin/activate

📦 3. Installer les dépendances
pip install flask requests beautifulsoup4 python-dotenv


Optionnel selon versions :

pip install openai selenium webdriver-manager

🔐 4. Créer votre fichier .env

À la racine du projet :

DEEPSEEK_API_KEY=VOTRE_CLE
DEEPSEEK_BASE_URL=VOTRE_URL


⚠️ Ne jamais pousser .env sur GitHub

▶️ 5. Lancer l’application
python app.py


Accéder à l’interface :

👉 http://127.0.0.1:5000/

🧩 6. (Optionnel) Installer l’extension Chrome

Aller dans chrome://extensions

Activer Mode développeur

Cliquer Charger l’extension non empaquetée

Choisir :

Smart_Web_Automation_Agent/extension/


➡️ L’agent pourra désormais modifier des sites réels en direct.

🎬 Démo : Captures d'Écran
🖼️ Étape 1 — Scraping du site

(Insérer capture ici)

🧠 Étape 2 — Saisie de l’objectif utilisateur

(Insérer capture ici)

⚡ Étape 3 — L’agent comprend → exécute l’action en temps réel

(Insérer capture ici)

🎯 Conclusion

Avec Smart Web Automation Agent, vous pouvez :

modifier n’importe quel site en temps réel

scraper automatiquement

formuler des actions en langage naturel

laisser l’IA transformer l’interface selon vos besoins

💡 Un agent polyvalent pour le scraping, l’automatisation web et l’édition intelligente.
