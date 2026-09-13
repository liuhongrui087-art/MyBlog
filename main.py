from app import create_app

# 传入配置，创建app实例
app = create_app("config.DevelopmentConfig")

if __name__ == '__main__':
    app.run(debug=True)
