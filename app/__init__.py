from flask import Flask

app = Flask(__name__, instance_relative_config=True)

## LIBRARIES
from flask_breadcrumbs import Breadcrumbs
Breadcrumbs(app=app)

def my_first_application_config():
    # Load the environment parameters configuration
    app.config.from_object('config.config')

    # Force to close session by default. Not applicate right now
    from datetime import timedelta
    app.permanent_session_lifetime = timedelta(minutes=5760) # Five days

    import locale
    locale.setlocale(locale.LC_ALL, ("es_ES", "UTF-8"))

    from itsdangerous import URLSafeTimedSerializer
    URLSafeTimedSerializer(app.config["SECRET_KEY"])  

    from config.db.connection import Mongo
    Mongo.init_app(app)

    from .public import public
    app.register_blueprint(public)

    from .libraries import libraries
    app.register_blueprint(libraries)

    from .auth import auth
    app.register_blueprint(auth, url_prefix="/auth/")

    ### ERRORS 
    from app.auth.routes import Errors
    app.register_error_handler(400, Errors.page_refresh)
    app.register_error_handler(404, Errors.page_not_found)
    app.register_error_handler(403, Errors.page_not_access)
    app.register_error_handler(401, Errors.page_need_arguments)
    app.register_error_handler(406, Errors.page_only_users_except_autor)
    app.register_error_handler(415, Errors.function_error_process)

    return app