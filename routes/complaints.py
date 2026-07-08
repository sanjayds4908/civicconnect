import os

from flask import Blueprint, render_template, request, redirect, url_for, flash, current_app
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename

from database.database import db
from models.complaint import Complaint

complaints = Blueprint("complaints", __name__)


# ================= REPORT COMPLAINT =================
@complaints.route("/report", methods=["GET", "POST"])
@login_required
def report():

    if request.method == "POST":

        filename = None

        # Upload Image
        if "image" in request.files:
            file = request.files["image"]

            if file.filename != "":
                filename = secure_filename(file.filename)

                upload_folder = os.path.join(
                    current_app.root_path,
                    "static",
                    "uploads"
                )

                os.makedirs(upload_folder, exist_ok=True)

                file.save(os.path.join(upload_folder, filename))

        complaint = Complaint(
            title=request.form["title"],
            description=request.form["description"],
            category=request.form["category"],
            location=request.form["location"],
            image=filename,
            user_id=current_user.id
        )

        db.session.add(complaint)
        db.session.commit()

        flash("Complaint Submitted Successfully!", "success")

        return redirect(url_for("complaints.my_complaints"))

    return render_template("report_issue.html")


# ================= MY COMPLAINTS =================
@complaints.route("/my-complaints")
@login_required
def my_complaints():

    complaints_list = Complaint.query.filter_by(
        user_id=current_user.id
    ).order_by(
        Complaint.created_at.desc()
    ).all()

    return render_template(
        "complaint_history.html",
        complaints=complaints_list
    )


# ================= COMPLAINT DETAILS =================
@complaints.route("/complaint/<int:id>")
@login_required
def complaint_details(id):

    complaint = Complaint.query.get_or_404(id)

    # Allow only owner or admin
    if complaint.user_id != current_user.id and current_user.role != "admin":
        flash("Access Denied!", "danger")
        return redirect(url_for("complaints.my_complaints"))

    return render_template(
        "complaint_details.html",
        complaint=complaint
    )