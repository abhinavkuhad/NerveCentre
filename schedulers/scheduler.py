from apscheduler.schedulers.background import BackgroundScheduler
from schedulers import newsapi


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(newsapi.fetch_news, 'interval', minutes=60)
    scheduler.start()
