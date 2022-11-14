from tech_news.database import search_news
from datetime import datetime


# Requisito 6
def search_by_title(title):
    query = {"title": {"$regex": title, "$options": "i"}}
    news_found = search_news(query)
    titles_and_urls = [(new['title'], new['url'])for new in news_found]
    return titles_and_urls


# Requisito 7
def search_by_date(date):
    try:
        formated_data = datetime.fromisoformat(date).strftime("%d/%m/%Y")
        query = {"timestamp": formated_data}
        news_found = search_news(query)
        titles_and_urls = [(new['title'], new['url'])for new in news_found]
        return titles_and_urls
    except ValueError:
        raise ValueError('Data inválida')


# Requisito 8
def search_by_tag(tag):
    query = {"tags": {"$regex": tag, "$options": "i"}}
    news_found = search_news(query)
    titles_and_urls = [(new['title'], new['url'])for new in news_found]
    return titles_and_urls


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
