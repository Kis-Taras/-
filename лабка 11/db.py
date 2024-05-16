from schemas.users import UserCreate as User
from schemas.posts import Post

class DummyDatabase:
    users: dict[int, User] = {}
    posts: dict[int, Post] = {}

db = DummyDatabase()
db.users[1] = {'id':1, 'email' : 'taraskis06@gmail.com', 'name':'Тарас', 'telegram_username' : '@kis_taras', 'comments' : ['Можна 5😄']}
db.users[2] = {'id':2, 'email' : 'dmitrokasprivskij@gmail.com', 'name' : 'Дмитро', 'telegram_username' : '@Артур', 'comments' : ['...']}
db.users[3] = {'id':3, 'email' : 'artursyniuk@gmail.com', 'name' : 'Артур', 'telegram_username' : '@DmYTr0_01', 'comments' : ['...']}
db.users[4] = {'id':4, 'email' : 'elveo2006@gmail.com', 'name' : 'Віталій', 'telegram_username' : '@Vitalii...', 'comments' : ['...']}
db.users[5] = {'id':5, 'email' : 'artikzivcik8@gmail.com', 'name' : 'Артем', 'telegram_username' : '@deep0850', 'comments' : ['...']}
