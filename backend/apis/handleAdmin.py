from . import *

class Controllers(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated
    def inaccessible_callback(self,name,**kwargs):
        return redirect(url_for('adminLogin'))
        
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
        if records[1]!=2:
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



