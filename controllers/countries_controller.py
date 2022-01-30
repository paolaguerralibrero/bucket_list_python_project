from flask import Flask, render_template, redirect, request
from flask import Blueprint
from models.user import User
import repositories.country_repository as country_repository
from models.country import Country

countries_blueprint = Blueprint("countries", __name__)

@countries_blueprint.route("/countries")
def countries():
    country = country_repository.select_all()
    return render_template("countries/index.html", all_counties = country)

@countries_blueprint.route("/countries/new", methods= ['GET'])
def new_user():
    return render_template("countries/new_country.html")