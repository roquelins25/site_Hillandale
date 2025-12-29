from flask import Blueprint, render_template, request, jsonify, redirect, url_for, session

main = Blueprint("main", __name__)

@main.route("/", methods=["GET"])
def get_data():
    return render_template("index.html")