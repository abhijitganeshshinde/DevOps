from flask import Flask,request,jsonify
from pymongo import MongoClient

client = MongoClient('mongodb+srv://abhi:@cluster0.bta0sbt.mongodb.net')
db = client['myshop']
itemcollection = db['items']

app = Flask(__name__)

@app.route('/hello')
def helloRoute():
    return jsonify('Hello World')

@app.route('/api/item',methods=['POST'])
def item():
    item = request.get_json()
    print(item)
    itemcollection.insert_one(jsonify(item))
    return jsonify(item)


if __name__ == '__main__':
    app.run(debug=True)

