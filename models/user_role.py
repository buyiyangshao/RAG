# models/user_role.py

from models import db


class UserRole(db.Model):
    __tablename__ = 'user_role'

    inner_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.role_id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)

    # 添加关系：可以通过 user_role.user 访问用户，通过 user_role.role 访问角色。外键约束
    user = db.relationship('User', back_populates='user_roles')
    role = db.relationship('Role', back_populates='user_roles')


    def to_dict(self) -> dict:
        return {
            'inner_id': self.inner_id,
            'user_id': self.user_id,
            'role_id': self.role_id
        }
