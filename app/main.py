from flask import Flask
import random

# the all-important app variable:
app = Flask(__name__)

@app.route("/")
def hello():
    return "This is a random number {0} \
           from 1 to 10".format(random.randint(1,10))

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=8080)

