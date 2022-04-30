from . import *  

def routesApi():
    api.add_resource(register,'/api/users/register')
    api.add_resource(login,'/api/users/login')
    api.add_resource(test,'/api/test')
    api.add_resource(tokenData,'/api/data')
    api.add_resource(loggedout,'/api/users/logout')
    
    
