import feedparser
def get_news():
    try:
        feed = feedparser.parse("https://www.tagesschau.de/xml/rss2_https/")
        return [e.title for e in feed.entries[:5]]
    except Exception as e:
        print("News Fehler:", e)
        return []
