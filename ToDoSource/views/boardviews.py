from django.shortcuts import render, HttpResponse
import json
from django.views.generic import View
from ..services import get_md5_string
from .serializers import *
from ..userservices import UserORM
from ..boardservices import BoardORM
from ..panelservices import PanelORM
from ..taksservices import TaskORM
from ..membershipservices import MemberShipORM, MemberShipHelper
from ..groupservices import GroupHelper, GroupORM
from ..services import get_new_group_code
from ..models import MembershipTbl
from ..email_services import get_mandrill_client, MandrillEmail, JinjaTemplate
from ..config import *
from rest_framework.views import APIView, status
import datetime


class GetBoardDetails(APIView):

    def get(self, request, user_id, board_id):
        access_token = request.META.get('HTTP_ACCESSTOKEN')
        user_orm = UserORM()
        panel_orm = PanelORM()
        board_orm = BoardORM()
        task_orm = TaskORM()
        response = dict()
        panels_details = list()
        #access_token = 'APP-5CNV9CVNND'
        if user_orm.get_user_access_token(user_id, access_token):
            board_details = board_orm.get_board_by_board_id(board_id)
            if board_details:
                panels = panel_orm.get_panel_by_board_id(board_id)
                #print panels
                if panels:
                    for panel in panels:
                        tasks = task_orm.get_tasks_by_panel_id(panel.panel_id)
                        task_serializer = TaskSerializer(tasks, many=True)
                        panels_details.append({'panel_id': panel.panel_id,
                                               'panel_name': panel.panel_name,
                                               'tasks': task_serializer.data})
                    response.update({'status': 'success'})
                    response.update({'message': 'data retrieve successfully!'})
                    response.update({'response_code': status.HTTP_200_OK})
                    response.update({'data': {'board_id': board_id,
                                              'board_name': board_details.board_name,
                                              'panels': panels_details}})
                else:
                    response.update({'status': 'success'})
                    response.update({'message': 'data retrieve successfully!'})
                    response.update({'response_code': status.HTTP_200_OK})
                    response.update({'data': {'board_id': board_id,
                                              'board_name': board_details.board_name,
                                              'panels': panels_details}})
            else:
                response.update({'status': 'error'})
                response.update({'message': 'could not retrieve data'})
                response.update({'response_code': status.HTTP_401_UNAUTHORIZED})
                response.update({'data': None})
        else:
            response.update({'status': 'error'})
            response.update({'message': 'invalid headers!'})
            response.update({'response_code': status.HTTP_401_UNAUTHORIZED})
            response.update({'data': None})
        return HttpResponse(json.dumps(response), content_type="application/json")


class AddBoard(APIView):
    def get(self, request, user_id, board_name, group_id):
        access_token = request.META.get('HTTP_ACCESSTOKEN')
        response = dict()
        user_orm = UserORM()
        board_orm = BoardORM()
        if user_orm.get_user_access_token(user_id, access_token):
            board_orm.add_board(board_name, group_id)
            response.update({'status': 'success'})
            response.update({'message': 'data saved successfully!'})
            response.update({'response_code': status.HTTP_200_OK})
        else:
            response.update({'status': 'error'})
            response.update({'message': 'invalid headers!'})
            response.update({'response_code': status.HTTP_401_UNAUTHORIZED})
            response.update({'data': None})
        return HttpResponse(json.dumps(response), content_type="application/json")


class DeleteBoard(APIView):
    def get(self, request, user_id, board_id):
        access_token = request.META.get('HTTP_ACCESSTOKEN')
        response = dict()
        user_orm = UserORM()
        board_orm = BoardORM()
        if user_orm.get_user_access_token(user_id, access_token):
            board_orm.delete_board(board_id)
            response.update({'status': 'success'})
            response.update({'message': 'board deleted successfully!'})
            response.update({'response_code': status.HTTP_200_OK})
        else:
            response.update({'status': 'error'})
            response.update({'message': 'invalid headers!'})
            response.update({'response_code': status.HTTP_401_UNAUTHORIZED})
            response.update({'data': None})
        return HttpResponse(json.dumps(response), content_type="application/json")


class AddGroup(APIView):
    def get(self, request, user_id, group_name):
        access_token = request.META.get('HTTP_ACCESSTOKEN')
        response = dict()
        user_orm = UserORM()
        member_ship_orm = MemberShipORM()
        member_ship = MembershipTbl()
        group_orm = GroupORM()
        if user_orm.get_user_access_token(user_id, access_token):
            group_code = get_new_group_code()
            group = group_orm.add_group(user_id, group_name, group_code)
            user = user_orm.get_user_with_user_id(user_id)
            member_ship_helper = MemberShipHelper(group.group_id, group_name, user_id, user.user_name,
                                                  datetime.datetime.now())
            member_ship_orm.update_member(member_ship, member_ship_helper)
            try:
                member_ship.save()
                response.update({'status': 'success'})
                response.update({'message': 'group created successfully!'})
                response.update({'response_code': status.HTTP_200_OK})
            except Exception as ex:
                response.update({'status': 'error'})
                response.update({'message': 'could not save data'})
                response.update({'response_code': status.HTTP_401_UNAUTHORIZED})
        else:
            response.update({'status': 'error'})
            response.update({'message': 'invalid headers!'})
            response.update({'response_code': status.HTTP_401_UNAUTHORIZED})
            response.update({'data': None})
        return HttpResponse(json.dumps(response), content_type="application/json")


