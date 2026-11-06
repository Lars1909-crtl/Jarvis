# JARVIS - Jetzt mit kostenloser KI (Groq)
Design: Schwarz + Dunkles Weinrot

## NEU: Kostenlose KI anschließen (2 Minuten, kostenlos)
Jarvis nutzt jetzt Groq - kostenlos, super schnell, kein Abo.

1. Geh auf https://console.groq.com
2. Kostenlos anmelden (mit Google geht am schnellsten)
3. Links auf "API Keys" -> "Create API Key" -> kopieren
4. In diesem Ordner eine Datei namens `.env` erstellen (siehe .env.example)
   Darin steht dann:
   GROQ_API_KEY=gsk_dein_key_hier

5. Server neu starten:
   python app.py

Fertig. Jarvis beantwortet jetzt JEDE Frage wie ein echter Jarvis.

Ohne Key funktioniert er weiterhin wie bisher (Wishlist, News, Termine, Smalltalk).

## Start
pip install -r requirements.txt
python app.py
iPad: http://DEINE-LAPTOP-IP:5000
