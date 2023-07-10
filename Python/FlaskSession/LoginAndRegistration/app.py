from flask import Flask,jsonify,request
import csv

app = Flask(__name__)

def find_user(username):
    csv_file = 'userlist.csv'

    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['username'] == username:
                return True

    return False

def find_userandpassword(username,password):
    csv_file = 'userlist.csv'
    if(username != '' and password != ''):

        with open(csv_file, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                print(row)
                if row['username'] == username and row['password'] == password :
                    return True

    return False

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data['username']
    existing_user = find_user(username)
    if existing_user:
        return jsonify({'IsScucces':False, 'Message':'Username already exists'})

    csv_file = 'userlist.csv'
    fieldnames = ['username', 'name', 'gender', 'age', 'email', 'password']
    with open(csv_file, 'a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writerow(data)
        file.write('\n')

    return jsonify({'IsScucces':True, 'Message':'Registration successful'})

@app.route('/userlogin', methods=['POST'])
def login():
    userdata = request.get_json()
    print(userdata)
    username = userdata['username']
    password = userdata['password']
    if username == '':
        return jsonify({'IsScucces':False,'Message': 'Username is not be empty'})
        
    if username == '':
        return jsonify({'IsScucces':False,'Message': 'Password is not be empty'})
    isUserIsExist = find_userandpassword(username,password)
    if isUserIsExist:
        return jsonify({'IsScucces':True, 'Message':'Login successful'})
    
    return jsonify({'IsScucces':False,'Message': 'Username not found'})

if __name__ == '__main__':
    app.run(debug=True,port=8000)