from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.ninjas_model import Ninja
from flask_app.models.dojos_model import Dojo


@app.route('/ninjas')
def all_ninjas():
    all_dojos = Dojo.get_all()
    return render_template('ninjas.html', all_dojos=all_dojos)

@app.route('/ninjas/new', methods=['POST'])
def create_ninja():
    Ninja.create(request.form)
    return redirect(f'/dojos/{request.form["dojo_id"]}/view')