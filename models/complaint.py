from database.database import db


class Complaint(db.Model):
    __tablename__ = "complaints"

    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(200), nullable=False)

    description = db.Column(db.Text, nullable=False)

    category = db.Column(db.String(100), nullable=False)

    location = db.Column(db.String(200), nullable=False)

    image = db.Column(db.String(255), nullable=True)

    status = db.Column(db.String(50), default="Pending")

    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    # Relationship with User
    user = db.relationship("User", backref="complaints")

    created_at = db.Column(db.DateTime, server_default=db.func.now())

    def __repr__(self):
        return f"<Complaint {self.title}>"