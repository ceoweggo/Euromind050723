from flask import Blueprint
libraries = Blueprint('libraries', __name__, template_folder='templates')

from app.libraries import routes