import uuid
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from sqlalchemy.dialects.postgresql import UUID
from . import db
from werkzeug.security import generate_password_hash, check_password_hash

class Usuario(db.Model, UserMixin):
    __tablename__ = 'usuario'

    id_usuario = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    nombre = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    contraseña = db.Column(db.String(200), nullable=False)
    tipo_usuario = db.Column(db.String(20), nullable=False)
    creado_en = db.Column(db.DateTime, server_default=db.func.now())

    peliculas = db.relationship('Pelicula', backref='autor', lazy=True)

    def get_id(self):
        return str(self.id_usuario)

    def definir_contrasena(self, password):
        self.contraseña = generate_password_hash(password)

    def verificar_contrasena(self, password):
        return check_password_hash(self.contraseña, password)

    def __repr__(self):
        return f'<Usuario {self.email}>'

class Pelicula(db.Model):
    __tablename__ = 'pelicula'

    id_pelicula = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    titulo = db.Column(db.String(200), nullable=False)
    descripcion = db.Column(db.Text, nullable=True)
    imagen_url = db.Column(db.String(255))
    fecha_subida = db.Column(db.DateTime, server_default=db.func.now())

    id_usuario = db.Column(UUID(as_uuid=True), db.ForeignKey('usuario.id_usuario'), nullable=False)

    def __repr__(self):
        return f'<Pelicula {self.titulo}>'

class Comentario(db.Model):
    __tablename__ = 'comentario'

    id_comentario = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    contenido = db.Column(db.Text, nullable=False)
    fecha = db.Column(db.DateTime, server_default=db.func.now())

    id_usuario = db.Column(UUID(as_uuid=True), db.ForeignKey('usuario.id_usuario'), nullable=False)
    id_pelicula = db.Column(UUID(as_uuid=True), db.ForeignKey('pelicula.id_pelicula'), nullable=False)

    usuario = db.relationship('Usuario', backref='comentarios')
    pelicula = db.relationship('Pelicula', backref='comentarios')

class Calificacion(db.Model):
    __tablename__ = 'calificacion'

    id_calificacion = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    puntuacion = db.Column(db.Integer, nullable=False)

    id_usuario = db.Column(UUID(as_uuid=True), db.ForeignKey('usuario.id_usuario'), nullable=False)
    id_pelicula = db.Column(UUID(as_uuid=True), db.ForeignKey('pelicula.id_pelicula'), nullable=False)

    __table_args__ = (db.UniqueConstraint('id_usuario', 'id_pelicula', name='unique_calificacion'),)

    usuario = db.relationship('Usuario', backref='calificaciones')
    pelicula = db.relationship('Pelicula', backref='calificaciones')

class Favorito(db.Model):
    __tablename__ = 'favorito'

    id_favorito = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    id_usuario = db.Column(UUID(as_uuid=True), db.ForeignKey('usuario.id_usuario'), nullable=False)
    id_pelicula = db.Column(UUID(as_uuid=True), db.ForeignKey('pelicula.id_pelicula'), nullable=False)

    __table_args__ = (db.UniqueConstraint('id_usuario', 'id_pelicula', name='unique_favorito'),)

    usuario = db.relationship('Usuario', backref='favoritos')
    pelicula = db.relationship('Pelicula', backref='favoritos')
