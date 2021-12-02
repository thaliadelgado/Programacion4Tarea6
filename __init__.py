from flask import Flask
from os import path
import redis



def create_app():
    app = Flask(__name__)
    # make redis
    redis_cache = redis.StrictRedis()

# make flask app
    app = Flask(__name__)
    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

  

    return app


