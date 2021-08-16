from flask import Flask
# 1.Flaskサーバーを立ち上げる
app=Flask(__name__)

#2. 各presenterが作るBlueprintをまとめる
from presenters import timeline, create
app.register_blueprint(timeline.app)
app.register_blueprint(create.app)

#3. 初期値のURL('/')からどこかのシーンへ移る
@app.route('/')
def __require_redirect_to_timeline():
    return timeline.redirect_to_timeline()

# 1.Flaskサーバーを立ち上げる
if __name__=='__main__':
    app.run('0.0.0.0',8000,True)