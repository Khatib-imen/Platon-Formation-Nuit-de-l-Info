from playwright.async_api import async_playwright
import asyncio

async def navigate_and_modify(url: str, actions: list):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)  # Affiche le navigateur
        page = await browser.new_page()
        await page.goto(url)

        for action in actions:
            if action["type"] == "delete_images":
                await page.evaluate("""
                    () => {
                        document.querySelectorAll('img').forEach(img => img.remove());
                    }
                """)
            elif action["type"] == "remove_words":
                words = action.get("words", [])
                for word in words:
                    await page.evaluate(f"""
                        () => {{
                            document.body.innerHTML = document.body.innerHTML.replaceAll('{word}', '');
                        }}
                    """)
            elif action["type"] == "click":
                selector = action.get("selector")
                if selector:
                    await page.click(selector)
        
        # Garde la page ouverte pour observer
        print("Actions exécutées ! La page reste ouverte.")
        await asyncio.sleep(30)
        await browser.close()
