from flask import Flask,request,jsonify
from pymongo import MongoClient

client = MongoClient('mongodb+srv://abhi:@cluster0.bta0sbt.mongodb.net')
db = client['myshop']
itemcollection = db['items']

app = Flask(__name__)

@app.route('/api/item',methods=['POST'])
def insertitem():
    item = request.get_json()
    # print(item)
    # itemcollection.insert_one(item)
    itemcollection.insert_many(item)
    return jsonify({'IsSuccess':True,'ResponseCode':0,'Message':'Added Successfully'})

@app.route('/api/item',methods=['GET'])
def getitems():
    items = list(itemcollection.find({},{'_id':0}))
    # print(items)
    return jsonify({'IsSuccess':True,'ResponseCode':0,'Message':'Success','ResponseData':items})

if __name__ == '__main__':
    app.run(debug=True)




# from flask import Flask,jsonify,request
# from flask_sqlalchemy import SQLAlchemy
# import pymysql
# from flask_pymongo import PyMongo

# app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://abhi:abhi@localhost/devops'
# # app.config['MONGO_URI'] = 'mongodb://localhost:27017/devops'

# app.config['MONGO_URI'] = 'mongodb+srv://abhi:@cluster0.bta0sbt.mongodb.net/devops'

# db = SQLAlchemy(app)
# mongo = PyMongo(app)

# class Userdetails(db.Model):
    
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(80), unique=False, nullable=False)
#     username = db.Column(db.String(80), unique=True, nullable=False)
#     email = db.Column(db.String(120), unique=True, nullable=False)
#     gender = db.Column(db.String(50), unique=False, nullable=False)
#     age = db.Column(db.Integer, unique=False, nullable=False)
#     password = db.Column(db.String(200), unique=False, nullable=False)
#     def __repr__(self):
#         return '<User %r>' % self.username
    

# @app.route('/register', methods=['POST'])
# def register():
#     data = request.get_json()
#     print(data)
#     name = data['name']
#     username = data['username']
#     email = data['email']
#     gender = data['gender']
#     age = data['age']
#     password = data['password']
#     # user = Userdetails(name=name, username=username, email=email,gender=gender,age=age,password=password)

#     user = {
#         'name': name,
#         'username': username,
#         'email': email,
#         'gender': gender,
#         'age': age,
#         'password': password
#     }

#     mongo.db.userdetails.insert_one(user)

#     # db.session.add(user)
#     # db.session.commit()

#     return jsonify({'IsScucces':True, 'Message':'Registration successful'})


# if __name__ == '__main__':
#     pymysql.install_as_MySQLdb()
#     app.run(debug=True)


# def find_user(username):
#     csv_file = 'userlist.csv'

#     with open(csv_file, 'r') as file:
#         reader = csv.DictReader(file)
#         for row in reader:
#             if row['username'] == username:
#                 return True

#     return False

# def find_userandpassword(username,password):
#     csv_file = 'userlist.csv'
#     if(username != '' and password != ''):

#         with open(csv_file, 'r') as file:
#             reader = csv.DictReader(file)
#             for row in reader:
#                 print(row)
#                 if row['username'] == username and row['password'] == password :
#                     return True

#     return False

# @app.route('/register', methods=['POST'])
# def register():
#     data = request.get_json()
#     username = data['username']
#     existing_user = find_user(username)
#     if existing_user:
#         return jsonify({'IsScucces':False, 'Message':'Username already exists'})

#     csv_file = 'userlist.csv'
#     fieldnames = ['username', 'name', 'gender', 'age', 'email', 'password']
#     with open(csv_file, 'a', newline='') as file:
#         writer = csv.DictWriter(file, fieldnames=fieldnames)
#         writer.writerow(data)
#         file.write('\n')

#     return jsonify({'IsScucces':True, 'Message':'Registration successful'})

# @app.route('/userlogin', methods=['POST'])
# def login():
#     userdata = request.get_json()
#     print(userdata)
#     username = userdata['username']
#     password = userdata['password']
#     if username == '':
#         return jsonify({'IsScucces':False,'Message': 'Username is not be empty'})
        
#     if username == '':
#         return jsonify({'IsScucces':False,'Message': 'Password is not be empty'})
#     isUserIsExist = find_userandpassword(username,password)
#     if isUserIsExist:
#         return jsonify({'IsScucces':True, 'Message':'Login successful'})
    
#     return jsonify({'IsScucces':False,'Message': 'Username not found'})

# if __name__ == '__main__':
#     app.run(debug=True,port=8000)