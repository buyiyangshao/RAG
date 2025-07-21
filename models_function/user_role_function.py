# models_function/user_role_function.py
from models.role import Role
from models.user import User
from models.user_role import UserRole
from models import db
from loguru import logger

# logger.add("log.log", rotation="1 MB", encoding="utf-8")


# 新增用户角色关联
def add_user_role(user_id: int, role_id: int) -> UserRole | None:
    """
    新增用户角色关联
    :param user_id: 用户ID
    :param role_id: 角色ID
    :return: 新增成功返回UserRole对象，失败返回None
    """
    try:
        user = User.query.filter_by(user_id=user_id).first()
        role = Role.query.filter_by(role_id=role_id).first()
        if not user or not role:
            # logger.warning("用户或角色不存在")
            return None
        existing = UserRole.query.filter_by(user_id=user_id, role_id=role_id).first()
        if existing:
            # logger.warning("用户角色关系已存在")
            return None

        user_role = UserRole(user_id=user_id, role_id=role_id)
        if user_role is None:
            # logger.warning("用户角色关系新建失败")
            return None
        db.session.add(user_role)
        db.session.commit()
        # logger.info("用户角色关系添加成功")
        return user_role
    except Exception as e:
        # logger.error(e)
        db.session.rollback()
        return None


# 删除用户角色关联
def delete_user_role_by_user_id(user_id: int) -> UserRole | None:
    """
    根据user_id删除用户角色
    :param user_id: 用户ID
    :return: 删除成功返回删除的UserRole对象，失败返回None
    """
    try:
        user_role = UserRole.query.filter_by(user_id=user_id).first()
        if not user_role:
            return None
        db.session.delete(user_role)
        db.session.commit()
        return user_role
    except Exception as e:
        # logger.error(e)
        db.session.rollback()
        return None


# 修改用户角色关联
def update_user_role(user_id: int, new_role_id: int) -> UserRole | None:
    """
    修改用户的角色
    :param user_id: 用户ID
    :param new_role_id: 新的角色ID
    :return: 修改成功返回新的UserRole对象，失败返回None
    """
    try:
        user_role = UserRole.query.filter_by(user_id=user_id).first()
        if not user_role:
            return None
        user_role.role_id = new_role_id
        db.session.commit()
        return user_role
    except Exception as e:
        # logger.error(e)
        db.session.rollback()
        return None


# 查询所有用户角色关联
def find_all_user_roles() -> list[UserRole] | None:
    """
    查询所有用户角色关系
    :return: 所有UserRole对象的列表，失败返回None
    """
    try:
        user_roles = UserRole.query.all()
        return user_roles
    except Exception as e:
        # logger.error(e)
        return None


# 根据user_id查询用户角色关联
def find_user_role_by_user_id(user_id: int) -> UserRole | None:
    """
    根据user_id查询用户角色
    :param user_id: 用户ID
    :return: 找到返回UserRole对象，失败返回None
    """
    try:
        user_role = UserRole.query.filter_by(user_id=user_id).first()
        return user_role
    except Exception as e:
        # logger.error(e)
        return None

