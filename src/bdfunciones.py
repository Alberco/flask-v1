from src.models import  Manga,Genero
from src import db

def all_manga():
    list_manga = Manga.query.all()
    return list_manga

def all_genero():
    lista_genero = Genero.query.all()
    return lista_genero

def add_manga(name,des):
    manga_new = Manga(name_manga=name,descripcion=des)
    db.session.add(manga_new)
    db.session.commit()
    return manga_new


def delete_manga(id):
    manga_delete = Manga.query.get(id)
    db.session.delete(manga_delete)
    db.session.commit()
    return manga_delete



def update_manga(id,title,description):
    manga_update = Manga.query.get(id)
    manga_update.title = title
    manga_update.descripcion = description
    db.session.add(manga_update)
    db.session.commit()
    return manga_update


def select_manga(id):
    i = Manga.query.get(id)
    return i