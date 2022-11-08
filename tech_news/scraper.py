# Requisito 1
import requests
from time import sleep
from parsel import Selector


def fetch(url, wait: int = 3):
    try:
        headers = {"user-agent": "Fake user-agent"}
        response = requests.get(url, timeout=wait, headers=headers)
        sleep(1)
        response.raise_for_status()
    except (requests.HTTPError, requests.ReadTimeout):
        return None
    return response.text


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(html_content)
    urls = []
    for article in selector.css(".cs-overlay-link"):
        link = article.css("a::attr(href)").get()
        urls.append(link)
    return urls


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(html_content)
    next_page_url = selector.css(".next.page-numbers::attr(href)").get()
    if not next_page_url:
        return None
    return next_page_url


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
