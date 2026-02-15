"""
sistema de analisis de noticias con APIs multiples - System of news analysis with multiple APIs
"""

import os

from dotenv import load_dotenv

from exceptions import APIKeyError
from news_api_client import fetch_news

load_dotenv(
    dotenv_path=os.path.join(os.path.dirname(__file__), "..", ".env")
)  # Carga variables de entorno desde .env - Load environment variables from .env

API_KEY = os.getenv(
    "API_KEY"
)  # PEP 8: Variables de entorno en mayusculas - Environment variables in uppercase

response_data = None
try:
    response_data = fetch_news("newsapi", api_key=API_KEY, query="Python")
except APIKeyError as api_exc:
    print(f"Error de API key: {api_exc}")

if response_data:
    for article in response_data["articles"]:
        print(f"Title: {article['title']}")
