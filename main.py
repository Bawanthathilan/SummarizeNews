import tkinter as tk
import nltk
from textblob import TextBlob
from newspaper import Article

#pip install nltk
#pip install textblob
#pip install newspaper3k
nltk.download('punkt')

url = 'https://www.bbc.com/news/technology-53640724'

article = Article(url)
article.download()
article.parse()

article.nlp()

print(f'Title:{article.title}')
print(f'Authors:{article.authors}')
print(f'Publication Date:{article.publish_date}')
print(f'Summary:{article.summary}')

analysis = TextBlob