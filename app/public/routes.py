from flask import render_template
from . import public

from flask_breadcrumbs import register_breadcrumb,default_breadcrumb_root
# Breadcrumbs load
default_breadcrumb_root(public, '.')

@public.route('/', methods=['GET'])
@register_breadcrumb(public, '.', 'Home')
def index():
    return render_template('index.html')

