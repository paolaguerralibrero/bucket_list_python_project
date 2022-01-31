from flask import Flask, render_template, redirect, request
from flask import Blueprint
from models.visit import Visit
import repositories.visit_repository as visit_repository
import repositories.country_repository as country_repository
import repositories.user_repository as user_repository


visits_blueprint = Blueprint("visits", __name__)


@visits_blueprint.route("/users/<user_id>")
def visited_countries(user_id):
    visited_countries = visit_repository.show_all(user_id)
    countries = country_repository.select_all()
    user = user_repository.select_by_id(user_id)
    return render_template("visits/index.html", all_visits = visited_countries, all_countries = countries, user = user)



@visits_blueprint.route("/visits/<user_id>", methods=['POST'])
def add_visited_country(user_id):
    user = user_repository.select_by_id(user_id)
    country_user_id = request.form['select_country']
    country = country_repository.select_by_id(country_user_id)
    visit = Visit(user, country, True)
    visit_repository.save(visit)
    return redirect('/users/'+ user_id)

@visits_blueprint.route("/visits/<visit_id>/<user_id>/delete", methods= ['GET'])
def delete_visit(visit_id, user_id):
    visit_repository.delete(visit_id)
    return redirect('/users/' + user_id)