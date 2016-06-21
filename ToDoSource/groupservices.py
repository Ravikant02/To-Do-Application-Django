__author__ = 'ravikant'
from models import GroupTbl
import datetime


class GroupORM(object):

    def get_groups_of_user(self, user_id):
        result = GroupTbl.objects.filter(user_id=user_id)
        if len(result) > 0:
            return result
        else:
            return None

    def get_group_details(self, group_id):
        result = GroupTbl.objects.filter(group_id=group_id)
        if len(result) > 0:
            return result[0]
        else:
            return None

    def update_group(self, group_tbl, group_helper):
        group_tbl.group_name = group_helper.group_name
        group_tbl.user_id = group_helper.user_id
        group_tbl.group_code = group_helper.group_code
        group_tbl.lastupd_dttm = group_helper.lastupd_dttm
        group_tbl.created_dttm = group_helper.created_dttm

    def add_group(self, user_id, group_name, group_code):
        group = GroupTbl()
        group.group_name = group_name
        group.user_id = user_id
        group.group_code = group_code
        group.lastupd_dttm = datetime.datetime.now()
        group.created_dttm = datetime.datetime.now()

        try:
            group.save()
        except Exception as ex:
            raise ex
        return group

    def is_group_code_exists(self, group_code):
        result = GroupTbl.objects.filter(group_code=group_code)
        if result:
            return True
        return False

    def get_group_details_by_group_code(self, group_code):
        result = GroupTbl.objects.filter(group_code=group_code)
        if len(result) > 0:
            return result[0]
        else:
            return None


class GroupHelper(object):

    def __init__(self, group_name, user_id, group_code, lastupd_dttm, created_dttm):
        self.group_name = group_name
        self.group_code = group_code
        self.user_id = user_id
        self.lastupd_dttm = lastupd_dttm
        self.created_dttm = created_dttm
