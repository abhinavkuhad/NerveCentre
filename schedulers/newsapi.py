from newsapi import NewsApiClient
from automatedworkflow.models import NewsCentre
from uuid import uuid4
# Init
newsapi = NewsApiClient(api_key='05b101562f604ee2a937baa72dbfdadc')


# /v2/top-headlines
def fetch_news():
    print("API Started.")
    top_headlines = newsapi.get_top_headlines(country='us')
    for headline in top_headlines['articles']:
        if headline:
            try:
                newscentre, created = NewsCentre.objects.get_or_create(id=uuid4(),source_name=headline['source']['name'],
                                                                       author=headline['author'], title=headline['title'],
                                                                       description=headline['description'],
                                                                       news_url=headline['url'],
                                                                       publish_date=headline['publishedAt'],
                                                                       content=headline['content'])
            except Exception as e:
                print(e)
    print("API Shutdown.")
