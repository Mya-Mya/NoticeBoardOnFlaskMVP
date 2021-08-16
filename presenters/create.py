from flask import Blueprint, Response, redirect, url_for, render_template, request
import model
import presenters.timeline

# 1. ひとつのHTMLファイルを担当するBlueprintを扱う
app = Blueprint('create', __name__, url_prefix='/create')

# 2. ここ(/create/)へ遷移する関数を定義する


def redirect_to_create() -> Response:
    ep = f'{app.name}.{__render_page.__name__}'
    return redirect(url_for(ep))

# 各エンドポイントは隠蔽する


@app.route('/')
def __render_page():
    context = dict(
        # ボタンが押された時やフォームが提出された時に移るURLを変数で提供する
        post_url=url_for(f'{app.name}.{__on_post.__name__}'),
        cancel_url=url_for(f'{app.name}.{__on_cancel.__name__}'),
    )
    return render_template('create.html', **context)

# 3. ボタンが押された時やフォームが提出された時に移るURLの担当をする


@app.post('/post')
def __on_post():
    # 3. そこでしかるべき処理を行い、HTMLを作成するエンドポイントへ移動する
    name = request.form['form_name']
    message = request.form['form_message']
    model.add_post(name, message)
    return presenters.timeline.redirect_to_timeline()


@app.route('/cancel')
def __on_cancel():
    return presenters.timeline.redirect_to_timeline()
