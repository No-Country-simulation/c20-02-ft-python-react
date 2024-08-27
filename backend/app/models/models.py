from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Usuario(db.Model):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False) #hasshed
    rol = db.Column(db.String(50), nullable=False) #que roles vamos a tener?
    profile = db.relationship('Profile', uselist=False, back_populates='user')

#considerar hacer merge con tabla usuario por scope de referencias
class Profile(db.Modcel):
    __tablename__ = 'profiles'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20))
    email = db.Column(db.String(100))
    avatar = db.Column(db.String(255))
    user = db.relationship('Usuario', back_populates='profile')

class Tablero(db.Model): #Function of  tablero = proyecto?
    __tablename__ = 'tableros'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
    table_name = db.Column(db.String(100), nullable=False)
    table_type = db.Column(db.String(50), nullable=False) #si privado o public
    descripcion = db.Column(db.Text)

class Lista(db.Model):
    __tablename__ = 'listas'
    id = db.Column(db.Integer, primary_key=True)
    table_id = db.Column(db.Integer, db.ForeignKey('tableros.id'), nullable=False)
    # nombre = db.Column(db.String(100), nullable=False)
    # position = db.Column(db.Integer) to support drag-and-drop reordering.

class Tarjeta(db.Model):
    __tablename__ = 'tarjetas'
    id = db.Column(db.Integer, primary_key=True)
    table_id = db.Column(db.Integer, db.ForeignKey('listas.id'), nullable=False) #better be list_id if referencing 'listas'
    # difference between description, details and comments?
    description = db.Column(db.String(255), nullable=False)
    details = db.Column(db.Text)
    comments = db.Column(db.Text)
    members = db.Column(db.Text) #implement relational table user-card
    tags = db.Column(db.Text) #leave for the end: Optional-use as relation
    check = db.Column(db.String(50)) #add as table and a checklist items 
    date = db.Column(db.String(50)) #deadline - fields mode descriptive
    # add 'recordatorio' in days
    # position = db.Column(db.Integer)
    
#consider using table reference for easy querying
    # class MiembrosTarjeta(db.Model):
    #     __tablename__ = 'miembros_tarjeta'
    #     usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), primary_key=True)
    #     tarjeta_id = db.Column(db.Integer, db.ForeignKey('tarjetas.id'), primary_key=True)

class Comentario(db.Model):
    __tablename__ = 'comentarios'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
    card_id = db.Column(db.Integer, db.ForeignKey('tarjetas.id'), nullable=False)
    country = db.Column(db.String(50), unique=True)
    img = db.Column(db.String(255)) #can be null
    category = db.Column(db.String(50))
    # created_at = db.Column(db.DateTime, default=db.func.current_timestamp()) para hacer display en front y mostrar por orden 
    