class ShareGroup(APIView):
    def post(self, request):
        if request.method == 'POST':
            access_token = request.META.get('HTTP_ACCESSTOKEN')

            user_id = request.POST.get('user_id')
            sender_name = request.POST.get('sender_name')
            receiver_name = request.POST.get('receiver_name')
            group_code = request.POST.get('group_code')
            group_name = request.POST.get('group_name')
            email_id = request.POST.get('email_id')

            print (email_id)
            response = dict()
            user_orm = UserORM()
            if user_orm.get_user_access_token(user_id, access_token):
                jinja_template = JinjaTemplate()
                environment = jinja_template.get_new_env()
                template = jinja_template.get_templates(environment)

                try:
                    mandrill_client = get_mandrill_client()
                    mandrill_email = MandrillEmail(mandrill_client)
                    email_template = template.render(image_url="http://192.168.43.92/media/app_logo.png",
                                                     user_name=receiver_name,
                                                     sender_name=sender_name,
                                                     group_code=group_code,
                                                     group_name=group_name)

                    result = mandrill_email.send_email(EMAIL_SUBJECT, FROM_ADDRESS, FROM_NAME, email_id, email_template)
                    print (result)
                    response.update({'status': 'success'})
                    response.update({'message': 'email sent successfully!'})
                    response.update({'response_code': status.HTTP_200_OK})
                except Exception as ex:
                    response.update({'status': 'error'})
                    response.update({'message': 'could not send email'})
                    response.update({'response_code': status.HTTP_401_UNAUTHORIZED})
                    print (ex)
            else:
                response.update({'status': 'error'})
                response.update({'message': 'invalid headers!'})
                response.update({'response_code': status.HTTP_401_UNAUTHORIZED})
                response.update({'data': None})
            print(response)
            return HttpResponse(json.dumps(response), content_type="application/json")


class JoinGroup(APIView):
    def get(self, request, user_id, group_code):
        if request.method == 'GET':
            access_token = request.META.get('HTTP_ACCESSTOKEN')
            response = dict()
            user_orm = UserORM()
            member_ship_orm = MemberShipORM()
            member_ship = MembershipTbl()
            group_orm = GroupORM()

            if user_orm.get_user_access_token(user_id, access_token):
                group = group_orm.get_group_details_by_group_code(group_code)
                if group:
                    user = user_orm.get_user_with_user_id(user_id)
                    member_ship_helper = MemberShipHelper(group.group_id, group.group_name, user_id, user.user_name,
                                                          datetime.datetime.now())
                    member_ship_orm.update_member(member_ship, member_ship_helper)
                    try:
                        member_ship.save()
                        response.update({'status': 'success'})
                        response.update({'message': 'group created successfully!'})
                        response.update({'response_code': status.HTTP_200_OK})
                    except Exception as ex:
                        response.update({'status': 'error'})
                        response.update({'message': 'could not save data'})
                        response.update({'response_code': status.HTTP_401_UNAUTHORIZED})
                else:
                    response.update({'status': 'error'})
                    response.update({'message': 'invalid group code!'})
                    response.update({'response_code': status.HTTP_401_UNAUTHORIZED})
                    response.update({'data': None})
            else:
                response.update({'status': 'error'})
                response.update({'message': 'invalid headers!'})
                response.update({'response_code': status.HTTP_401_UNAUTHORIZED})
                response.update({'data': None})

            return HttpResponse(json.dumps(response), content_type="application/json")


class EmailReminder(APIView):
    def post(self, request):
        if request.method == 'POST':
            access_token = request.META.get('HTTP_ACCESSTOKEN')

            user_id = request.POST.get('user_id')
            task_name = request.POST.get('task_name')
            board_name = request.POST.get('board_name')
            reminder_datetime = request.POST.get('reminder_datetime')
            print (user_id)
            print (task_name)
            print (board_name)
            print (reminder_datetime)

            response = dict()
            user_orm = UserORM()
            if user_orm.get_user_access_token(user_id, access_token):
                user = user_orm.get_user_with_user_id(user_id)
                jinja_template = JinjaTemplate()
                environment = jinja_template.get_new_env()
                template = jinja_template.get_templates(environment)

                try:
                    '''
                    mandrill_client = get_mandrill_client()
                    mandrill_email = MandrillEmail(mandrill_client)
                    email_template = template.render(image_url="http://192.168.43.92/media/app_logo.png",
                                                     user_name=receiver_name,
                                                     sender_name=sender_name,
                                                     group_code=group_code)

                    result = mandrill_email.send_email(EMAIL_SUBJECT, FROM_ADDRESS, FROM_NAME, email_id, email_template)
                    print (result)
                    '''
                    response.update({'status': 'success'})
                    response.update({'message': 'email sent successfully!'})
                    response.update({'response_code': status.HTTP_200_OK})
                except Exception as ex:
                    response.update({'status': 'error'})
                    response.update({'message': 'could not send email'})
                    response.update({'response_code': status.HTTP_401_UNAUTHORIZED})
            else:
                response.update({'status': 'error'})
                response.update({'message': 'invalid headers!'})
                response.update({'response_code': status.HTTP_401_UNAUTHORIZED})
                response.update({'data': None})
            return HttpResponse(json.dumps(response), content_type="application/json")
