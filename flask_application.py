from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route ("/", methods = ['GET'])
def hello():
    return jsonify({"Greeting":"Hello World"})

@app.route ("/", methods = ['POST'])
def bye():
    return jsonify({"BYE":"Hello World"})

@app.route ("/abc/", methods = ['GET','POST'])
def abc():
    if request.method == 'GET':
        return jsonify({"Welcome":"GUEST!!!"})
    if request.method == 'POST':
        return jsonify({"Good Bye":"GUEST!!!"})

@app.route("/cube/<int:num>" , methods = ['GET'])
def cube(num):
    return jsonify({'result' : num**3})

if __name__ == '__main__':
    app.run(debug=True)
