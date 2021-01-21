import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__) #was dis?

# set base directory
basedir = os.path.abspath(os.path.dirname(__file__)) #?

# SQLite Database
DATABASE = 'sqlite:///' + os.path.join(
    basedir, 'db.wutang')

# DATABASE = 'postgresql://localhost/wutang'

app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #?

# init database
db = SQLAlchemy(app) #?

# init Marshmallow
marshmallow = Marshmallow(app)

DEBUG = True
PORT = 8000

@app.route('/') #?
def hello_world():
    return 'Hello World'
@app.route('/post', methods=['POST'])
@app.route('/post/<postid>', methods=['GET'])
def create_post(postid=None):
    from models import Post
    if postid == None:
        name = request.json['name']
        profile_name = request.json['profile_name']
        email = request.json['email']
        return Post.create_post(name, profile_name, email)
    else:
        return Post.get_post(postid)

if __name__ == '__main__':
    app.run(debug=DEBUG, port=PORT)
