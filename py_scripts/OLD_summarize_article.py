import random
import requests
from bs4 import BeautifulSoup

# for testing url headers:
# url = "http://httpbin.org/headers"

# target urls that work
# url = "https://www.darkreading.com/risk/access-control-gap-microsoft-active-directory-enterprise-attack-surface"

# target urls that don't work
# url = "https://www.cnn.com/2023/03/14/politics/us-drone-russian-jet-black-sea/index.html"
# url = "https://www.darkreading.com/risk/access-control-gap-microsoft-active-directory-enterprise-attack-surface"
# url = "https://www.darkreading.com/vulnerabilities-threats/microsoft-zero-day-bugs-security-feature-bypass"
url = "https://www.cnbc.com/2023/03/16/ukraine-war-live-updates-latest-news-on-russia-and-the-war-in-ukraine.html"

# list of user agent headers used to trick web-scraping detectors
user_agents_list = [
    'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.83 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36',
    'Mozilla/5.0 (iPhone12,1; U; CPU iPhone OS 13_0 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Mobile/15E148 Safari/602.1',
    'Mozilla/5.0 (iPhone14,3; U; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Mobile/19A346 Safari/602.1',
    'Mozilla/5.0 (Linux; Android 7.0; Pixel C Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/52.0.2743.98 Safari/537.36'
]


def extract_article_text(url):

    response = requests.get(url, headers={'User-Agent': random.choice(user_agents_list)})
    if response.status_code != 200:
        print(f"Failed to retrieve page: {response.status_code}")
        exit()
    # more you can print to test code:
    # response.text

    soup = BeautifulSoup(response.content, "html.parser")
    if soup is None:
        print("Failed to parse HTML content")
        exit()

    # article_content = soup.find("div", class_="entry-content")
    # if article_content is None:
    #     print("Failed to find article content")
    #     exit()

    # for paragraph in article_content.find_all("p"):
    #     print(paragraph.get_text())

    # Find the article text in the HTML
    article_text = ''
    article = soup.find('article')
    if article:
        for p in article.find_all('p'):
            article_text += p.get_text() + '\n'

    # Output the article text
    if len(article_text) > 20:
        print(article_text)
        print(len(article_text))
    else:
        print("\nERR: the article from " + url + " was less than 20 characters. The article probably wasn't found using BeautifulSoup.\n")

# print("url = " + url)
# extract_article_text("https://www.darkreading.com/risk/access-control-gap-microsoft-active-directory-enterprise-attack-surface")




from urllib import request
url = "http://www.bbc.co.uk/news/election-us-2016-35791008"
html = request.urlopen(url).read().decode('utf8')
html[:60]

from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')
title = soup.find('title')

print(title) # Prints the tag
print(title.string) # Prints the tag string content