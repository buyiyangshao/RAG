# models/role.py

from models import db


class Role(db.Model):
    __tablename__ = 'roles'

    role_id = db.Column(db.Integer, primary_key=True, unique=True)
    role_name = db.Column(db.String(255), unique=True)

    user_roles = db.relationship('UserRole', back_populates='role', cascade='all, delete-orphan')

    def to_dict(self) -> dict:
        return {
            'role_id': self.role_id,
            'role_name': self.role_name
        }
