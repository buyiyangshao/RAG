# models/chat_session.py

from models import db


class ChatSession(db.Model):
    __tablename__ = 'chat_sessions'

    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True)
    chat_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    chat_type = db.Column(db.String(255))

    # 定义关系
    user = db.relationship('User', back_populates='chat_sessions')

    def to_dict(self) -> dict:
        return {
            'user_id': self.user_id,
            'chat_id': self.chat_id,
            'title': self.title,
            'chat_type': self.chat_type
        }
