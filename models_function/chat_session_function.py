# models_function/chat_session_function.py

from models import db
from models.chat_session import ChatSession
from loguru import logger

# logger.add("log.log", rotation="1 MB", encoding="utf-8")


# 新增一个chat_session
def add_chat_session(user_id: int, chat_id: int, title: str = "title", chat_type: str = "normal") -> ChatSession | None:
    """
    :param chat_type:
    :param user_id: 用户id
    :param chat_id: 聊天id
    :param title: 聊天的主题 title
    :return: 返回新增的chat_session对象，如果新增失败则返回None
    """
    existing = ChatSession.query.filter_by(user_id=user_id, chat_id=chat_id).first()
    if existing:
        return None

    chat_session = ChatSession(user_id=user_id, chat_id=chat_id, title=title, chat_type=chat_type)  # 改为关键字参数
    try:
        db.session.add(chat_session)
        db.session.commit()
        return chat_session
    except Exception as e:
        db.session.rollback()
        return None


# 删除一个chat_session
def delete_chat_session(user_id: int, chat_id: int) -> ChatSession | None:
    """
    删除指定 chat_session
    :param user_id: 用户 ID
    :param chat_id: 聊天会话 ID
    :return: 删除成功返回该对象，失败返回 None
    """
    session = ChatSession.query.filter_by(user_id=user_id, chat_id=chat_id).first()
    if not session:
        # logger.error("chat_session 不存在")
        return None

    try:
        db.session.delete(session)
        db.session.commit()
        return session
    except Exception as e:
        # logger.error(e)
        db.session.rollback()
        return None


# 更新一个chat_session
def update_chat_session(user_id: int, chat_id: int, new_title: str) -> ChatSession | None:
    """
    更新 chat_session 的标题
    :param user_id: 用户 ID
    :param chat_id: 聊天会话 ID
    :param new_title: 新的标题
    :return: 成功返回更新后的对象，失败返回 None
    """
    session = ChatSession.query.filter_by(user_id=user_id, chat_id=chat_id).first()
    if not session:
        # logger.error("chat_session 不存在")
        return None

    try:
        session.title = new_title
        db.session.commit()
        return session
    except Exception as e:
        # logger.error(e)
        db.session.rollback()
        return None


# 查找所有chat_session
def find_all_chat_sessions() -> list[ChatSession] | None:
    """
    :return: 所有记录组成的列表，失败返回 None
    """
    try:
        sessions = ChatSession.query.all()
        return sessions
    except Exception as e:
        # logger.error(e)
        return None


# 根据user_id 查找他所有的session
def find_chat_sessions_by_user_id(user_id: int) -> list[ChatSession] | None:
    """
    :param user_id:
    :return: ChatSession 的列表 或None
    """
    try:
        return ChatSession.query.filter_by(user_id=user_id).all()
    except Exception as e:
        # logger.error(e)
        return None


# 查找Chat Session列表中chat_id的最大值
def get_max_chat_id(user_chat_sessions: list[ChatSession]) -> int:
    """
    获取用户所有会话中的最大会话ID
    :param user_chat_sessions: 用户所有会话列表
    :return: 最大会话ID，若列表为空则返回0
    """
    if len(user_chat_sessions) == 0:
        return 0
    return max(session.chat_id for session in user_chat_sessions)


# 根据id查找一个chat_session
def find_single_chat_session_by_id(user_id: int, chat_id: int) -> ChatSession | None:
    """
    查询指定 user_id 的特定 chat_session
    :param user_id: 用户 ID
    :param chat_id: 聊天会话 ID
    :return: chat_id 存在时返回匹配对象；失败返回 None
    """
    try:
        return ChatSession.query.filter_by(user_id=user_id, chat_id=chat_id).first()
    except Exception as e:
        # logger.error(e)
        return None


# 设置chat_type
def update_chat_type(user_id: int, chat_id: int, chat_type: str) -> ChatSession | None:
    """
    更新 chat_session 的 chat_type
    :param user_id: 用户 ID
    :param chat_id: 聊天会话 ID
    :param chat_type: 聊天类型
    :return: 成功返回更新后的对象，失败返回 None
    """
    session = ChatSession.query.filter_by(user_id=user_id, chat_id=chat_id).first()
    if not session:
        # logger.error("chat_session 不存在")
        return None

    try:
        session.chat_type = chat_type
        db.session.commit()
        return session
    except Exception as e:
        # logger.error(e)
        db.session.rollback()
        return None
