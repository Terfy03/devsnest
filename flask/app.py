from flask import Flask, request, jsonify, redirect
 
app = Flask(__name__)
 
 
@app.route('/')
def hello_world():
    return "hello world"
 
@app.route('/user')
def hello_world2():
    return "user page loaded"
 
# @app.route('/postman', methods=['GET','POST'])
# def hello_world3():
#     data = request.get_data()
#     return 'Hello World!' + request.method + str(data)
 
# @app.route('/postman2', methods=['POST'])
# def hello_world4():
#     data = request.json
#     data["KSHITIZ"] = "FLASK@123"
#     return jsonify(data)
 
@app.route('/greet/<int:user>', methods=['GET'])
def hello_world5(user):
    return str(user+1)
 
@app.route('/goback', methods=['GET'])
def hello_world7():
    return redirect('/')
 
@app.route('/isPal/<string:s>', methods=['GET'])
def hello_world8(s):
    return "YES ^_^" if s == s[::-1] else "NO -.-"

original = []
@app.route("/stringConcat/<string:s>", methods = ['GET'])
def concat(s):
	original.append(s)
	return s

@app.route("/finalString", methods= ['GET'])
def finalString():
	return  "-".join(original)
 
 
 
 
if __name__ == '__main__':
    app.run()