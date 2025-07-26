from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, TextAreaField
from wtforms.validators import DataRequired, Email, EqualTo, Length
from wtforms import RadioField

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Contraseña', validators=[DataRequired()])
    submit = SubmitField('Iniciar Sesión')

class RegisterForm(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired(), Length(min=2, max=100)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Contraseña', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirmar Contraseña', validators=[
        DataRequired(), EqualTo('password')
    ])
    tipo_usuario = SelectField('Tipo de Usuario', choices=[('estandar', 'Estándar'), ('moderador', 'Moderador')])
    submit = SubmitField('Registrarse')

class UploadMovieForm(FlaskForm):
    titulo = StringField('Título', validators=[DataRequired(), Length(min=1, max=200)])
    descripcion = TextAreaField('Descripción', validators=[DataRequired()])
    imagen_url = StringField('URL del Póster', validators=[DataRequired()])
    submit = SubmitField('Publicar Película')

class ComentarioForm(FlaskForm):
    contenido = TextAreaField('Comentario', validators=[DataRequired(), Length(min=1)])
    submit = SubmitField('Enviar Comentario')

class RatingForm(FlaskForm):
    puntuacion = RadioField('Calificación', choices=[
        ('1', '⭐'), ('2', '⭐⭐'), ('3', '⭐⭐⭐'), ('4', '⭐⭐⭐⭐'), ('5', '⭐⭐⭐⭐⭐')
    ], validators=[DataRequired()])
    submit = SubmitField('Calificar')