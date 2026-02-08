sample_articles = [
    {
        "title": "Python logra nuevo exito",
        "source": {"name": "TechNews"},
        "description": "Gran noticia",
        "category": "Tecnología",
    },
    {
        "title": "Economia en crecimiento",
        "source": {"name": "FinanceDaily"},
        "description": "Buenas noticias económicas",
        "category": "Economía",
    },
    {
        "title": "Deportes al rojo vivo",
        "source": {"name": "SportsCenter"},
        "description": "Partidos emocionantes",
        "category": "Deportes",
    },
    {
        "title": "Avances en IA",
        "source": {"name": "TechNews"},
        "description": "Nuevas tecnologías",
        "category": "Tecnología",
    },
    {
        "title": "Mercados bersatiles suben",
        "source": {"name": "FinanceDaily"},
        "description": "Inversiones rentables",
        "category": "Economía",
    },
    {
        "title": "Campeonato mundial",
        "source": {"name": "SportsCenter"},
        "description": "Evento deportivo global",
        "category": "Deportes",
    },
]


def extract_titles_traditional(articles):
    """Extrae solo los titulos usando un for - Extracts only titles using a for loop."""
    titles = []
    for article in articles:
        titles.append(article["title"])
        if len(article["title"]) > 10:
            titles.append(article["title"])
    return titles


def extract_titles(articles):
    """extrae solo los titulos usando un comprehension - extracts only titles using a comprehension."""
    return [article["title"] for article in articles if len(article["title"]) > 10]


def extract_article_summaries(articles):
    """Extrae resúmenes de artículos - Extracts article summaries."""
    return {
        article["title"]: article["description"]
        for article in articles
        if len(article["description"]) > 20
    }


def extract_sources_traditional(articles):
    """Extrae fuentes unicas usando un for - Extracts unique sources using a for loop."""
    sources = set()
    for article in articles:
        sources.add(article["source"]["name"])
    return list(sources)


def extract_sources(articles):
    """Extrae fuentes unicas usando un set comprehension - Extracts unique sources using a set comprehension."""
    return list({article["source"]["name"] for article in articles})


def categorize_traditional(articles):
    """Categoriza artículos usando un for - Categorizes articles using a for loop."""
    sources = extract_sources(articles)
    result = {
        # KEY: category, VALUE: list of article titles
    }
    for source in sources:
        if source not in result:
            result[source] = []
        for article in articles:
            if source == article["source"]["name"]:
                result[source].append(article["title"])
    return result


def categorize(articles):
    """Categoriza artículos usando un dict comprehension - Categorizes articles using a dict comprehension."""
    sources = extract_sources(articles)
    return {
        source: [
            article["title"]
            for article in articles
            if source == article["source"]["name"]
        ]
        for source in sources
    }


# print(extract_titles_traditional(sample_articles))
# print("---")
# print(extract_titles(sample_articles))


# print(extract_article_summaries(sample_articles))

# print(extract_sources_traditional(sample_articles))
# print("---")
# print(extract_sources(sample_articles))

print(categorize_traditional(sample_articles))
print("---")
print(categorize(sample_articles))
