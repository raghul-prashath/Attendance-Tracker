#Flask
from flask import Flask,request,render_template,redirect, url_for,flash,jsonify,make_response
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager,jwt_required,create_access_token
from flask_jwt_extended import get_jwt_identity,set_access_cookies, unset_jwt_cookies
from flask_restful import Resource, Api
from flask_admin import Admin, AdminIndexView
from flask_admin.menu import MenuLink
from flask_admin.contrib.sqla import ModelView
from flask_login import LoginManager,UserMixin,login_user,current_user,logout_user,login_required
#SQLAlchemy
from sqlalchemy import event
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin

app = Flask(__name__)

#CORS
CORS(app)

app.config.from_object("config.DevelopmentConfig")

bcrypt = Bcrypt(app)
jwt = JWTManager(app)
api = Api(app)
login_manager= LoginManager()
login_manager.init_app(app)
db = SQLAlchemy(app)


from apis.models import MyAdminIndexView
admin = Admin(app,name='Admin Panel',template_mode='bootstrap3',index_view=MyAdminIndexView())

from apis.handleDbms import Users,Course,Timetable
from apis.handleDbms import handleDb,getSpecialRights,SpecialRights,getAttendance
handleDb()
from apis.handleDbms import selectRoll,checkUserId,registerUser
from apis.handleAdmin import Controllers, UsersController, spController, timetableController,  courseController
from apis.handleAdmin import hashPass,load_user,adminLogin,adminLogout
from apis.appModels import register,login,loggedout,test
from apis.appModels import tokenData
from apis.handleAdminPanel import addView
from apis.routes import routesApi


routesApi()
addView()


if __name__=='__main__':
    app.run()
    

