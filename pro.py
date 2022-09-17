
from flask import Flask, jsonify, request
app = Flask(__name__)

tasks = [{
    "Contact": "9288890987",
    "Name": "John Doe",
    "done": False,
    "id": 1
}, {
    "Contact": "930894083",
    "Name": "Ryan Doe",
    "done": False,
    "id": 2
}]

@app.route('/addData', methods = ['POST'])
def addTask ():
    if(not request.json):
        return jsonify ({
            'status ' : 'error',
            'message ' : 'please provide the data '
        })

    task = {
        'id' : tasks [-1] ["id"] +1,
        'Name': request.json.get('Contact',""),
        'done':False

    }
    tasks.append(task)
    return jsonify ({
            'status ' : 'success',
            'message ' : 'data added successfully '
        })
@app.route('/getData')
def getData ():
    return jsonify({
        'data ': tasks
    })

if (__name__=='__main__'):
    app.run()

    