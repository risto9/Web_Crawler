import requests
from bs4 import BeautifulSoup
import os

def get_news():
    url = "https://news.ycombinator.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    headlines = soup.find_all("a", class_=None)
    filtered_headlines = []
    for link in headlines:
        parent = link.find_parent("td", class_="title")
        if parent:
            filtered_headlines.append(link)

    news = []
    for headline in filtered_headlines:
        news.append({
            "title": headline.get_text(),
            "link": headline.get("href")
        })

    return news

def save_to_readme(news_items, file_path):
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write("# Hacker News Headlines\n\n")
        f.write("Here are the latest headlines from Hacker News:\n\n")
        for item in news_items:
            f.write(f"- [{item['title']}]({item['link']})\n")

    print(f"README.md file has been created at {file_path}")

    # Отворање на README фајлот откако ќе биде создаден
    os.startfile(file_path)

news_items = get_news()
file_path = "C:/Users/rpaun/OneDrive/Десктоп/README.md"
save_to_readme(news_items, file_path)
