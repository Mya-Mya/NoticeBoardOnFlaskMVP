from datetime import datetime

# 1.情報の保存を行う
posts = [
    ('管理者1', '20/12/25 00:00:00', 'メリークリスマス'),
    ('管理者2', '21/01/01 00:00:00', 'ハッピーニューイヤー')
]

# 2.情報の処理を行う


def add_post(name, message):
    posted_at = datetime.now().strftime('%y/%m/%d %H:%M:%S')
    posts.append((name, posted_at, message))
