from flask import Blueprint, Response, redirect, url_for, render_template
import model
import presenters.create

# 1. ひとつのHTMLファイルを担当するBlueprintを扱う
app = Blueprint('timeline', __name__, url_prefix='/timeline')

# 2. ここ(/timeline/)へ遷移する関数を定義する


def redirect_to_timeline() -> Response:
    ep = f'{app.name}.{__render_page.__name__}'
    return redirect(url_for(ep))

# 各エンドポイントは隠蔽する


@app.route('/')
def __render_page():
    context = dict(
        # ボタンが押された時やフォームが提出された時に移るURLを変数で提供する
        create_url=url_for(
            f'{app.name}.{__require_redirect_to_create.__name__}'),
        posts=reversed(model.posts)
    )
    return render_template('timeline.html', **context)

# 3. ボタンが押された時やフォームが提出された時に移るURLの担当をする


@app.route('/create')
def __require_redirect_to_create():
    # 3. そこでしかるべき処理を行い、HTMLを作成するエンドポイントへ移動する
    return presenters.create.redirect_to_create()
