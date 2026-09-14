from datetime import datetime, timedelta
from app import create_app, db
from routes import Post

app = create_app('config.DevelopmentConfig')

with app.app_context():
    db.create_all()

    if Post.query.count() > 0:
        print(f'数据库里已有 {Post.query.count()} 篇文章，跳过。')
    else:
        posts = [
            Post(
                title='欢迎来到我的博客',
                content='这是我学习 Flask 时搭建的第一个项目。\n\n'
                        '从最简单的路由开始，一步步加上了模板、数据库、表单，\n'
                        '最后做成了一个能写文章的博客。',
                created_at=datetime.now() - timedelta(days=3),
            ),
            Post(
                title='为什么要写博客',
                content='写作是最好的思考方式。\n\n'
                        '一个想法，只有在你能清楚地写出来时，才算真正想明白了。',
                created_at=datetime.now() - timedelta(days=1),
            ),
            Post(
                title='学习笔记：模板继承',
                content='母版负责骨架（导航、样式引用、页脚），\n'
                        '子模板只填自己需要的块。\n\n'
                        '好处是：改导航只需要改一个文件。',
                created_at=datetime.now(),
            ),
        ]
        db.session.add_all(posts)
        db.session.commit()
        print(f'已插入 {len(posts)} 篇示例文章。')
