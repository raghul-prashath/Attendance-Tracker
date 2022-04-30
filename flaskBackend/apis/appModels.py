from . import *
        
#test
class test(Resource):
    def get(self):
        return {"message": "Hello World!"}, 200

#Register
class register(Resource):
    def post(self):
        rollNo = request.get_json()['rollNo']
        name = request.get_json()['name']
        programme = request.get_json()['programme']
        accYear = request.get_json()['accYear']
        password = request.get_json()['password']

        records = selectRoll(rollNo)

        def hasNumbers(inputString):
            return any(char.isdigit() for char in inputString)
        
        if(bool(hasNumbers(name)) == True or len(password) < 8):
            return {'message':'Bad Request','Format': 'False'}, 401

        if records == None:
            registerUser(rollNo, name, programme, accYear, password, 'user')
            access_token = create_access_token(identity = rollNo)
            resp=jsonify({'message':'registered successfully', 'Format': 'True'})
            set_access_cookies(resp,access_token)
            return make_response(resp, 200)

        else:
            return {'access_token': access_token, 'message':'user exist', 'Format': 'False'}, 401
            
# Login
class login(Resource):
    def post(self):
        rollNo = request.get_json()['rollNo']
        password = request.get_json()['password']
        records = selectRoll(rollNo)

        if records == None:
            return {'message':'Bad Request','Format': 'False'}, 401   

        elif bcrypt.check_password_hash(records[6],password):
            access_token = create_access_token(identity = rollNo)
            resp = jsonify({'access_token':access_token, 'message':'Login successfully', 'Format': 'True'})
            set_access_cookies(resp, access_token)
            return make_response(resp, 200)

        else:   
            return {'access_token': access_token, 'message':'invalid username or password', 'Format': 'False'}, 401

#Logout
class loggedout(Resource):
    @jwt_required
    def get(self):
        resp = jsonify(logout = True)
        unset_jwt_cookies(resp)
        return make_response(resp)

class tokenData(Resource):
    @jwt_required
    def get(self):
        rollNo = get_jwt_identity()
        data = getAttendance(rollNo)
        if data==None:
            return {'message':'Empty','Format': 'True'}, 200
        else:
            return {'rollNo' : data}, 200




