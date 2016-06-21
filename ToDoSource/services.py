from random import randint
import hashlib
from userservices import UserORM
from groupservices import GroupORM


def get_unique_code():
    # logger.info("Inside get_unique_code method")
    code_str_limit = "0123456789ZBYCXDWVFUGTHSRJQKPLMN"
    app_str = 'APPLICATION-DEVELOPER'
    code_prefix = 'APP'

    for i in range(0, 11):
        if i == 1 or i == 3 or i == 5:
            code_prefix += str(code_str_limit[randint(0, len(code_str_limit) - 1)])
        else:
            str_from_app_str = app_str[randint(0, len(app_str) - 1)]
            if str_from_app_str == 'I' or str_from_app_str == 'E':
                code_prefix += str(code_str_limit[randint(0, len(code_str_limit) - 1)])
            else:
                code_prefix += str_from_app_str
    # logger.info("Found code %s"%code_prefix)
    return code_prefix


def get_new_access_token():
    # logger.info("Inside get_new_promotion_code method")
    user_orm = UserORM()
    access_token = get_unique_code()
    while user_orm.is_access_token_exists(access_token):
        access_token = get_unique_code()
    return access_token


def get_md5_string(input_string):
    m = hashlib.md5()
    m.update(input_string.encode('utf-8'))
    return m.hexdigest()


def get_group_unique_code():
    # logger.info("Inside get_unique_code method")
    code_str_limit = "0123456789"
    app_str = 'BOARDGROUP'
    code_prefix = 'GRP'

    for i in range(0, 8):
        if i == 1 or i == 3 or i == 5:
            code_prefix += str(code_str_limit[randint(0, len(code_str_limit) - 1)])
        else:
            str_from_app_str = app_str[randint(0, len(app_str) - 1)]
            code_prefix += str_from_app_str
    return code_prefix


def get_new_group_code():
    group_orm = GroupORM()
    group_code = get_group_unique_code()
    while group_orm.is_group_code_exists(group_code):
        group_code = get_group_unique_code()
    return group_code


def handle_uploaded_file(file_obj, image_name):
    try:
        destination = open(image_name, 'wb+')
        for chunk in file_obj.chunks():
            destination.write(chunk)
        destination.close()
    except:
        raise
