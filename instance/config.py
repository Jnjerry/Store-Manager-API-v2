#contains variables specific to our application

class Config(object):
    "parent configuration class"
    DEBUG= False
    CSRF_ENABLED = True
    SECRET_KEY=os.getenv("SECRET_KEY","funguo")
    DATABASE_URL=os.getenv("DATABASE_URL")


class DevelopmentConfig(Config):
    "Configurations for Development Phase"
    DEBUG = True


class TestingConfig(Config):
    """Configurations for Testing,"""
    TESTING = True
    DEBUG = True
    DATABASE_URL = os.getenv("DATABASE_TEST_URL")

class StagingConfig(Config):
    """Configurations for Staging."""
    DEBUG = True


class ProductionConfig(Config):
    """Configurations for Production."""
    DEBUG = False
    TESTING = False


app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'staging': StagingConfig,
    'production': ProductionConfig,
}
