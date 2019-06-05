""" работа с формами """

from flask import Flask, render_template, request, url_for,flash, redirect

app=Flask(__name__)
app.secret_key = 'some_secret'

@app.route("/", methods=['GET'])
def index():
    name=request.args.get("name")
    email=request.args.get("email")
    go=request.args.get("go")

    if not email and go:
        flash('email is not sent')
            
    return render_template("forms.html", name=name, email=email, go=go)

@app.route("/url")
def url():
    return url_for('static', filename='style.css')

app.run(debug = True)