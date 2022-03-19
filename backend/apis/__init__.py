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
login = LoginManager(app)


class Users(db.Model,UserMixin):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    rollno = db.Column(db.String(6),unique=True)
    name = db.Column(db.String(40),unique=False)
    year = db.Column(db.Integer,nullable=False)
    program = db.Column(db.String(40),nullable=False)
    password = db.Column(db.String(30),unique=False)
db.create_all()

class course(db.Model,UserMixin):
    id = db.Column(db.String(6),primary_key=True)
    code = db.Column(db.String(6),nullable=False)
    name = db.Column(db.String(40),nullable=False)
db.create_all()

class timetable(db.Model,UserMixin):
    id = db.Column(db.String(6),primary_key=True)
    year = db.Column(db.Integer,nullable=False)
    program = db.Column(db.String(40),nullable=False)
    day = db.Column(db.String(40),nullable=False)
    hour = db.Column(db.String(40),nullable=False)
    stTime = db.Column(db.DateTime(40),nullable=False)
    endTime = db.Column(db.DateTime(40),nullable=False)
db.create_all()

class AdminHome(AdminIndexView):
    def is_accessible(self):
        return current_user.is_authenticated

user = Users(rollno='18pd28',name='Raghul',year='4',program='Data Science',password='25112000')
db.session.add(user)
db.session.commit()

admin = Admin(app, name='microblog', template_mode='bootstrap3')
admin.add_view(ModelView(Users, db.session))
admin.add_view(ModelView(course, db.session))
admin.add_view(ModelView(timetable, db.session))


@login.user_loader
def load_user(id):
    return Users.query.get(id)

@app.route('/')
def home():
    return 'Welcome to Attendance Tracker'


    

if __name__ == '__main__':
    
    app.run(debug=True)