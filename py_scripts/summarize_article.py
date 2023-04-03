import openai
import random
import requests
import os
from bs4 import BeautifulSoup
import re

# Sumy elements
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer

# openai.api_key = os.environ["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"]
openai.api_key = "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"

# list of user agent headers used to trick web-scraping detectors
user_agents_list = [
    'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.83 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36',
    'Mozilla/5.0 (iPhone12,1; U; CPU iPhone OS 13_0 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Mobile/15E148 Safari/602.1',
    'Mozilla/5.0 (iPhone14,3; U; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Mobile/19A346 Safari/602.1',
    'Mozilla/5.0 (Linux; Android 7.0; Pixel C Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/52.0.2743.98 Safari/537.36'
]

# Extracts all of the text in <p> tags from a given url
def BeautifulSoup_summarize(url):
    # Get the HTML content from the URL
    html = requests.get(url, headers={'User-Agent': random.choice(user_agents_list)}).content
    # html = requests.get(url).content

    # Parse the HTML content with BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # extract the text from the soup looking for all html tags
    article_text = ''
    # for element in soup.find_all(['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6']):
    for element in soup.find_all(['p']):
        article_text += ' ' + element.get_text()

    return article_text

# Function to summarize text
def GPT_summarize_text(text):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"summarize this text for me in less than 250 characters: {text}",
        temperature=0.5,
        max_tokens=50,
        n=1,
        stop=None,
        timeout=15,
    )
    summary = response.choices[0].text.strip()
    return summary

# Function to generate a title for text
def GPT_generate_title(text):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"suggest a title for this text: {text}",
        temperature=0.7,
        max_tokens=30,
        n=1,
        stop=None,
        timeout=15,
    )
    title = response.choices[0].text.strip()
    return title

# Function to generate hashtags for text
def GPT_generate_hashtags(text):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"suggest 12 engaging hashtags for this text: {text}",
        temperature=0.7,
        max_tokens=60,
        n=1,
        stop=None,
        timeout=15,
    )
    hashtags = response.choices[0].text.strip()
    hashtags = re.findall(r"#\w+", hashtags)
    return hashtags

# def get_html(url):
#     response = requests.get(url)
#     return response.content

# def extract_article_text(html):
#     soup = BeautifulSoup(html, 'html.parser')
#     article_text = ''
#     for element in soup.find_all(['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6']):
#         article_text += ' ' + element.get_text()
#     return article_text

# def filter_out_non_article_content(messy_text):
#     prompt = f"in this text, there is an article I would like to keep. Remove all text before the start of the article and after the end of the article: {messy_text}"
#     response = openai.Completion.create(
#         engine="davinci",
#         prompt=prompt,
#         temperature=0.5,
#         max_tokens=2048,
#         n=1,
#         stop=None,
#     )
#     plain_article = response.choices[0].text.strip()
#     return plain_article




# def summarize_from_html(html):
#     prompt = f"find the article text in this raw website code and return it: {html}"
#     response = openai.Completion.create(
#         engine="davinci",
#         prompt=prompt,
#         temperature=0.5,
#         max_tokens=2048,
#         n=1,
#         stop=None,
#     )
#     article_text = response.choices[0].text.strip()
#     return article_text

# def gather_article_text_AI(url):
#     prompt = f"return the text from this article: {url}"
#     response = openai.Completion.create(
#         engine="davinci",
#         prompt=prompt,
#         temperature=0.5,
#         max_tokens=2048,
#         n=1,
#         stop=None,
#     )
#     article_text = response.choices[0].text.strip()
#     return article_text

# def gather_article_text_BS(url):
#     import requests
#     from bs4 import BeautifulSoup

#     url = "https://www.cnbc.com/2023/03/16/ukraine-war-live-updates-latest-news-on-russia-and-the-war-in-ukraine.html"

#     # Send GET request to webpage
#     response = requests.get(url)

#     # Use BeautifulSoup to parse webpage content and extract text
#     soup = BeautifulSoup(response.content, "html.parser")
#     article_text = soup.get_text()

#     print(article_text)
#     return article_text

# def summarize_text(article_text):
#     max_chars = 250
#     prompt = f"summarize this text for me in less than '{max_chars}' characters: '{article_text}'"
#     response = openai.Completion.create(
#         engine="davinci",
#         prompt=prompt,
#         temperature=0,
#         max_tokens=250,
#         n=1,
#         stop=None,
#         timeout=15,
#     )
#     summary = response.choices[0].text.strip()
#     return summary

# def suggest_title(summary):
#     prompt = f"provide a title for this summary: '{summary}'"
#     response = openai.Completion.create(
#         engine="davinci",
#         prompt=prompt,
#         temperature=0,
#         max_tokens=250,
#         n=1,
#         stop=None,
#         timeout=15,
#     )
#     suggested_title = response.choices[0].text.strip()
#     return suggested_title


# target urls that work
# url = "https://www.darkreading.com/risk/access-control-gap-microsoft-active-directory-enterprise-attack-surface"
# url = "https://arstechnica.com/information-technology/2023/03/openai-checked-to-see-whether-gpt-4-could-take-over-the-world/"
# url = "https://www.cnn.com/2023/03/14/politics/us-drone-russian-jet-black-sea/index.html"
# url = "https://www.darkreading.com/vulnerabilities-threats/microsoft-zero-day-bugs-security-feature-bypass"
# url = "https://www.cnbc.com/2023/03/16/ukraine-war-live-updates-latest-news-on-russia-and-the-war-in-ukraine.html"
# url = "https://studyfinds.org/humans-machines-artificial-intelligence-agi/"

# target urls that don't work
# this url is actually hilarious in how it combats scraping
# url = https://www.ncsc.gov.uk/blog-post/refreshed-toolkit-helps-board-members-to-govern-cyber-risk




url = input("Please provide a URL of an article to summarize: \n")

# summarizes the article and saves it to a variable
article = BeautifulSoup_summarize(url)
print(article)

# Open a file in write mode
with open("articleoutput.txt", "w") as f:
    # Write the string to the file
    f.write(article)

# Close the file
f.close()




# Sumy - summarize the text to a digestible size for GPT (~6-sentence summary)
# Set the number of sentences for the summary
SUMMARY_LENGTH = 5

# Instantiate a plaintext parser
parser = PlaintextParser.from_string(article, Tokenizer("english"))

# Instantiate a LexRank summarizer
summarizer = LexRankSummarizer()

# Get the summary using the summarizer
summary = summarizer(parser.document, SUMMARY_LENGTH)

# Combine the summary sentences into a single string
Sumy_article_summary = ""
for sentence in summary:
    Sumy_article_summary += str(sentence)

# Print the summarized article
# print(Sumy_article_summary)

# GPT - suggest an engaging title from the Sumy summary
GPT_summary = GPT_summarize_text(Sumy_article_summary)

# GPT - summarize Sumy summary
GPT_title = GPT_generate_title(Sumy_article_summary)

# GPT - suggest 15 hashtags based on Sumy summary
GPT_hashtags = GPT_generate_hashtags(Sumy_article_summary)



# print results
print(f"\nSummary: {GPT_summary}")
print(f"Title: {GPT_title}")
print(f"Hashtags: {GPT_hashtags}")