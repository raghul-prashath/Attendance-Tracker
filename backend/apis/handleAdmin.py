from . import *

class Controllers(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated
    def inaccessible_callback(self,name,**kwargs):
        return redirect(url_for('adminLogin'))


class UsersController(Controllers):
    column_list = ('adminId', 'rollNo', 'name', 'programme', 'accYear')
    def is_accessible(self):
        records=getSpecialRights(current_user.userId)
        for record in records:
            if bool(record[6]):
                return True
        return False
        
    @property
    def can_create(self):
        records=getSpecialRights(current_user.userId)
        for record in records:
            if bool(record[2]):
                return True
        return False

    @property
    def can_read(self):
        records=getSpecialRights(current_user.userId)
        for record in records:
            if bool(record[3]):
                return True
        return False

    @property
    def can_edit(self):
        records=getSpecialRights(current_user.userId)
        for record in records:
            if bool(record[4]):
                return True
        return False

    @property
    def can_delete(self):
        records=getSpecialRights(current_user.userId)
        for record in records:
            if bool(record[5]):
                return True
        return False

class courseController(Controllers):
    def is_accessible(self):
        records=getSpecialRights(current_user.userId)
        for record in records:
            if bool(record[7]):
                return True
        return False
        
    @property
    def can_create(self):
        records=getSpecialRights(current_user.userId)
        for record in records:
            if bool(record[2]):
                return True
        return False

    @property
    def can_read(self):
        records=getSpecialRights(current_user.userId)
        for record in records:
            if bool(record[3]):
                return True
        return False
        
    @property
    def can_edit(self):
        records=getSpecialRights(current_user.userId)
        for record in records:
            if bool(record[4]):
                return True
        return False

    @property
    def can_delete(self):
        records=getSpecialRights(current_user.userId)
        for record in records:
            if bool(record[5]):
                return True
        return False

class timetableController(Controllers):
    def is_accessible(self):
        records=getSpecialRights(current_user.userId)
        for record in records:
            if bool(record[8]):
                return True
        return False
        
    @property
    def can_create(self):
        records=getSpecialRights(current_user.userId)
        for record in records:
            if bool(record[2]):
                return True
        return False

    @property
    def can_read(self):
        records=getSpecialRights(current_user.userId)
        for record in records:
            if bool(record[3]):
                return True
        return False
        
    @property
    def can_edit(self):
        records=getSpecialRights(current_user.userId)
        for record in records:
            if bool(record[4]):
                return True
        return False

    @property
    def can_delete(self):
        records=getSpecialRights(current_user.userId)
        for record in records:
            if bool(record[5]):
                return True
        return False


class spController(Controllers):
    column_list = ('role','adminId','create','read','update','delete','usersTable','courseTable','timeTable')
    def is_accessible(self):
        records=getSpecialRights(current_user.userId)
        for record in records:
            if bool(record[9]):
                return True
        return False
        
    @property
    def can_create(self):
        records=getSpecialRights(current_user.userId)
        for record in records:
            if bool(record[2]):
                return True
        return False

    @property
    def can_read(self):
        records=getSpecialRights(current_user.userId)
        for record in records:
            if bool(record[3]):
                return True
        return False
        
    @property
    def can_edit(self):
        records=getSpecialRights(current_user.userId)
        for record in records:
            if bool(record[4]):
                return True
        return False

    @property
    def can_delete(self):
        records=getSpecialRights(current_user.userId)
        for record in records:
            if bool(record[5]):
                return True
        return False


@event.listens_for(Users.password,'set',retval=True)
def hashPass(target,value,oldvalue,initiator):
    if value != oldvalue:
        return bcrypt.generate_password_hash(value).decode('utf-8')
    return value
    
@login_manager.user_loader
def load_user(id):
    return Users.query.filter_by(userId=id).first()

@app.route('/',methods=['POST','GET'])
def adminLogin():    
    if request.method== 'POST':
        rollNo = request.form.get('rollNo')
        password = request.form.get('password')
        records = selectRoll(rollNo)
        user = Users.query.filter_by(rollNo=rollNo).first()

        if records == None:
            flash('Invalid credentials')
            return render_template('login.html')

        elif bcrypt.check_password_hash(records[6], password):
            if records[0]!=2:
                login_user(user)
                flash('Logged in successfully.')
                return redirect(url_for('admin.index'))
            else:
                flash('Invalid credentials')
                return render_template('login.html')

        else:   
            flash('Invalid credentials')
            return render_template('login.html')

    return render_template('login.html')

@app.route('/logout')
@login_required
def adminLogout():    
    logout_user()
    flash('Logged out successfully.')
    return redirect(url_for('adminLogin'))



