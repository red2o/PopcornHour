from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from app.models import Usuario, Pelicula, Comentario, Calificacion, Favorito
from app.forms import LoginForm, RegisterForm, UploadMovieForm
from app import db
from app.decorators import moderador_required
from datetime import datetime
from app.forms import ComentarioForm, RatingForm
import uuid

main = Blueprint('main', __name__)
auth = Blueprint('auth', __name__)

@main.route('/')
def index():
    if current_user.is_authenticated:
        return redirect(url_for('main.catalogo'))
    return render_template('index.html')

@main.route('/catalogo')
@login_required
def catalogo():
    peliculas = Pelicula.query.all()
    return render_template('catalogo.html', peliculas=peliculas)

@main.route('/pelicula/<uuid:id>', methods=['GET', 'POST'])
@login_required
def movie_detail(id):
    pelicula = Pelicula.query.get_or_404(id)

    # Formularios
    comentario_form = ComentarioForm()
    rating_form = RatingForm()

    # Procesar calificación
    if rating_form.validate_on_submit() and rating_form.submit.data:
        nueva_calificacion = Calificacion(
            id_usuario=current_user.id_usuario,
            id_pelicula=id,
            puntuacion=int(rating_form.puntuacion.data)
        )
        db.session.add(nueva_calificacion)
        db.session.commit()
        flash('¡Gracias por tu calificación!', 'success')
        return redirect(url_for('main.movie_detail', id=id))

    # Procesar comentario
    if comentario_form.validate_on_submit() and comentario_form.submit.data:
        nuevo_comentario = Comentario(
            id_usuario=current_user.id_usuario,
            id_pelicula=id,
            contenido=comentario_form.contenido.data,
            fecha=datetime.utcnow()
        )
        db.session.add(nuevo_comentario)
        db.session.commit()
        flash('Comentario agregado correctamente.', 'success')
        return redirect(url_for('main.movie_detail', id=id))

    # Obtener datos
    comentarios = Comentario.query.filter_by(id_pelicula=id).all()
    calificaciones = Calificacion.query.filter_by(id_pelicula=id).all()
    promedio = (
        sum([c.puntuacion for c in calificaciones]) / len(calificaciones)
        if calificaciones else 0
    )

    # Verificar si es favorito
    favorito = Favorito.query.filter_by(id_usuario=current_user.id_usuario, id_pelicula=id).first()
    es_favorito = favorito is not None

    return render_template(
        'movie_detail.html',
        pelicula=pelicula,
        comentarios=comentarios,
        promedio=promedio,
        es_favorito=es_favorito,
        comentario_form=comentario_form,
        rating_form=rating_form
    )


@main.route('/perfil')
@login_required
def perfil():
    favoritos = Favorito.query.filter_by(id_usuario=current_user.id_usuario).all()
    return render_template("perfil.html", usuario=current_user, favoritos=favoritos)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))

    form = LoginForm()
    if form.validate_on_submit():
        usuario = Usuario.query.filter_by(email=form.email.data).first()
        if usuario and usuario.verificar_contrasena(form.password.data):
            login_user(usuario)
            print("Tipo de usuario autenticado:", usuario.tipo_usuario)

            # Redirección según tipo
            if usuario.tipo_usuario.strip().lower() == 'moderador':
                return redirect(url_for('main.moderators_panel'))
            else:
                return redirect(url_for('main.catalogo'))
        else:
            flash('Credenciales incorrectas.', 'danger')
    return render_template('login.html', form=form)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Sesión cerrada.', 'info')
    return redirect(url_for('main.index'))

@auth.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))

    form = RegisterForm()
    if form.validate_on_submit():
        nuevo_usuario = Usuario(
            nombre=form.nombre.data,
            email=form.email.data,
            tipo_usuario=form.tipo_usuario.data
        )
        nuevo_usuario.definir_contrasena(form.password.data)
        db.session.add(nuevo_usuario)
        db.session.commit()
        flash('Cuenta creada correctamente. Ahora puedes iniciar sesión.', 'success')
        return redirect(url_for('auth.login'))
    return render_template('register.html', form=form)

@main.route('/moderador')
@login_required
def moderators_panel():
    if current_user.tipo_usuario != 'moderador':
        flash('Acceso denegado.', 'danger')
        return redirect(url_for('main.index'))
    peliculas = Pelicula.query.filter_by(id_usuario=current_user.id_usuario).all()
    return render_template('moderators_panel.html', peliculas=peliculas, user=current_user)

@main.route('/favoritos')
@login_required
def ver_favoritos():
    favoritos = Favorito.query.filter_by(id_usuario=current_user.id_usuario).all()
    peliculas = [f.pelicula for f in favoritos if f.pelicula]
    return render_template("favoritos.html", peliculas=peliculas)

@main.route('/favorito/<uuid:id_pelicula>', methods=['POST'])
@login_required
def toggle_favorito(id_pelicula):
    favorito = Favorito.query.filter_by(id_usuario=current_user.id_usuario, id_pelicula=id_pelicula).first()

    if favorito:
        db.session.delete(favorito)
    else:
        nuevo_favorito = Favorito(id_usuario=current_user.id_usuario, id_pelicula=id_pelicula)
        db.session.add(nuevo_favorito)

    db.session.commit()
    return redirect(url_for('main.movie_detail', id=id_pelicula))

@main.route('/subir', methods=['GET', 'POST'])
@login_required
@moderador_required
def subir_pelicula():
    form = UploadMovieForm()
    if form.validate_on_submit():
        nueva_pelicula = Pelicula(
            id_pelicula=uuid.uuid4(),
            titulo=form.titulo.data,
            descripcion=form.descripcion.data,
            imagen_url=form.imagen_url.data,
            id_usuario=current_user.id_usuario,
            fecha_subida=datetime.utcnow()
        )
        db.session.add(nueva_pelicula)
        db.session.commit()
        flash('Película subida correctamente.', 'success')
        return redirect(url_for('main.moderators_panel'))
    return render_template('upload_movie.html', form=form)
