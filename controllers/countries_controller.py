from flask import Flask, render_template, redirect, request
from flask import Blueprint
from models.user import User
from models.country import Country
import repositories.country_repository as country_repository

countries_blueprint = Blueprint("countries", __name__)


@countries_blueprint.route("/countries")
def countries():
    countries = country_repository.select_all()
    return render_template("countries/index.html", all_countries = countries)

@countries_blueprint.route("/countries/new", methods= ['GET'])
def new_country():
    return render_template("countries/new_country.html")

@countries_blueprint.route("/countries", methods= ['POST'])
def create_country():
    name = request.form['name']
    continent = request.form['continent']
    flag = request.form['flag']
    country= Country(name, continent, flag)
    country_repository.save(country)
    return redirect('/countries')

@countries_blueprint.route("/countries/<id>")
def show(id):
    country = country_repository.select_by_id(id)
    return render_template("countries/show_country.html", country = country)
