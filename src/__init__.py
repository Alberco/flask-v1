from flask import Flask 
from flask_sqlalchemy  import SQLAlchemy
from flask_migrate import Migrate

user = "Guardar en variable de entorno"
password = "Guardar en variable de entorno"

todo = Flask(__name__)
todo.config['SECRET_KEY'] = "kokpkdpaskdkaopds"
todo.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{user}:{password}@localhost:5432/manga_todo"
todo.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(todo)
db.init_app(todo)
migrate = Migrate()
migrate.init_app(todo,db)


from  src import router