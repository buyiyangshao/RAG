# models_function/user_function.py


from models import db
from models.user import User
from loguru import logger


# logger.add("log.log", rotation="1 MB", encoding="utf-8")


# 新增用户
def add_user(user_mail: str, user_name: str, user_password: str) -> User | None:
    """
    :param user_mail: user_mail做主键
    :param user_name: 用户名
    :param user_password:  密码（明文）
    :return:  返回新增的用户对象，新增失败则返回None
    """
    # 检查用户是否已存在
    existing = User.query.filter_by(user_mail=user_mail).first()
    if existing:
        return None
    # 创建新用户
    user = User(user_mail=user_mail, user_name=user_name, user_password=user_password)
    try:
        db.session.add(user)
        db.session.commit()
        return user
    except Exception as e:
        # logger.error(e)
        db.session.rollback()
        return None


# 删除用户
def delete_user(user_id: int) -> User | None:
    """
    :param user_id: 要删除的用户ID
    :return: 删除成功返回被删除的用户对象，失败返回 None
    """
    user = User.query.filter_by(user_id=user_id).first()
    if not user:
        return None

    try:
        db.session.delete(user)
        db.session.commit()
        return user
    except Exception as e:
        # logger.error(e)
        db.session.rollback()
        return None


# 更新用户名和密码
def update_user(user_id: int, user_name: str, user_password: str, user_mail: str) -> User | None:
    """
    :param user_id: 要更新的用户ID
    :param user_mail: 新的邮箱
    :param user_name: 新的用户名
    :param user_password: 新的密码
    :return: 更新成功返回更新后的用户对象，失败返回 None
    """
    user = User.query.filter_by(user_id=user_id).first()
    if user == None:
        return None

    # 检查邮箱是否被别人使用
    if user.user_mail != user_mail:
        if User.query.filter_by(user_mail=user_mail).first():
            # logger.error("邮箱已存在")
            return None
    # 如果邮箱未更改，无需处理邮箱冲突问题

    try:
        user.user_name = user_name
        user.user_password = user_password
        user.user_mail = user_mail
        db.session.commit()
        return user
    except Exception as e:
        # logger.error(e)
        db.session.rollback()
        return None


# 查询所有用户
def find_all_user() -> list[User] | None:
    """
    :return: 返回所有用户对象的列表，失败返回 None
    """
    try:
        users = User.query.all()
        return users
    except Exception as e:
        # logger.error(e)
        return None


# 根据user_id查找用户
def find_user_by_id(user_id: int) -> User | None:
    """
    :param user_id: 要查找的用户ID
    :return: 找到返回用户对象，找不到或异常返回 None
    """
    try:
        user = User.query.filter_by(user_id=user_id).first()
        return user
    except Exception as e:
        # logger.error(e)
        return None


# login 输入user_mail和user_password来登录
def login_user(user_mail: str, user_password: str) -> User | None:
    """
    登录验证
    :param user_mail: 用户邮箱
    :param user_password: 密码（明文）
    :return: 验证成功返回用户对象，失败返回 None
    """
    try:
        user = User.query.filter_by(user_mail=user_mail).first()
        if not user:
            # logger.error("用户不存在")
            return None
        if user and user.user_password == user_password:
            return user
        else:
            # logger.error("密码错误")
            return None
    except Exception as e:
        # logger.error(e)
        return None


# 根据mail读取用户id
def get_id_by_mail(user_mail: str) -> User | None:
    """
    根据邮箱获取用户ID
    :param user_mail: 用户邮箱
    :return: 找到返回用户ID，找不到或异常返回 None
    """
    try:
        user = User.query.filter_by(user_mail=user_mail).first()
        if not user:
            # logger.error("用户不存在")
            return None
        return user.user_id
    except Exception as e:
        # logger.error(e)
        return None
