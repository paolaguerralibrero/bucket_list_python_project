from flask import Flask, render_template
app = Flask(__name__)
from controllers.user_controller import users_blueprint
from controllers.countries_controller import countries_blueprint

app.register_blueprint(users_blueprint)
app.register_blueprint(countries_blueprint)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
