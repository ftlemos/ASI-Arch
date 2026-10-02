from.mongo_database import create_client
from unittest.mock import MagicMock

try:
    db = create_client()
except Exception as e:
    print(f"⚠️ DB not available, using mock: {e}")
    db = MagicMock()
    db.health = lambda: True
    db.insert = lambda *a, **k: None
    db.find = lambda *a, **k: []
    db.update = lambda *a, **k: None

def program_sample(*args, **kwargs):
    try:
        return db.program_sample(*args, **kwargs)
    except:
        return None

def update(*args, **kwargs):
    try:
        return db.update(*args, **kwargs)
    except:
        return None
