"""
News Updater - Kostenlos über Tagesschau RSS, kein API-Key nötig.
"""
import feedparser

def get_news():
    try:
        feed = feedparser.parse("https://www.tagesschau.de/xml/rss2_https/")
        headlines = []
        for entry in feed.entries[:5]:
            headlines.append(entry.title)
        return headlines
    except Exception as e:
        print("News Fehler:", e)
        return []
