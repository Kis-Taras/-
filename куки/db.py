from collections import defaultdict
from models import Post, User, Photo

db = {
    "post1": {"title": "Перший пост", "content": "Можна 5😄"},
    "post2": {"title": "Другий пост", "content": "Другий пост"},
}

users_db = {
    "users1" :{ 'id': 1, 'name': 'Taras Kis', 'email': 'taraskis06@gmail.com', 'name': 'Тарас', 'telegram_username': '@kis_taras', 'comments': 'Можна 5😄'}
}

photos_db = {
    "photo1": {"url": "/static/img/foto1.jpeg", "description": "Прекрасний захід сонця."},
    "photo2": {"url": "/static/img/foto2.jpg", "description": "Чудовий краєвид."},
}

stats = defaultdict(int)
