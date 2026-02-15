from sample_data import sample_articles

counter = 1
for article in sample_articles:
    print(f"{counter}: {article}")
    counter += 1


sample_articles_enum = enumerate(
    sample_articles, start=1
)  # Devuelve un iterador de tuplas (index, article) - Returns an iterator of tuples (index, article)

for article in sample_articles_enum:
    print(article)
