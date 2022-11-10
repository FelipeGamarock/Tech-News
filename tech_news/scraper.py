import requests
from time import sleep
from parsel import Selector
from tech_news.database import create_news


# Requisito 1
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
    selector = Selector(html_content)

    title = selector.css(".entry-title::text").get().strip()

    timestamp = selector.css("li.meta-date::text").get()

    writer = selector.css("a.url.fn.n::text").get()

    summary = selector.css(
        "div.entry-content > p:first-of-type *::text"
    ).getall()
    summary = "".join(summary).strip()

    category = selector.css(".label::text").get()

    url = selector.css("link[rel=canonical]::attr(href)").get()

    tags = selector.css(".post-tags li a::text").getall()

    list_comments = selector.css(".comment-list li").getall()
    comments_count = len(list_comments)

    new_data = {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "comments_count": comments_count,
        "summary": summary,
        "tags": tags,
        "category": category,
    }
    return new_data


# Requisito 5
def get_tech_news(amount):
    pages = amount//12
    all_urls = []

    first_page_content = fetch("https://blog.betrybe.com/")
    urls_first_page = scrape_novidades(first_page_content)
    all_urls.extend(urls_first_page)

    next_page_url = scrape_next_page_link(first_page_content)
    next_page_content = fetch(next_page_url)
    i = 0
    while i < pages:
        urls_next_page = scrape_novidades(next_page_content)
        all_urls.extend(urls_next_page)

        next_page_url = scrape_next_page_link(next_page_content)
        next_page_content = fetch(next_page_url)
        i += 1

    urls_selected = all_urls[0:amount]
    all_news = []
    for url in urls_selected:
        html_content = fetch(url)
        news = scrape_noticia(html_content)
        all_news.append(news)

    create_news(all_news)
    return all_news
