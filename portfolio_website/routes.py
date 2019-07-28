from flask import render_template

def route_home():
    return render_template("home.html")