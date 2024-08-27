from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Usuario(db.Model):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    rol = db.Column(db.String(50), nullable=False)
    profile = db.relationship('Profile', uselist=False, back_populates='user')

class Profile(db.Modcel):
    __tablename__ = 'profiles'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    rut_dni = db.Column(db.String(50), unique=True)
    phone = db.Column(db.String(20))
    address = db.Column(db.String(255))
    email = db.Column(db.String(100))
    avatar = db.Column(db.String(255))
    user = db.relationship('Usuario', back_populates='profile')

class Tablero(db.Model):
    __tablename__ = 'tableros'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
    table_name = db.Column(db.String(100), nullable=False)
    table_type = db.Column(db.String(50), nullable=False)

class Lista(db.Model):
    __tablename__ = 'listas'
    id = db.Column(db.Integer, primary_key=True)
    table_id = db.Column(db.Integer, db.ForeignKey('tableros.id'), nullable=False)

class Tarjeta(db.Model):
    __tablename__ = 'tarjetas'
    id = db.Column(db.Integer, primary_key=True)
    table_id = db.Column(db.Integer, db.ForeignKey('listas.id'), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    details = db.Column(db.Text)
    comments = db.Column(db.Text)
    members = db.Column(db.Text)
    tags = db.Column(db.Text)
    check = db.Column(db.String(50))
    date = db.Column(db.String(50))

class Comentario(db.Model):
    __tablename__ = 'comentarios'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
    card_id = db.Column(db.Integer, db.ForeignKey('tarjetas.id'), nullable=False)
    country = db.Column(db.String(50), unique=True)
    img = db.Column(db.String(255))
    category = db.Column(db.String(50))
