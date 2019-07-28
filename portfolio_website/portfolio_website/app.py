from flask import Flask
import portfolio_website.routes as routes

# create flask app
app = Flask(__name__)

# define all routes with implementations in the routes file
@app.route("/")
@app.route("/home")
def _route_home():
    return routes.route_home()
