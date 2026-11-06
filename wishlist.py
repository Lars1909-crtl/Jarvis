import json, os
FILE = "wishlist.json"

def _load():
    if not os.path.exists(FILE):
        return []
    try:
        with open(FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return []

def _save(items):
    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(items, f, ensure_ascii=False, indent=2)

def get_all():
    return _load()

def add(wish: str):
    items = _load()
    if wish not in items:
        items.append(wish)
        _save(items)
    return items

def remove(wish: str):
    items = _load()
    items = [x for x in items if x.lower() != wish.lower()]
    _save(items)
    return items
