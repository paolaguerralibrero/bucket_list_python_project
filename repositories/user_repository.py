from db.run_sql import run_sql

from models.user import User

def save(user):
    sql = "INSERT INTO users (first_name, last_name) VALUES (%s, %s) RETURNING *"
    values = [user.first_name, user.last_name]
    results = run_sql(sql, values)
    id = results[0][0]
    user.id = id
    return user

def select_all():
    users = []
    sql = "SELECT * FROM users"
    results = run_sql(sql)
    for row in results:
        user = User(row['first_name'], row['last_name'], row['id'])
        users.append(user)
    return users

def select_by_id(id):
    user = None
    sql = "SELECT * FROM users WHERE id= %s"
    result = run_sql(sql, [id])
    row = result[0]
    return User(row['first_name'], row['last_name'], row['id'])

def delete_all():
    sql = "DELETE FROM users"
    run_sql(sql)

def update(user):
    sql = "UPDATE users SET (first_name, last_name) = (%s, %s) WHERE id = %s"
    values = [user.first_name, user.last_name, user.id]
    run_sql(sql, values)

def delete(id):
    sql = "DELETE  FROM users WHERE id = %s"
    values = [id]
    run_sql(sql, values)