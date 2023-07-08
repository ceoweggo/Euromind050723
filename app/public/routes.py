from flask import render_template
from . import public
from config.db.connection import Mongo
from datetime import datetime

from flask_breadcrumbs import register_breadcrumb,default_breadcrumb_root
# Breadcrumbs load
default_breadcrumb_root(public, '.')

@public.route('/', methods=['GET'])
@register_breadcrumb(public, '.', 'Home')
def index():
    person_id = '0001'
    my_application_data = {
        'person_id': int(person_id),
        'name': 'Gabriela',
        'surname': 'Kandeva',
        'created': datetime.now()
    }

    if Mongo.db.users.insert_one(my_application_data):
        print("All was ok")
    else:
        print("something was wrong")

    return render_template('index.html')

