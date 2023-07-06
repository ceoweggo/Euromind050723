from app import app
from pathlib import Path
from dotenv import load_dotenv
import os

def Config(object):
    env_path = Path('.') / '.env'
    load_dotenv(dotenv_path=env_path)

    SECRET_KEY = os.getenv('SECRET_KEY')

    # VARIABLES
    CSRF_ENABLED = None
    WTF_CSRF_ENABLED = None
    SESSION_COOKIE_SECURE = None
    SESSION_COOKIE_HTTPONLY = None
    SESSION_COOKIE_SAMESITE = None

    # SETTINGS BY DEFAULT
    DEBUG = True
    ENV = "development"
    OAUTHLIB_INSECURE_TRANSPORT = True

    ## DATABASE MONGO URI
    MONGO_URI=os.environ.get("DATABASE_LOCAL_URL")

    if object == 'deployment':
        ENV = "deployment"
        DEBUG = False
        CSRF_ENABLED = True
        WTF_CSRF_ENABLED = True

        ## DATABASE MONGO URI
        MONGO_URI=os.environ.get("DATABASE_REMOTE_URL")

        SESSION_COOKIE_SECURE = True
        SESSION_COOKIE_HTTPONLY = True
        SESSION_COOKIE_SAMESITE = 'NONE'
        
    elif object == 'testing':
        DEBUG = False

        ## DATABASE MONGO URI
        MONGO_URI=os.environ.get("DATABASE_TESTING_URL")

    ## APP UPDATING
    app.config.update(
        DEBUG=DEBUG,
        FLASK_ENV=ENV,
        FLASK_APP=os.environ.get('FLASK_APP'),
        SECRET_KEY=SECRET_KEY,
        MONGO_URI=MONGO_URI,
        CSRF_ENABLED=CSRF_ENABLED,
        WTF_CSRF_ENABLED=WTF_CSRF_ENABLED
    )