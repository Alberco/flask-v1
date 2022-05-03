from src import todo,db
from flask import render_template,request,redirect,url_for,flash
from src.bdfunciones import all_manga,delete_manga,add_manga,select_manga
from src.form import Register_manga,Update_manga


@todo.route('/',methods=['GET'])
@todo.route('/home',methods=['GET'])
def index():
    return render_template('index.html')

@todo.route('/list',methods=['GET'])
def todo_list():
    mangas = all_manga()
    return render_template('list_manga.html',mangas = mangas)

@todo.route('/add',methods=['GET','POST'])
def register_todo():
    form = Register_manga()
    if  request.method == 'POST' and form.validate_on_submit():
        title = form.title.data
        des = form.descripcion.data
        add_manga(title,des)
        return redirect(url_for('todo_list'))
    return render_template('add_manga.html',form=form)

@todo.route('/delete/<string:id>',methods=['GET','POST'])
def delete_todo(id):
    delete_manga(id)
    flash('Contact deleted successfully!')
    return redirect(url_for('todo_list'))

@todo.route('/update/<string:id>',methods=['GET','POST'])
def update_todo(id):
    item = select_manga(id)
    form = Update_manga(obj=item)
    if  request.method == 'POST' and form.validate_on_submit():
        item.name_manga = form.title.data
        item.descripcion = form.descripcion.data
        db.session.add(item)
        db.session.commit()
        return redirect(url_for('todo_list'))
    form.title.data = item.name_manga
    form.descripcion.data = item.descripcion
    return render_template('update.html',form=form)