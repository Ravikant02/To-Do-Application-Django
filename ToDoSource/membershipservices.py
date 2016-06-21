from models import MembershipTbl


class MemberShipORM(object):

    def update_member(self, member_ship_tbl, member_ship_helper):
        member_ship_tbl.group_id = member_ship_helper.group_id
        member_ship_tbl.group_name = member_ship_helper.group_name
        member_ship_tbl.user_id = member_ship_helper.user_id
        member_ship_tbl.user_name = member_ship_helper.user_name
        member_ship_tbl.lastupd_dttm = member_ship_helper.lastupd_dttm

    def get_groups_by_user_id(self, user_id):
        result = None
        try:
            result = MembershipTbl.objects.filter(user_id=user_id)
        except Exception as ex:
            raise ex
        return result


class MemberShipHelper(object):

    def __init__(self, group_id, group_name, user_id, user_name, lastipd_dttm):
        self.group_id = group_id
        self.group_name = group_name
        self.user_id = user_id
        self.user_name = user_name
        self.lastupd_dttm = lastipd_dttm
