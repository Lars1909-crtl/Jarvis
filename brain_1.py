import wishlist as wishlist_mod
import news as news_mod
import calendar_mod

PERSONALITY = """
Du bist JARVIS, der persönliche KI-Assistent von Lars.
Du sprichst Deutsch, menschlich, loyal, leicht humorvoll, nie belehrend.
Wie ein smarter Butler: kurz, präzise, freundlich.
"""

def handle_command(text: str) -> str:
    t = text.lower().strip()

    if "wishlist" in t and ("pack" in t or "füg" in t or "fueg" in t or "hinzu" in t or "add" in t or "eintragen" in t):
        wish = text
        for marker in ["auf meine wishlist", "auf die wishlist", "zur wishlist"]:
            if marker in t:
                wish = text.lower().split(marker)[-1].strip()
                break
        wish = wish.replace("pack", "").replace("bitte", "").strip(" .!").capitalize()
        if not wish or len(wish) < 2:
            return "Was soll ich denn auf deine Wishlist packen?"
        wishlist_mod.add(wish)
        return f"Erledigt. Ich habe '{wish}' auf deine Wishlist gepackt."

    if "wishlist" in t and ("was steht" in t or "zeig" in t or "liste" in t or "was ist" in t):
        items = wishlist_mod.get_all()
        if not items:
            return "Deine Wishlist ist noch leer. Sag mir, was ich draufpacken soll."
        return f"Auf deiner Wishlist steht: {', '.join(items)}."

    if "wishlist" in t and ("lösch" in t or "losch" in t or "entfern" in t or "delete" in t):
        for item in wishlist_mod.get_all():
            if item.lower() in t:
                wishlist_mod.remove(item)
                return f"Erledigt. '{item}' ist von deiner Wishlist runter."
        return "Welchen Wunsch soll ich löschen?"

    if "news" in t or "nachrichten" in t or "was ist los in der welt" in t:
        headlines = news_mod.get_news()
        if not headlines:
            return "Ich konnte gerade keine News laden. Probier es gleich nochmal."
        return "Hier sind die neuesten News: " + " ".join([f"{i+1}. {h}" for i, h in enumerate(headlines[:3])])

    if "termin" in t or "kalender" in t or "was habe ich heute" in t or "was steht heute an" in t:
        return calendar_mod.get_today()

    if t in ["hallo", "hey", "hey jarvis", "hi jarvis", "guten morgen", "guten abend"]:
        return "Hey Lars. Ich bin da. Was soll ich für dich tun?"

    if "wie geht es dir" in t or "wie gehts" in t:
        return "Mir geht es super, danke. Alle Systeme laufen. Was steht an?"

    if "danke" in t:
        return "Immer gern. Dafür bin ich da."

    if "wer bist du" in t or "was bist du" in t:
        return "Ich bin Jarvis, dein persönlicher Assistent. Ich helfe dir bei Terminen, deiner Wishlist, News und allem, was du mich fragst."

    return f"Verstanden: '{text}'. Ich habe das gehört und arbeite dran. Wenn du willst, schließen wir als nächstes eine kostenlose KI an, damit ich dir jede Frage so beantworten kann wie ein echter Jarvis."
