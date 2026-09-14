from flask import Blueprint, request, make_response, render_template, session, jsonify

from app import db


# 创建蓝图实例 bp
bp = Blueprint('main', __name__)

# ========= 定义数据库模型（一张User表，存用户名）=========
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80),unique=False,nullable=False)
# 全部路由改成 @bp.route
@bp.route('/user/new')
def index():
    return render_template('index.html')

@bp.route('/about')
def about():
    return 'This is the About Page.'

@bp.route('/greet/<name>')
def greet(name):
    return render_template('greet.html', name=name)

@bp.route('/user/save', methods=['POST'])
def submit():
    username = request.form.get('username')
    if username:
        # 新增：把名字写入数据库
        new_user = User(username=username)
        db.session.add(new_user)
        db.session.commit()
        session['username'] = username
    return render_template('submit.html', username=username)

@bp.route('/custom_response')
def custom_response():
    response = make_response('This is a custom response!')
    response.headers['X-Custom-Header'] = 'value'
    return response

@bp.route('/')
def hello():
    return render_template('hello.html')

@bp.route('/user/list')
def show_users():
    all_user = User.query.all()
    return render_template('show_users.html', users=all_user)

# ========= Session 示例 =========

@bp.route('/set_session/<username>')
def set_session(username):
    session['username'] = username
    return jsonify({'ok': True, 'username': username})

@bp.route('/get_session')
def get_session():
    username = session.get('username')
    return jsonify({'username': username})

@bp.route('/clear_session')
def clear_session():
    session.pop('username', None)   # 只删这一个键，键不存在也不报错
    return jsonify({'ok': True, 'message': 'Session cleared'})
