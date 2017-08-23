# coding=utf-8

from flask import Flask,render_template,request,flash
from flask_bootstrap import Bootstrap
from hello import  UserForm
import MySQLdb


app = Flask(__name__)
app.config["SECRET_KEY"]="hard to guess string"
bootstrap = Bootstrap(app)


@app.route("/",methods=["GET","POST"])
def index():
    form = UserForm()
    if form.validate_on_submit():
        name = form.name.data
        password = form.password.data
        age = form.age.data
        save(name,password,age)
        flash('Looks like you have save your name(%s)!'%name)
    return  render_template("index.html",form = form)


def save(name,password,age):
    db = MySQLdb.connect("localhost","root","123456","test")
    cursor = db.cursor();
    cursor.execute("INSERT INTO user (name,password,age) VALUES (%s,%s,%s)", (name,password,age))
    db.commit()
    db.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0",port=9000,debug=True)

