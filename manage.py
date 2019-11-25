from app import app
from flask_script import Manager ,Server

# from flask_script import Manager,Server
from flask_migrate import  Migrate ,MigrateCommand
from app.models import User 
from app import pitch_app,db
from config import config_options
   
# Creating app instance
app =pitch_app('development')
manager = Manager(app)
# manager.add_command('server',Server)
migrate = Migrate(app,db)
manager.add_command('db',MigrateCommand)
# @manager.command
# def test():
#     """Run the unit tests."""
#     import unittest
#     tests = unittest.TestLoader().discover('tests')
#     unittest.TextTestRunner(verbosity=2).run(tests)

# #....
@manager.shell
def make_shell_context():
    return dict(app = app,db = db,User = User )

if __name__ =='__main__':
    manager.run()

    

# manager = Manager (app)
# if __name__ == '__main__':
#     manager.run()