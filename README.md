# MyBlog

一个用 Flask 从零搭建的博客系统，作为 Web 开发的学习项目。

## 功能

- **文章管理**：发布、查看、编辑、删除（完整 CRUD）
- **首页**：展示最新 5 篇文章
- **文章列表 / 详情页**：按发布时间倒序排列
- **模板继承**：统一的页面母版，导航栏自动高亮当前页
- **XSS 防护**：所有用户输入经 Jinja2 自动转义

## 技术栈

| 层 | 技术 |
|---|---|
| 语言 | Python 3.11 |
| Web 框架 | Flask 3.1 |
| 数据库 | SQLite + Flask-SQLAlchemy |
| 模板引擎 | Jinja2（母版继承）|
| 前端 | 原生 HTML / CSS |

## 运行方式

### 1. 获取代码

```bash
git clone <仓库地址>
cd MyBlog
```

### 2. 创建并激活虚拟环境

**Windows:**&#8203;

```bash
python -m venv venv
venv\Scripts\activate
```

**macOS / Linux:**&#8203;

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. 安装依赖

```bash
pip install -r requirements.txt
```

### 4. 启动

```bash
python main.py
```

浏览器访问 http://127.0.0.1:5000

### 5. 添加示例文章（可选）

```bash
python seed.py
```

## 目录结构

```
MyBlog/
├── app.py                  # 应用工厂：创建 Flask 实例、绑定数据库、注册蓝图
├── main.py                 # 程序入口
├── config.py               # 环境配置（开发 / 测试 / 生产）
├── routes.py               # 路由与数据模型
├── requirements.txt        # 依赖清单
├── .flaskenv               # Flask CLI 环境变量
├── templates/              # Jinja2 模板
│   ├── base.html           # 母版（导航 + 页面骨架）
│   ├── hello.html          # 首页
│   ├── post_list.html      # 文章列表
│   ├── post_new.html       # 写文章
│   ├── post_detail.html    # 文章详情
│   ├── post_edit.html      # 编辑文章
│   ├── about.html          # 关于
│   ├── index.html          # 提交名字练习
│   ├── submit.html         # 提交结果
│   ├── show_users.html     # 用户列表
│   └── greet.html          # 问候练习
├── static/
│   ├── style.css
│   └── images/cat.jpg
└── instance/
    └── blog.db             # SQLite 数据库（自动生成，未纳入版本控制）
```

## 路由一览

| 方法 | 路径 | 功能 |
|---|---|---|
| GET | `/` | 首页（最新文章）|
| GET | `/posts` | 文章列表 |
| GET | `/posts/new` | 写文章表单 |
| POST | `/posts/save` | 保存新文章 |
| GET | `/posts/<id>` | 文章详情 |
| GET / POST | `/posts/<id>/edit` | 编辑文章 |
| POST | `/posts/<id>/delete` | 删除文章 |
| GET | `/about` | 关于 |
| GET | `/greet/<name>` | 问候（练习）|
| GET | `/user/new` | 提交名字（练习）|
| POST | `/user/save` | 提交处理（练习）|
| GET | `/user/list` | 用户列表（练习）|

## 说明

- 数据库文件 `instance/blog.db` **未纳入版本控制**，首次运行时由 `db.create_all()` 自动创建
- 虚拟环境 `venv/` **未纳入版本控制**，请按上面第 2 步自行创建
- 用户输入全部通过 Jinja2 模板渲染并自动转义，已修复反射型与存储型 XSS
