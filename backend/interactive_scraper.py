from playwright.async_api import async_playwright
import asyncio

async def interactive_scraper():
    url = input("Entrez l'URL à scraper : ").strip()
    if not url.startswith(("http://", "https://")):
        print("URL invalide")
        return

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)  
        page = await browser.new_page()
        await page.goto(url)
        print(f"Site chargé : {url}")

        while True:
            print("\nActions disponibles :")
            print("1 - Supprimer toutes les images")
            print("2 - Supprimer un mot spécifique")
            print("3 - Supprimer par sélecteur CSS")
            print("4 - Quitter")
            choice = input("Choisissez une action : ").strip()

            if choice == "1":
                await page.evaluate("""() => {
                    document.querySelectorAll('img').forEach(img => img.remove());
                }""")
                print("Toutes les images ont été supprimées.")

            elif choice == "2":
                word = input("Entrez le mot à supprimer : ").strip()
                if word:
                    await page.evaluate(f"""
                        () => {{
                            document.body.innerHTML = document.body.innerHTML.replaceAll('{word}', '');
                        }}
                    """)
                    print(f" Le mot '{word}' a été supprimé.")

            elif choice == "3":
                selector = input("Entrez le sélecteur CSS : ").strip()
                if selector:
                    await page.evaluate(f"""
                        () => {{
                            document.querySelectorAll('{selector}').forEach(el => el.remove());
                        }}
                    """)
                    print(f"Tous les éléments '{selector}' ont été supprimés.")

            elif choice == "4":
                print("Fin de la session.")
                break
            else:
                print("Option invalide, réessayez.")

        print("La page reste ouverte 60s pour observation...")
        await asyncio.sleep(60)
        await browser.close()

if __name__ == "__main__":
    asyncio.run(interactive_scraper())

