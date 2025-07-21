# models_function/role_function.py

from models import db
from models.role import Role
from loguru import logger

# logger.add("log.log", rotation="1 MB", encoding="utf-8")


# 新增角色
def add_role(role_name: str) -> Role | None:
    """
    :param role_name: 角色名称
    :return: 添加成功返回 role 对象，失败返回 None
    """
    existing = Role.query.filter_by(role_name=role_name).first()
    if existing:
        return None

    role = Role(role_name=role_name)
    try:
        db.session.add(role)
        db.session.commit()
        return role
    except Exception as e:
        # logger.error(e)
        db.session.rollback()
        return None


# 删除角色
def delete_role(role_id: int, role_name: str) -> Role | None:
    """
    :param role_id: 要删除的角色ID
    :param role_name: 要删除的角色名
    :return: 删除成功返回被删除的角色对象，失败返回 None
    """
    role = Role.query.filter_by(role_id=role_id, role_name=role_name).first()
    if not role:
        return None

    try:
        db.session.delete(role)
        db.session.commit()
        return role
    except Exception as e:
        # logger.error(e)
        db.session.rollback()
        return None


# 更新角色名称
def update_role(role_id: int, new_role_name: str) -> Role | None:
    """
    :param role_id: 要更新的角色ID
    :param new_role_name: 新的角色名
    :return: 更新成功返回新角色对象，失败返回 None
    """
    role = Role.query.filter_by(role_id=role_id).first()
    if not role:
        return None

    try:
        role.role_name = new_role_name
        db.session.commit()
        return role
    except Exception as e:
        # logger.error(e)
        db.session.rollback()
        return None


# 查询所有角色
def find_all_roles() -> list[Role] | None:
    """
    :return: 成功返回所有角色对象的列表，失败返回 None
    """
    try:
        roles = Role.query.all()
        return roles
    except Exception as e:
        # logger.error(e)
        return None


# 根据 role_id 查询角色
def find_role_by_id(role_id: int) -> Role | None:
    """
    :param role_id: 角色ID
    :return: 成功返回角色对象，失败返回 None
    """
    try:
        role = Role.query.filter_by(role_id=role_id).first()
        return role
    except Exception as e:
        # logger.error(e)
        return None


# 根据role_name查询角色
def find_role_by_name(role_name: str) -> Role | None:
    """
    :param role_name: 角色名
    :return: 成功返回角色对象，失败返回None
    """
    try:
        role = Role.query.filter_by(role_name=role_name).first()
        return role
    except Exception as e:
        # logger.error(e)
        return None


# 新增两个role（admin和normal）
def add_default_roles() -> list[Role] | None:
    """
    :return: 新增成功返回两个role对象的列表，失败返回None
    """
    admin_existing = Role.query.filter_by(role_name="admin").first()
    user_existing = Role.query.filter_by(role_name="user").first()
    if admin_existing and user_existing:
        return [admin_existing, user_existing]
    role1 = add_role("admin")
    role2 = add_role("user")
    if role1 and role2:
        return [role1, role2]
    else:
        return None
