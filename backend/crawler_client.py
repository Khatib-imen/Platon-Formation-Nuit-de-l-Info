# backend/crawler_client.py
import asyncio
from crawl4ai import AsyncWebCrawler
import json

async def crawl_website_async(url: str):
    async with AsyncWebCrawler() as crawler:
        try:
            result = await crawler.arun(
                url=url,
                export_format="dict",   # Retourne un dict directement
                render_js=True          # ⚡ rend les sites dynamiques
            )
            # Convertir en dict pur
            if hasattr(result, "dict"):
                return result.dict()
            elif hasattr(result, "to_dict"):
                return result.to_dict()
            else:
                return dict(result)
        except Exception as e:
            return {"error": str(e)}

def crawl_website(url: str):
    """Fonction synchrone pour Flask"""
    return asyncio.run(crawl_website_async(url))
