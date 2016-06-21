# -*- coding: utf-8 -*-
import types
import mandrill
from config import *
from jinja2 import Environment, PackageLoader
__author__ = 'ravikant'


class JinjaTemplate():
    def get_new_env(self):
        environment = Environment(loader=PackageLoader('templates', 'emailtemplates'), autoescape=True)
        return environment

    def get_templates(self, environment):
        template = environment.get_template('email_template.html')
        return template


def _encode_str(s):
    if type(s)==types.UnicodeType:
        return s.encode('utf8')
    return s


def get_mandrill_client():
    mandrill_client = mandrill.Mandrill(MANDRILL_API_KEY)
    return mandrill_client


class MandrillEmail():
    def __init__(self, mandrill_client):
        self.mandrill_client = mandrill_client

    def send_email(self, subject, from_address,from_name,to_address, email_body, plain_text=None, mock=False):
        try:
            message = {
                'from_email': from_address,
                'from_name': from_name,
                'html': _encode_str(email_body),
                'subject': _encode_str(subject),
                'to': [{'email': to_address, 'type': 'to'}]
            }
            result = self.mandrill_client.messages.send(message=message, async=False)
            return result
        except:
            raise