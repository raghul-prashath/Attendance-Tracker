from . import *


class SpecialRights(db.Model):
    __tablename__="specialRights"
    
    
    adminId= db.Column('adminId', db.Integer,primary_key=True)
    role=db.Column('role', db.String,unique=True, nullable=False)

    create = db.Column('create',db.Boolean)
    read = db.Column('read',db.Boolean)
    update = db.Column('update',db.Boolean)
    delete = db.Column('delete',db.Boolean)
    usersTable=db.Column('usersTable',db.Boolean)
    courseTable=db.Column('userLikeTable',db.Boolean)
    timeTable=db.Column('commentTable',db.Boolean)
    spTable=db.Column('spTable',db.Boolean)

    def __init__(self,adminId,role,create,read,update,delete,usersTable,courseTable,timeTable,spTable):
        self.adminId=adminId
        self.role = role
        self.create = create
        self.read = read
        self.update = update
        self.delete = delete
        self.usersTable=usersTable
        self.courseTable=courseTable
        self.timeTable=timeTable
        self.spTable=spTable


    
class Users(db.Model, UserMixin):
    __tablename__ = "users"
    userId = db.Column('userId',db.Integer, primary_key=True)
    adminId = db.Column('adminId',db.Integer, db.ForeignKey('specialRights.adminId'))
    roles = db.relationship("SpecialRights", backref='adminId_SpecialRights')
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
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')
        
    def get_id(self):
        return (self.adminId)


class Course(db.Model):
    __tablename__ = 'course'
    courseId = db.Column('courseId', db.Integer, primary_key=True)
    courseCode = db.Column('courseCode', db.String)
    courseName = db.Column('courseName', db.String)
    rollNo = db.Column('rollNo', db.String)
    totalP = db.Column('totalPresent', db.Integer)
    totalA = db.Column('totalAbsent', db.Integer)
    totalC = db.Column('totalClass', db.Integer)
    atPercent = db.Column('Percent', db.Integer)

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



        
# handleDb to Handle initial Db operations
def handleDb():
    db.create_all()    
    if not SpecialRights.query.all():
        db.session.add(SpecialRights(1,'admin',True,True,True,True,True,True,True,True))
        db.session.add(SpecialRights(2,'user',False,False,False,False,False,False,False,False))
        db.session.commit()
    if not Users.query.all():
        db.session.add(Users('18pd28','Raghul','Data Science',4,'25112000',1))
        db.session.commit()
        db.session.add(Users('18pd16','Lingesh','Data Science',4,'rjofficio',2))
        db.session.commit()
    


def getSpecialRights(adminId):
    rights=SpecialRights.query.filter_by(adminId=adminId)    
    records=[]
    for rows in rights:
        records.append((rows.adminId, rows.role, rows.create, rows.read, rows.update, rows.delete, rows.usersTable, rows.courseTable, rows.timeTable, rows.spTable))
    return records 


#Register user    
def registerUser(rollNo, name, programme, accYear, password, roles):
    exist=SpecialRights.query.filter_by(role=roles).first()    
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
