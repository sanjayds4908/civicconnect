from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required
from models.user import User
from database.database import db

auth = Blueprint("auth", __name__)

# ================= REGISTER =================
@auth.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        full_name = request.form["full_name"]
        email = request.form["email"]
        phone = request.form["phone"]
        password = request.form["password"]

        user_exists = User.query.filter_by(email=email).first()
        if user_exists:
            flash("Email already registered!", "danger")
            return redirect(url_for("auth.register"))

        user = User(
            full_name=full_name,
            email=email,
            phone=phone,
            role="user"
        )
        user.set_password(password)

        db.session.add(user)
        db.session.commit()

        flash("Account created successfully!", "success")
        return redirect(url_for("auth.login"))

    return render_template("register.html")


# ================= LOGIN =================
@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        # 🔥 ADMIN LOGIN (HARD CODED)
        if email == "admin@gmail.com" and password == "admin@123":
            user = User.query.filter_by(email=email).first()

            if not user:
                user = User(
                    full_name="Admin",
                    email=email,
                    phone="0000000000",
                    role="admin"
                )
                user.set_password(password)
                db.session.add(user)
                db.session.commit()

            login_user(user)
            flash("Admin login successful!", "success")
            return redirect("/admin")

        # NORMAL USER LOGIN
        user = User.query.filter_by(email=email).first()

        if user and user.check_password(password):
            login_user(user)
            flash("Login successful!", "success")
            return redirect("/dashboard")

        flash("Invalid email or password", "danger")

    return render_template("login.html")


# ================= LOGOUT =================
@auth.route("/logout")
@login_required
def logout():
    logout_user()
    flash("Logged out successfully", "info")
    return redirect(url_for("auth.login"))