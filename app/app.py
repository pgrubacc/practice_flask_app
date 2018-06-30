from flask import Flask
from models import db
import random

# the all-important app variable:
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://dbuser:password@127.0.0.1:5432/postgres'
db.init_app(app)

@app.route("/")
def hello():
    return "This is a random number {0} \
           from 1 to 10".format(random.randint(1,10))

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=8080)

