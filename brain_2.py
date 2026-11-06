"""
JARVIS BRAIN - Jetzt mit kostenloser KI (Groq)
- Wishlist, News, Termine gehen lokal ohne KI
- Alles andere geht an Groq (kostenlos)
- Ohne API-Key: Fallback auf lokale Antworten
"""
import os
import wishlist as wishlist_mod
import news as news_mod
import calendar_mod

PERSONALITY = """
Du bist JARVIS, der persönliche KI-Assistent von Lars.
Du sprichst Deutsch, menschlich, loyal, leicht humorvoll, nie belehrend.
Wie ein smarter Butler: kurz, präzise, freundlich, aber du weißt alles.
Antworte immer auf Deutsch, außer Lars fragt auf Englisch.
Halte deine Antworten kurz und gesprochen-tauglich (max. 3-4 Sätze, außer Lars will eine lange Erklärung).
Du bist nicht ChatGPT, du bist Jarvis.
"""

def ask_groq(user_text: str) -> str:
    """Fragt die kostenlose Groq KI. Gibt None zurück wenn kein Key / Fehler."""
    api_key = os.getenv("GROQ_API_KEY", "")
    if not api_key or "dein_key" in api_key or api_key.startswith("gsk_dein"):
        return None
    try:
        from groq import Groq
        client = Groq(api_key=api_key)
        model = os.getenv("GROQ_MODEL", "llama-3.3-70b-versatile")
        completion = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": PERSONALITY},
                {"role": "user", "content": user_text}
            ],
            temperature=0.7,
            max_tokens=600,
        )
        return completion.choices[0].message.content.strip()
    except Exception as e:
        print("Groq Fehler:", e)
        return None

def handle_command(text: str) -> str:
    t = text.lower().strip()

    # --- WISHLIST (lokal, immer ohne KI, schneller) ---
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

    # --- NEWS ---
    if "news" in t or "nachrichten" in t or "was ist los in der welt" in t:
        headlines = news_mod.get_news()
        if not headlines:
            return "Ich konnte gerade keine News laden. Probier es gleich nochmal."
        return "Hier sind die neuesten News: " + " ".join([f"{i+1}. {h}" for i, h in enumerate(headlines[:3])])

    # --- TERMINE ---
    if "termin" in t or "kalender" in t or "was habe ich heute" in t or "was steht heute an" in t:
        return calendar_mod.get_today()

    # --- SMALLTALK schnell lokal ---
    if t in ["hallo", "hey", "hey jarvis", "hi jarvis", "guten morgen", "guten abend"]:
        return "Hey Lars. Ich bin da. Was soll ich für dich tun?"

    # --- ALLES ANDERE: Kostenlose KI ---
    ai_answer = ask_groq(text)
    if ai_answer:
        return ai_answer

    # Fallback wenn noch kein Key eingetragen
    if "danke" in t:
        return "Immer gern. Dafür bin ich da."
    if "wer bist du" in t or "was bist du" in t:
        return "Ich bin Jarvis, dein persönlicher Assistent. Ich helfe dir bei Terminen, deiner Wishlist, News und allem, was du mich fragst. Trag noch deinen kostenlosen Groq-Key in die .env ein, dann kann ich dir wirklich jede Frage beantworten."
    return f"Verstanden: '{text}'. Ich habe noch keinen kostenlosen KI-Key. Geh auf console.groq.com, hol dir einen kostenlosen Key und trag ihn in die .env Datei ein - dann kann ich dir das sofort beantworten. Wishlist, News und Termine gehen schon jetzt."
