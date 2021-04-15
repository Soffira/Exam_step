# from flask import Flask
# from flask_restful import Resource, Api, reqparse
import cherrypy

# app = Flask(__name__)
# api = Api(app)

userss = {
    '1': {
        'username': 'van',
        'email': 'vanbyvan@fmail.ru',
        'department': 'production',
        'date_joined': '2011-11-11T11:10:09' 
    },
    '2': {
        'username': 'billy',
        'email ': 'billyjeans@fmail.ru',
        'department': 'pr',
        'date_joined': '1983-03-02T12:12:53'
    },
    '3': {
        'username': 'max',
        'email ': 'maximus@fmail.ru',
        'department': 'production',
        'date_joined': '1999-05-29T14:14:28'
    },
    '4': {
        'username': 'leonard',
        'email ': 'leokapri@fmail.ru',
        'department': 'sales',
        'date_joined': '1974-12-11T14:45:32'
    }
}

    
class Users:
    def get(self, name=None, department=None):
        inf1 = []
        inf2 = []
        if name == None:
            for user in userss:
                inf1.append(userss[user])
        else:
            for user in userss:
                if name in userss[user]['username']:
                    inf1.append(userss[user])
        if department == None:
            for user in userss:
                inf2.append(userss[user])
        else:
            for user in userss:
                if department in userss[user]['department']:
                    inf2.append(userss[user])
        inf3 = []
        for i in inf1:
            if i in inf2:
                inf3.append(i)
        return ('data: %s' % inf3)

        if name == None and department == None:
            return ("Error: No id field provided. Please specify information")
    
    def POST(self, a, b):
        return 
    exposed = True
# api.add_resource(Users, '/users')

class Departments:
    def get(self, department=None):
        deps1 = []
        if name == None:
            for user in userss:
                inf1.append(userss[user])
        else:
            for user in userss:
                if name in userss[user]['username']:
                    inf1.append(userss[user])

# class Users(Resource):
#     def get(self):
#         return {'data': userss}, 200
# api.add_resource(Users, '/users')

# if __name__ == 'main':
#     app.run()

# if name == 'main':
def serv_start():
    cherrypy.tree.mount(
        Users(), '/api/users', {
            '/': 
                {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}
        }
    )
    return cherrypy #поменять  местами с закомиченным
    # cherrypy.config.update('{server.socket_host': '0.0.0.0', 'server.socket_port': 80})
    # cherrypy.engine.start()
    # cherrypy.engine.block()