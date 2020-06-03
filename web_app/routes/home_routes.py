# web_app/routes/home_routes.py

from flask import Blueprint

home_routes = Blueprint("home_routes", __name__)

@home_routes.route("/")
def index():
    print("VISITING THE HOME PAGE")
    x = 2 + 2
    return f"Hello World! {x}"

@home_routes.route("/about")
def about():
    print("VISITING THE ABOUT PAGE")
    return "About me"
