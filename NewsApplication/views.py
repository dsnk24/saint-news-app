from django.shortcuts import render
from newsapi import NewsApiClient # Import to get the news api

# Create your views here.
def index(request):
    napi = NewsApiClient(api_key="8c85fb88a775493ba01b3ab63705bddf")

    top_headlines = napi.get_top_headlines(sources="fox-news,bbc-news,cnn,abc-news")

    articles = top_headlines['articles']

    news = []
    desc = []
    imgs = []
    links = []

    for i in range(len(articles)):
        article = articles[i]

        news.append(article['title'])
        desc.append(article['description'])
        imgs.append(article['urlToImage'])
        links.append(article['url'])

    v_list = zip(news, desc, imgs, links)

    return render(request, 'index.html', context={'v_list': v_list})

