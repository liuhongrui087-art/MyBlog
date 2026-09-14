from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

# 先创建db对象，这里先不绑定app
db = SQLAlchemy()

def create_app(config_name):
    # 在函数内部创建app，没有全局app！
    app = Flask(__name__)

    app.config.from_object(config_name)
    # ========== 数据库配置 ==========
    # 数据库放在instance文件夹（你项目已经有instance目录，推荐放这里）
    # 拿到app.py所在文件夹
    basedir = os.path.abspath(os.path.dirname(__file__))
    # 数据库放在 instance 目录下（该目录不在版本控制里，克隆后可能不存在，先确保它存在）
    db_dir = os.path.join(basedir, "instance")
    os.makedirs(db_dir, exist_ok=True)
    # 拼接数据库路径，不管项目放在哪个盘都自动适配
    db_path = os.path.join(db_dir, "blog.db")
    # sqlite URI 写法
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_path
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # 关闭警告

    # 把db绑定app
    db.init_app(app)
    # 延迟导入蓝图，避免循环导入
    import routes
    #注册蓝图
    app.register_blueprint(routes.bp)

    #在应用上下文里面创建数据表(只第一次运行生效)
    with app.app_context():
        db.create_all()
    return app
