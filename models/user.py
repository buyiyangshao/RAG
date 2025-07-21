# models/user.py

from models import db


class User(db.Model):
    __tablename__ = 'users'

    # user_id 作为主键，自增，唯一，非空
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True, unique=True, nullable=False)

    # user_mail 唯一，非空
    user_mail = db.Column(db.String(255), unique=True, nullable=False)

    user_name = db.Column(db.String(255), nullable=False)
    user_password = db.Column(db.String(255), nullable=False)

    # 关系定义保持不变
    chat_sessions = db.relationship('ChatSession', back_populates='user', cascade='all, delete-orphan')
    user_roles = db.relationship('UserRole', back_populates='user', cascade='all, delete-orphan')

    def to_dict(self) -> dict:
        return {
            'user_mail': self.user_mail,
            'user_id': self.user_id,
            'user_name': self.user_name,
            'user_password': self.user_password
        }
