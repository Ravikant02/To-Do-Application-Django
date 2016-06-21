__author__ = 'ravikant'
import json


class LoginJsonHelper(object):

    def __init__(self, user_name, password):
        self.user_name = user_name
        self.password = password


class LoginJsonConverter(object):

    def __init__(self):
        pass

    def load_json(self, json_string):
        result = json.loads(json_string)
        user_name = None
        password = None
        if 'user_name' in result:
            user_name = result['user_name']
        if 'password' in result:
            password = result['password']

        return LoginJsonHelper(user_name, password)
