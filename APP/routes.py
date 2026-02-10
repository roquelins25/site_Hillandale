from flask import Blueprint, render_template, request, jsonify, redirect, url_for, session
from .models.sup_client import supabase

main = Blueprint("main", __name__)

# =========================
# Página pública
# =========================
@main.route("/", methods=["GET"])
def index():
    return render_template("index.html")


# =========================
# Botão "Development Area"
# =========================
@main.route("/development", methods=["GET"])
def development_entry():
    """
    Entrada controlada da área de desenvolvimento.
    """
    if "user" in session:
        return redirect(url_for("main.dashboard"))

    return redirect(url_for("main.login"))


# =========================
# Login (acessado SOMENTE via /development)
# =========================
@main.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if not username or not password:
            return render_template(
                "login.html",
                error="Please enter both username and password."
            )

        result = (
            supabase
            .table("h_credential")
            .select("email","pass")
            .eq("email", username)
            .eq("pass", password)
            .execute()
        )

        if result.data:
            session["user"] = username 
            return redirect(url_for("main.dashboard"))

        return render_template(
            "login.html",
            error="Incorrect username and Password. Please try again."
        )
            

    return render_template("login.html")

# =========================
# Dashboard DEV (protegido)
# =========================
@main.route("/dashboard", methods=["GET"])
def dashboard():
    if "user" not in session:
        return redirect(url_for("main.development_entry"))

    return render_template("development.html")


# =========================
# Logout
# =========================
@main.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("main.index"))



