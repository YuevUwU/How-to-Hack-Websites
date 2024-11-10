from flask import Flask, request, make_response, redirect, send_file
import base64
import pickle

app = Flask(__name__)
session_name = "pickle_session"

@app.route("/sauce")
def sauce():
    return send_file(__file__, mimetype="text/plain")


@app.route("/")
def main():
    session = request.cookies.get(session_name)
    if session == None:
        return '<form action="./login" method="POST">' +\
            '<p>Name: <input name="name" type="text"></p>' +\
            '<p>Age: <input name="age" type="number"></p>' +\
            '<button>Submit</button></form><hr><a href="./sauce">Source code</a>'

    else:
        user = pickle.loads(base64.b64decode(session))
        return f'<p>Name: {user["name"]}</p><p>Age: {user["age"]}</p>'


@app.route("/login", methods=['POST'])
def login():
    user = base64.b64encode(pickle.dumps({
        "name": request.form.get('name'),
        "age": int(request.form.get('age'))
    })).decode('utf-8')
    resp = make_response(redirect('./'))
    resp.set_cookie(session_name, user)
    return resp
