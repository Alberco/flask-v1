from . import db


genero_man= db.Table('genero_manga',
                        db.Column('manga_id',db.Integer(),db.ForeignKey("manga.id"),primary_key=True),
                        db.Column('genero_id',db.Integer(),db.ForeignKey('genero.id'),primary_key=True)      
)
 
class Manga(db.Model):
    __tablename__ = "manga"
    id = db.Column(db.Integer(),primary_key=True,autoincrement=True)
    name_manga = db.Column(db.String(length=40),nullable=False)
    descripcion = db.Column(db.String(length=255))
    manga_genero = db.relationship('Genero',secondary=genero_man,lazy='subquery',backref=db.backref('genero',lazy=True))

    def __init__(self,name_manga,descripcion):
        self.name_manga =name_manga
        self.descripcion = descripcion

class Genero(db.Model):
    __tablename__ = "genero"
    id = db.Column(db.Integer(),primary_key=True,autoincrement=True)
    name_genero = db.Column(db.String(length=20),nullable=False)

    def __init__(self,name_genero):
        self.name_genero = name_genero
    
    
    
    