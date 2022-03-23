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
    __tablename__ = 'users'
    rollNo = db.Column(db.String(6),unique=True,primary_key=True)
    studentName = db.Column(db.String(40),unique=False)
    accYear = db.Column(db.Integer)
    programme = db.Column(db.String(40))
    password = db.Column(db.String(30),unique=False)
db.create_all()

class course(db.Model,UserMixin):
    __tablename__ = 'course'
    courseCode = db.Column(db.String(6),primary_key=True)
    courseName = db.Column(db.String(40))
    rollNo = db.column(db.String(6))
    totalP = db.column(db.Integer)
    totalA = db.column(db.Integer)
    totalC = db.column(db.Integer)
    attendancePercentage = db.column(db.Integer)
db.create_all()

class timetable(db.Model,UserMixin):
    __tablename__ = 'timetable'
    id = db.Column(db.Integer,primary_key=True)
    courseCode = db.Column(db.String(40), ForeignKey('parent.id'))
    accYear = db.Column(db.Integer)
    programme = db.Column(db.String(40))
    day = db.Column(db.String(40))
    stHour = db.Column(db.Integer)
    endHour = db.Column(db.Integer)
    stTime = db.Column(db.DateTime(40))
    endTime = db.Column(db.DateTime(40))
db.create_all()

class AdminHome(AdminIndexView):
    def is_accessible(self):
        return current_user.is_authenticated

user = Users(rollNo='18pd28',studentName='Raghul Prashath K A',accYear='4',programme='Data Science',password='25112000')
db.session.add(user)
db.session.commit()

admin = Admin(app, name='Attendance Tracker', template_mode='bootstrap3')
admin.add_view(ModelView(Users, db.session))
admin.add_view(ModelView(course, db.session))
admin.add_view(ModelView(timetable, db.session))

@login.user_loader
def load_user(id):
    return Users.query.get(id)

@app.route('/')
def home():
    return 'Welcome to Attendance'

if __name__ == '__main__':
    app.run(debug=True)