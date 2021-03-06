from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
#prueba git
class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    fullName = db.Column(db.String(250), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    favoritos = db.relationship('Favoritos', lazy=True)

    def __repr__(self):
        return '<ID %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "fullName": self.fullName,
            "email": self.email,
            "favoritos": list(map(lambda x: x.serialize(), self.favoritos))
            # do not serialize the password, its a security breach
        }


class Characters(db.Model):
    __tablename__ = 'characters'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    height= db.Column(db.String(50))
    mass = db.Column(db.String(50))
    skin_color = db.Column(db.String(50))
    hair_color = db.Column(db.String(50))
    eye_color = db.Column(db.String(50))
    birth_year = db.Column(db.String(50))
    gender = db.Column(db.String(50))
    photoUrl = db.Column(db.String(500), nullable=False)
    favoritos = db.relationship('Favoritos', lazy=True)
    def __repr__(self):
        return '<Characters %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "height": self.height,
            "mass" : self.mass,
            "skin_color" : self.skin_color,
            "hair_color" : self.hair_color,
            "eye_color" : self.eye_color,
            "birth_year" : self.birth_year,
            "gender" : self.gender,
            "photoUrl" : self.photoUrl,
            "favoritos": list(map(lambda x: x.serialize(), self.favoritos))
            # do not serialize the password, its a security breach
        }

class Planets(db.Model):
    __tablename__ = 'planets'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    population= db.Column(db.String(50))
    terrain = db.Column(db.String(50))
    climate = db.Column(db.String(50))
    gravity = db.Column(db.String(50))
    galaxy = db.Column(db.String(50))
    surface_water = db.Column(db.String(50))
    orbital_period = db.Column(db.String(50))
    photoUrl = db.Column(db.String(500), nullable=False)
    favoritos = db.relationship('Favoritos')
    def __repr__(self):
        return '<Planets %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "population": self.population,
            "terrain" : self.terrain,
            "climate" : self.climate,
            "gravity" : self.gravity,
            "galaxy" : self.galaxy,
            "surface_water" : self.surface_water,
            "orbital_period" : self.orbital_period,
            "photoUrl" : self.photoUrl,
            "favoritos": list(map(lambda x: x.serialize(), self.favoritos))
            # do not serialize the password, its a security breach
        }



class Favoritos(db.Model):
    __tablename__ = 'favoritos'
    id = db.Column(db.Integer, primary_key=True) 
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    planets_id = db.Column(db.Integer,db.ForeignKey("planets.id"))
    characters_id = db.Column(db.Integer,db.ForeignKey("characters.id"))


    def __repr__(self):
        return '<Id %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "user_id" : self.user_id,
            "planets_id" : self.planets_id,
            "characters_id" : self.characters_id,
            # do not serialize the password, its a security breach
        }