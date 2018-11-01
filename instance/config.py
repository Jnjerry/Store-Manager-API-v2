#contains variables specific to our application
import os
class Config(object):
    "parent configuration class"
    DEBUG= False
    CSRF_ENABLED = True
    SECRET_KEY=os.getenv("SECRET_KEY","funguo")


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
    'database_url':"dbname='store_manager_api' host='localhost' port='5432' user='postgres' password='m@ngun@1'"
    'test_url':"dbname='store_test_api' host='localhost' port='5432' user='postgres' password='m@ngun@1'"
}
