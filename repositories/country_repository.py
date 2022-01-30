from db.run_sql import run_sql

from models.country import Country

def save(country):
    sql = "INSERT INTO countries (country_name) VALUES (%s) RETURNING *"
    values = [country.country_name]
    results = run_sql(sql, values)
    id = results[0][0]
    country.id = id
    return country

def select_all():
    countries = []
    sql = "SELECT * FROM countries"
    results = run_sql(sql)
    for row in results:
        user = Country(row['country_name'], row['id'])
        countries.append(user)
    return countries

def select_by_id(id):
    country = None
    sql = "SELECT * FROM countries WHERE id= %s"
    result = run_sql(sql, [id])
    row = result[0]
    return Country(row['country_name'], row['id'])

def delete_all():
    sql = "DELETE FROM countries"
    run_sql(sql)

def update(country):
    sql = "UPDATE countries SET (country_name) = (%s) WHERE id = %s"
    values = [country.country_name, country.id]
    run_sql(sql, values)

def delete(id):
    sql = "DELETE  FROM countries WHERE id = %s"
    values = [id]
    run_sql(sql, values)