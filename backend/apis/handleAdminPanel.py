from . import * 

#Admin Panel
def addView():
    admin.add_view(Controller(Roles, db.session))
    admin.add_view(Controller(Users, db.session))
    admin.add_view(Controller(Course, db.session))
    admin.add_view(Controller(Timetable, db.session))

    admin.add_link(MenuLink(name='Logout',url="/logout"))
