from . import *  

def routesApi():
    api.add_resource(register,'/users/register')
    api.add_resource(login,'/users/login')
    api.add_resource(test,'/test')
    api.add_resource(tokenData,'/data')
    api.add_resource(loggedout,'/users/logout')
    
    
