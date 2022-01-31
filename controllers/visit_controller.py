from flask import Flask, render_template, redirect, request
from flask import Blueprint
from models.visit import Visit
import repositories.visit_repository as visit_repository
import repositories.country_repository as country_repository

visits_blueprint = Blueprint("visits", __name__)


@visits_blueprint.route("/users/<user_id>")
def visited_countries(user_id):
    visited_countries = visit_repository.show_all(user_id)
    countries = country_repository.select_all()
    return render_template("visits/index.html", all_visits = visited_countries, all_countries = countries)