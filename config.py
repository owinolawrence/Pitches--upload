import os

basedir = os.path.abspath(os.path.dirname(__file__))
class Config(object):

    
    SECRET_KEY = '435313ea80b5a872114356a1'
    # SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://moringa:p@localhost/pitches'
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    SUBJECT_PREFIX = 'Pitches-uploads'
class ProductionConfig(Config):
     pass
class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
class TestingConfig(Config):
    TESTING = True
config_options = {
'test':TestingConfig
}