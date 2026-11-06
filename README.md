# JARVIS - Dein persönlicher KI-Assistent
Kostenlos. Lokal. Aufgebaut Stück für Stück.

## Was kann er schon?
- Mit dir sprechen (Mikrofon -> Antwort -> Stimme)
- Wishlist: "Pack X auf meine Wishlist" / "Was steht auf meiner Wishlist?"
- News: "Gib mir die News"
- Termine: Grundgerüst für Google Kalender (siehe calendar.py)
- Persönlichkeit in brain.py anpassbar

## Setup (Windows / MacBook)
1. Python 3.11+ installieren (Haken bei Add to PATH)
2. In diesem Ordner Terminal öffnen:
   pip install -r requirements.txt
3. Server starten:
   python app.py
4. Auf dem iPad: Safari öffnen -> http://DEINE-LAPTOP-IP:5000
   Teilen -> Zum Home-Bildschirm -> Fertig ist deine Jarvis-App

## Laptop-IP finden
Windows: ipconfig (IPv4 Adresse)
Mac: ifconfig | grep inet

## Struktur
- app.py -> Server
- brain.py -> Persönlichkeit + Logik
- wishlist.py -> Wishlist
- news.py -> News Updater
- calendar.py -> Termine
- voice.py -> Stimme (Piper TTS vorbereitet)
- templates/index.html -> Das Gesicht auf dem iPad

## Nächste Schritte
Sag Meta AI einfach: "Füg Spotify hinzu" / "Ändere Persönlichkeit" / "Bau Termine fertig"
