from flask import Flask, render_template, redirect, url_for, flash
from config import Config
from database.database import db
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, login_required, current_user

from models.user import User
from models.complaint import Complaint

# Blueprints
from routes.auth import auth
from routes.complaints import complaints

app = Flask(__name__)
app.config.from_object(Config)

# Initialize Extensions
db.init_app(app)
bcrypt = Bcrypt(app)

login_manager = LoginManager()
login_manager.login_view = "auth.login"
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# Register Blueprints
app.register_blueprint(auth)
app.register_blueprint(complaints)


# ================= HOME =================
@app.route("/")
def home():
    return render_template("index.html")


# ================= DASHBOARD =================
@app.route("/dashboard")
@login_required
def dashboard():
    return render_template("dashboard.html")


# ================= PROFILE =================
@app.route("/profile")
@login_required
def profile():
    return render_template("profile.html")


# ================= ANALYTICS =================
@app.route("/analytics")
@login_required
def analytics():

    total = Complaint.query.count()

    pending = Complaint.query.filter_by(
        status="Pending"
    ).count()

    progress = Complaint.query.filter_by(
        status="In Progress"
    ).count()

    resolved = Complaint.query.filter_by(
        status="Resolved"
    ).count()

    return render_template(
        "analytics.html",
        total=total,
        pending=pending,
        progress=progress,
        resolved=resolved
    )


# ================= ADMIN PANEL =================
@app.route("/admin")
@login_required
def admin():

    if current_user.role.lower() != "admin":
        flash("Access Denied!", "danger")
        return redirect(url_for("dashboard"))

    complaints = Complaint.query.order_by(
        Complaint.created_at.desc()
    ).all()

    return render_template(
        "admin.html",
        complaints=complaints
    )


# ================= UPDATE STATUS =================
@app.route("/admin/update/<int:id>/<status>")
@login_required
def update_status(id, status):

    if current_user.role.lower() != "admin":
        flash("Access Denied!", "danger")
        return redirect(url_for("dashboard"))

    complaint = Complaint.query.get_or_404(id)

    complaint.status = status

    db.session.commit()

    flash("Complaint Status Updated Successfully!", "success")

    return redirect(url_for("admin"))


# ================= RUN APP =================
if __name__ == "__main__":

    with app.app_context():
        db.create_all()

    app.run(debug=True)