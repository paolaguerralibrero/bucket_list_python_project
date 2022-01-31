from db.run_sql import run_sql
from models.visit import Visit
import repositories.country_repository as country_repository
import repositories.user_repository as user_repository

def save(visit):
    sql = "INSERT INTO visit ( user_id, country_id, visited ) VALUES ( %s, %s, %s ) RETURNING id"
    values = [visit.user.id, visit.country.id, visit.visited]
    results = run_sql( sql, values )
    visit.id = results[0]['id']
    return visit

def show_all(user_id):
    visits = []
    sql = "SELECT * FROM visit WHERE user_id= %s"
    results = run_sql(sql, [user_id])
    user = user_repository.select_by_id(user_id)
    for row in results:
        country = country_repository.select_by_id(row['country_id'])
        visit = Visit(user, country, row['visited'], row['id'])
        visits.append(visit)
    return visits

def delete(id):
    sql = "DELETE  FROM visit WHERE id = %s"
    values = [id]
    run_sql(sql, values)