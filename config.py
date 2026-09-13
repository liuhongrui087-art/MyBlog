# config.py
# 开发环境配置
class DevelopmentConfig:
    DEBUG = True
    SECRET_KEY = "my-dev-secret-123"

# 测试环境配置
class TestConfig:
    DEBUG = False
    TESTING = True
    SECRET_KEY = "test-secret"

# 生产环境配置（上线用）
class ProductionConfig:
    DEBUG = False
    SECRET_KEY = "a_very_secure_long_key_here"
