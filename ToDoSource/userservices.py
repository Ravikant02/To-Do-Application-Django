from models import *


class UserORM(object):

    def get_user_with_user_id(self, user_id):
        result = UserProfileTbl.objects.get(user_id=user_id)
        return result

    def get_user_login(self, user_name, password):
        result = UserProfileTbl.objects.filter(user_name=user_name, password=password)
        if len(result) > 0:
            return result[0]
        else:
            return None

    def is_access_token_exists(self, access_token):
        result = UserProfileTbl.objects.filter(access_token=access_token)
        if result:
            return True
        return False

    def update_user_data(self, user_profile, user_profile_helper):
        user_profile.user_name = user_profile_helper.user_name
        user_profile.emailid = user_profile_helper.email_id
        user_profile.password = user_profile_helper.password
        #user_profile.contact = user_profile_helper.contact
        user_profile.access_token = user_profile_helper.access_token
        user_profile.lastupd_dttm = user_profile_helper.lastupd_dttm
        user_profile.created_dttm = user_profile_helper.created_dttm

    def get_user_name_if_exists(self, user_name):
        resutl = UserProfileTbl.objects.filter(user_name=user_name)
        if resutl:
            return True
        else:
            return False

    def get_user_access_token(self, user_id, access_token):
        result = UserProfileTbl.objects.filter(user_id=user_id, access_token=access_token)
        if len(result) > 0:
            return True
        else:
            return None

    def update_user_avatar_url(self, user_profile, avatar_url):
        user_profile.avatar_url = avatar_url


class UserProfileHelper(object):

    def __init__(self, user_name, password, email_id, access_token, lastupd_dttm, created_dttm):
        self.user_name = user_name
        self.password = password
        self.email_id = email_id
        self.access_token = access_token
        self.lastupd_dttm = lastupd_dttm
        self.created_dttm = created_dttm


class MemberShipORM(object):
    def get_groups_by_user_id(self, user_id):
        result = None
        try:
            result = MembershipTbl.objects.filter(user_id=user_id)
        except Exception as ex:
            raise ex
        return result
