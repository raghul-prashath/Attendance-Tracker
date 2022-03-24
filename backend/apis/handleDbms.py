from . import *
        
class Roles(db.Model):
    __tablename__ = "roles"
    adminId= db.Column('adminId', db.Integer,primary_key=True)
    role=db.Column('role', db.String,unique=True, nullable=False)
    
    def __init__(self, role):
        self.role=role
    
class Users(db.Model, UserMixin):
    __tablename__ = "users"
    userId = db.Column('userId',db.Integer, primary_key=True)
    adminId = db.Column('adminId',db.Integer, db.ForeignKey('roles.adminId'))
    roles = db.relationship("Roles", backref='adminId_roles')
    name = db.Column('name', db.String)
    programme = db.Column('programme', db.String)
    rollNo = db.Column('rollNo', db.String, unique=True)
    accYear = db.Column('accYear', db.Integer)
    password = db.Column('password', db.String)
    
    def __init__(self, rollNo, name, programme, accYear, password, adminId):
        self.adminId=adminId
        self.name = name
        self.programme = programme
        self.rollNo = rollNo
        self.accYear = accYear
        self.password = password
        
    def get_id(self):
        return (self.userId)

class Course(db.Model):
    __tablename__ = 'course'
    courseId = db.Column('courseId', db.Integer, primary_key=True)
    courseCode = db.Column('courseCode', db.String)
    courseName = db.Column('courseName', db.String)
    rollNo = db.column('rollNo', db.String)
    totalP = db.column('totalPresent', db.Integer)
    totalA = db.column('totalAbsent', db.Integer)
    totalC = db.column('totalClass', db.Integer)
    atPercent = db.column('Percent', db.Integer)

    def __init__(self, courseCode, courseName, rollNo, totalP, totalA, totalC, atPercent):
        self.courseCode = courseCode
        self.courseName = courseName
        self.rollNo = rollNo
        self.totalP = totalP
        self.totalA = totalA
        self.totalC = totalC
        self.atPercent = atPercent 
        
    def get_id(self):
        return (self.courseId)

class Timetable(db.Model):
    __tablename__ = 'timetable'
    classId = db.Column('classId', db.Integer, primary_key=True)
    courseCode = db.Column('courseCode', db.String)
    accYear = db.Column('accYear', db.Integer)
    programme = db.Column('programme', db.String)
    day = db.Column('day', db.String)
    stHour = db.Column('stHour', db.Integer)
    endHour = db.Column('endHour', db.Integer)
    stTime = db.Column('stTime', db.DateTime)
    endTime = db.Column('endTime', db.DateTime)
    classRoom = db.Column('roomName', db.String)

    def __init__(self, courseCode, accYear, Programme, day, stHour, endHour, stTime, endTime, classRoom):
        self.courseCode = courseCode
        self.accYear = accYear
        self.Programme = Programme
        self.day = day
        self.stHour = stHour
        self.endHour = endHour
        self.stTime = stTime
        self.endTime = endTime 
        self.classRoom = classRoom 
        
    def get_id(self):
        return (self.classId)

db.create_all()

# handleDb to Handle initial Db operations
def handleDb():
    if not Roles.query.all():
        db.session.add(Roles('admin'))
        db.session.commit()
        db.session.add(Roles('user'))
        db.session.commit()
    if not Users.query.all():
        db.session.add(Users('18pd28','Raghul','Data Science',4,'25112000',2))
        db.session.commit()
        db.session.add(Users('18pd16','Lingesh','Data Science',4,'rjofficio',1))
        db.session.commit()

#Register user    

def registerUser(rollNo, name, programme, accYear, password, roles):
    exist=Roles.query.filter_by(role=roles).first()    
    if exist:
        db.session.add(Users(rollNo, name, programme, accYear, password, exist.adminId))
        db.session.commit()
    
#Select email to check if there is no matching email   
def selectRoll(rollNo):
    user=Users.query.filter_by(rollNo=rollNo).first()
    if user:
        return [user.adminId,user.userId,user.rollNo,user.name,user.programme,user.accYear,user.password]
    else:
        return None

#check user Id
def checkUserId(userId):
    userId=Users.query.filter_by(userId=userId).first()
    if userId:
        return 1
    else:
        return 0
