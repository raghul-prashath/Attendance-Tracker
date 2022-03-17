from flask import Flask,redirect
from flask_admin import BaseView,expose,Admin,AdminIndexView
from flask_admin.contrib.sqla import ModelView
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin,login_user,logout_user,login_required,LoginManager,current_user

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///timetable.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'abc'
app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)

# https://stackoverflow.com/questions/71283071/how-to-restrict-admin-access-with-flask-admin


class users(db.Model,UserMixin):
    id = db.Column(db.Integer,primary_key=True)
    rollno = db.Column(db.String(200),unique=False,nullable=False)
    password = db.Column(db.String(200),unique=False,nullable=False)

class course(db.Model,UserMixin):
    id = db.Column(db.String(6),primary_key=True)
    name = db.Column(db.String(100),unique=False,nullable=False)
    
db.create_all()

class AdminHome(AdminIndexView):
    def is_accessible(self):
        return current_user.is_authenticated
    def inaccessible_callback(self,name,**kwargs):
        return redirect('/admin')

admin = Admin(app,name='Control',index_view=AdminHome())

@login_manager.user_loader
def user_loader(user_id):
    return users.query.get(int(user_id))

@app.route('/a')
def home():
    return 'asd'


if __name__ == '__main__':
    app.run(debug=True)