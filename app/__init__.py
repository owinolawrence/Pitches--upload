from flask import Flask
from config import Config
import os
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from config import config_options
from flask_bootstrap import Bootstrap
# from flask_uploads import UploadSet,configure_uploads,IMAGES
# from flask_mail import Mail

app = Flask(__name__)
bootstrap = Bootstrap()
db = SQLAlchemy()
# photos = UploadSet('photos',IMAGES)
# mail = Mail()



login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'
def pitch_app(config_name):
    
    app.config.from_object(config_options[config_name])
    # initialize extensions
    login_manager.init_app(app)
    db.init_app(app)
    bootstrap.init_app(app)
    # mail.init_app(app)
    # configure UploadSet
    # configure_uploads(app,photos)
    # registering main blueprint
   
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    # registering auth blueprint
    
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    return app