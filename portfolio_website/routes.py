from flask import render_template


def route_home():
    return render_template("home.html")


def route_get_project(project_name):
    page = "projects_{}.html".format(project_name)
    return render_template(page)