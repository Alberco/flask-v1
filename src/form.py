from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,SelectField
from wtforms.validators import  Length,DataRequired
from src.bdfunciones import  all_genero

list_generos = []

generos = all_genero()
for genero in generos:
    list_generos.append(genero.name_genero)
    

class Register_manga(FlaskForm):
    title = StringField(label='Name Manga',validators=[Length(min=3,max=40),DataRequired()])
    descripcion = StringField(label='Description Manga',validators=[Length(min=3,max=255),DataRequired()])
    genero = SelectField(label='Genero', choices=list_generos)
    submit = SubmitField(label='Enviar')
    
class Update_manga(FlaskForm):
    title = StringField(label='Name Manga',validators=[Length(min=3,max=40),DataRequired()])
    descripcion = StringField(label='Description Manga',validators=[Length(min=3,max=255),DataRequired()])
    submit = SubmitField(label='Update')
    