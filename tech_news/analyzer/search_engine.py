from tech_news.database import search_news


# Requisito 6
def search_by_title(title):
    query = {"title": {"$regex": title, "$options": "i"}}
    news_found = search_news(query)
    title_and_urls = [(new['title'], new['url'])for new in news_found]
    return title_and_urls


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_tag(tag):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
