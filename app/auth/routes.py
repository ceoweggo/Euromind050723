from flask import render_template,flash,make_response,redirect,url_for

class Errors():
    def function_error_process(e):
        flash("¡Ups! Ha ocurrido un error inesperado y no se puedo realizar la acción", "danger")
        r = make_response(redirect(url_for('public.index')))
        r.headers.set('Content-Security-Policy', "default-src 'self'")
        return r

    def page_refresh(e):
        return render_template('errors/400.html'), 400

    def page_need_arguments(e):
        return render_template('errors/401.html', title="Se ha producido un error al cargar la función. Vuelva a intentarlo"), 401

    def page_not_access(e):
        return render_template('errors/403.html', title="¡No tienes autorización para acceder!"), 403

    def page_not_found(e):
        return render_template('errors/404.html', title="Página no encontrada"),404

    def page_only_users_except_autor(e):
        return render_template('errors/406.html'), 406