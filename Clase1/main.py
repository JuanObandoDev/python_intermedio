# main.py - Todo el código es un archivo - All code is in one file
"""
sistema de analisis de noticias con APIs multiples - System of news analysis with multiple APIs
"""

# PEP 8: configuracion centralizada - constantes en MAYUSUCLAS con guiones bajos - central configuration - constants in UPPERCASE with underscores
API_TIMEOUT = 30
MAX_ATTEMPTS = 3
DEFAULT_LANGUAGE = (
    "es"  # PEP 8: Comillas dobles para strings - Double quotes for strings
)


# PEP 8: Utilidades comunes del proyecto - funciones en snake_case - Common utilities of the project - functions in snake_case
def clean_text(text):
    # PEP 8: 4 espacios por identacion, no tabs - 4 spaces per indentation, no tabs
    """Limpia y normaliza el texto. - Cleans and normalizes text."""
    if not text:
        return ""
    return text.strip().lower()


# PEP 8: Doble linea en blanco entre funciones para separar logicamente - Double blank line between functions to logically separate
def validate_api_key(api_key):
    """Valida que la API key tenga formato correcto. - Validates that the API key has correct format."""
    return len(api_key) > 10 and api_key.isalnum()


# PEP 8: Funciones principales - argupada despues de utilidades - Main functions - grouped after utilities
def fetch_news_from_api(api_name, query):
    """Obtiene noticias de una API específica. - Fetches news from a specific API."""
    pass


def process_article_data(raw_data):
    """Procesa datos crudos de articulos. - Processes raw article data."""
    pass


# Longitud de linea: maximo 88 caracteres (Ruff default) - Line length: maximum 88 characters (Ruff default)
# Identacion: 4 espacions, nunca tabs - Indentation: 4 spaces, never tabs
# Nombres descriptivos: snake:case para funciones y variables - Descriptive names: snake_case for functions and variables
# Imports ordenados: estandar → terceros → locales - Ordered imports: standard → third-party → local
# Lineas en blanco: separar funciones y clases logicamente - Blank lines: logically separate functions and classes
# Comillas consistentes: usar comillas dobles para strings - Consistent quotes: use double quotes for strings


# def ejemplo_args(*args):
#     """Ejemplo de función con argumentos variables. - Example of function with variable arguments."""
#     print(f"TODOS {args}")


# ejemplo_args(1, 2, 3, "cuatro", "cinco")
# ejemplo_args("noticia1", "noticia2", "noticia3")
# ejemplo_args()


# def ejemplo_kwargs(**kwargs):
#     """Ejemplo de función con argumentos keyword variables. - Example of function with variable keyword arguments."""
#     print(f"kwargs type {type(kwargs)}")
#     print(f"kwargs {kwargs}")


# ejemplo_kwargs(api_key="1234567890abcdef", timeout=20, attempts=5)
# ejemplo_kwargs(section="technology", from_date="2026-01-01")
# ejemplo_kwargs()


import json
import os
import urllib.parse
import urllib.request

from dotenv import load_dotenv

load_dotenv(
    dotenv_path=os.path.join(os.path.dirname(__file__), "..", ".env")
)  # Carga variables de entorno desde .env - Load environment variables from .env

API_KEY = os.getenv(
    "API_KEY"
)  # PEP 8: Variables de entorno en mayusculas - Environment variables in uppercase

BASE_URL = os.getenv(
    "BASE_URL"
)  # PEP 8: Variables de entorno en mayusculas - Environment variables in uppercase


class NewsSystemError(Exception):
    """Excepción personalizada para errores del sistema de noticias."""

    pass


class APIKeyError(NewsSystemError):
    """Excepción personalizada para errores de API key."""

    pass


def newsapi_client(api_key, query, timeout=30, attempts=3):
    """Cliente para NewsAPI. - Client for NewsAPI."""
    query_string = urllib.parse.urlencode({"q": query, "apiKey": api_key})
    url = f"{BASE_URL}?{query_string}"

    try:
        with urllib.request.urlopen(url, timeout=timeout) as response:
            data = response.read().decode("utf-8")
            return json.loads(data)
    except urllib.error.URLError:
        raise APIKeyError("Error de conexión a la API.")

    return f"NewsAPI: {query} (timeout={timeout}, attempts={attempts})"


def guardian_client(api_key, section, from_date, timeout=30, attempts=3):
    """Cliente para The Guardian API. - Client for The Guardian API."""
    return f"The Guardian: {section} (from={from_date}, timeout={timeout}, attempts={attempts})"


def fetch_news(api_name, *args, **kwargs):
    """Función flexible para conectar con la API. - Flexible function to connect with the API."""
    base_config = {
        "timeout": API_TIMEOUT,
        "attempts": MAX_ATTEMPTS,
    }

    config = {
        **base_config,  # PEP 8: Uso de ** para combinar diccionarios - Use of ** to combine dictionaries
        **kwargs,  # Sobrescribe configuracion base con kwargs - Override base configuration with kwargs
    }

    api_clients = {
        "newsapi": newsapi_client,
        "guardian": guardian_client,
    }

    try:
        client = api_clients[api_name]
        return client(*args, **config)
    except KeyError:
        print("Error: API no soportada.")
        return {"articles": []}
    except Exception as exc:
        print(f"Error inesperado: {exc}")
        return {"articles": []}
    finally:
        print("Finalizando solicitud a la API.")


response_data = None
try:
    response_data = fetch_news("newsapi", api_key=API_KEY, query="Python")
except APIKeyError as api_exc:
    print(f"Error de API key: {api_exc}")

if response_data:
    for article in response_data["articles"]:
        print(f"Title: {article['title']}")
