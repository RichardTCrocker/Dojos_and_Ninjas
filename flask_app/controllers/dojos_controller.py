from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.dojos_model import Dojo
from flask_app.models.ninjas_model import Ninja



@app.route('/')
@app.route('/dojos')
def all_dojos():
    all_dojos = Dojo.get_all()
    return render_template('index.html',all_dojos=all_dojos)


@app.route('/dojos/<int:id>/view')
def view_one_dojo(id):
    data = {
        'id':id
    }
    one_dojo = Dojo.one_dojos_ninjas(data)
    return render_template("dojos.html",one_dojo=one_dojo)

@app.route('/dojos/new', methods=['POST'])
def create_dojo():
    data = {
        'name' : request.form["name"]
    }
    id = Dojo.create(data)
    return redirect('/dojos')