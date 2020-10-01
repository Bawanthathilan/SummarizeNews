import tkinter as tk
import nltk
from textblob import TextBlob
from newspaper import Article
#pip install nltk
#pip install textblob
#pip install newspaper3k
# nltk.download('punkt')
# url = 'http://www.dailymirror.lk/breaking_news/We-are-not-here-to-deliver-lecture-German-Swiss-Envoys-tell-President/108-196953'


def summarize():
    url =utext.get('1.0', 'end').strip()
    article = Article(url)
    article.download()
    article.parse()

    article.nlp()
    title.config(state='normal')
    author.config(state='normal')
    publication.config(state='normal')
    summary.config(state='normal')
    sentiment.config(state='normal')

    title.delete('1.0', 'end')
    title.insert('1.0', article.title)
    
    author.delete('1.0', 'end')
    author.insert('1.0', article.authors)

    publication.delete('1.0', 'end')
    publication.insert('1.0', article.publish_date)

    summary.delete('1.0', 'end')
    summary.insert('1.0', article.summary)

    analysis = TextBlob(article.text)
    sentiment.delete('1.0', 'end')
    sentiment.insert('1.0', f'Polarity: {analysis.polarity}Sentiment:{"positive" if analysis.polarity > 0 else "negative" if analysis.polarity < 0 else "neutral"}')



    title.config(state='disabled')
    author.config(state='disabled')
    publication.config(state='disabled')
    summary.config(state='disabled')
    sentiment.config(state='disabled')

    
root = tk.Tk()
root.title('News Summarizer')
root.geometry('1200x600')

tlable = tk.Label(root, text="Title")
tlable.pack()

title = tk.Text(root, height=1, width=140)
title.config(state='disabled' , bg='#dddddd')
title.pack()

alable = tk.Label(root, text="Author")
alable.pack()

author = tk.Text(root, height=1, width=140)
author.config(state='disabled' , bg='#dddddd')
author.pack()

plable = tk.Label(root, text="Publishing date")
plable.pack()

publication = tk.Text(root, height=1, width=140)
publication.config(state='disabled' , bg='#dddddd')
publication.pack()

slable = tk.Label(root, text="Summary")
slable.pack()

summary = tk.Text(root, height=20, width=140)
summary.config(state='disabled' , bg='#dddddd')
summary.pack()



selable = tk.Label(root, text='Sentiment Analysis')
selable.pack()

sentiment = tk.Text(root, height=1, width=140)
sentiment.config(state='disabled' , bg='#dddddd')
sentiment.pack()

ulable = tk.Label(root, text="URL")
ulable.pack()

utext = tk.Text(root, height=1, width=140)
utext.pack()

btn = tk.Button(root, text="Summerize" , command=summarize)
btn.pack()


root.mainloop()