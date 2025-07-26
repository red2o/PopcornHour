from flask import redirect, url_for, flash
from flask_login import current_user
from functools import wraps

def moderador_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated:
            flash("Debes iniciar sesión primero.", "warning")
            return redirect(url_for('auth.login'))
        elif current_user.tipo_usuario != 'moderador':
            flash("Acceso denegado. Solo para moderadores.", "danger")
            return redirect(url_for('main.index'))
        return f(*args, **kwargs)
    return decorated_function
