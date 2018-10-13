from flask import Flask,jsonify,render_template,request
from flask_restful import Resource,Api
from entities import HelloWord,TodoSimple
 


app = Flask(__name__)
api = Api(app)


#  pdb.set_trace()
api.add_resource(HelloWord,'/')
api.add_resource(TodoSimple,  '/todo','/todo/<int:todo_id>')
 

# api.add_resource(TodoSimple,  '/todos/<todo_id>')




if __name__ == '__main__':
    app.run(
        debug=True,
        port=app.config['PORT'] if 'PORT' in app.config else 5000,
        host=app.config['BIND'] if 'BIND' in app.config else '127.0.0.1'
        )