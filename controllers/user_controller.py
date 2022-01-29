from flask import Flask, render_template, redirect, request
from flask import Blueprint
from models.user import User
import repositories.user_repository as user_repository

users_blueprint = Blueprint("users", __name__)

@users_blueprint.route("/users")
def users():
    users = user_repository.select_all()
    return render_template("users/index.html", all_users = users)

@users_blueprint.route("/users/new", methods= ['GET'])
def new_user():
    return render_template("users/new_user.html")

@users_blueprint.route("/users", methods= ['POST'])
def create_user():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    user= User(first_name, last_name)
    user_repository.save(user)
    return redirect('/users')

@users_blueprint.route("/users/<id>/delete", methods= ['POST'])
def delete_task(id):
    user_repository.delete(id)
    return redirect('/users')