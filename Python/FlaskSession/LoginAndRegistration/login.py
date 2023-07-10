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


@app.route('/userlogin', methods=['POST'])
def login():
    userdata = request.get_json()
    print(userdata)
    username = userdata['username']
    password = userdata['password']
    print( find_user(username))
    isUserIsExist = find_user(username)
    if isUserIsExist:
        return 'Login successful'
    

    return 'Username not found'

if __name__ == '__main__':
    app.run(debug=True,port=5000)