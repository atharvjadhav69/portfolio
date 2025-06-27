from flask import Flask, request, send_file
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('mongodb+srv://atharvj084:7nVxW9Ai5vN36XQ5@cluster0.5zdzhvd.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
db = client['portfolio_db']
collection = db['contacts']

@app.route('/')
def index():
    return send_file('index.html')   
@app.route('/submit', methods=['POST'])
def submit():
    data = request.form


    name = data['namequery']    
    email = data['email']
    number = data['Phone number']
    Address = data['Address']
    message = data['message']

    collection.insert_one({
        'name': name,
        'email': email,
        'Phone number' :number,
        'Address': Address,
        'message': message
    })

    return send_file('thanaku.png')

if __name__ == '__main__':
    app.run(debug=True)
    




 