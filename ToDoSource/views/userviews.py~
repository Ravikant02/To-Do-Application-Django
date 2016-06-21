from django.shortcuts import render, HttpResponse
import json
from django.views.generic import View
from serializers import UserSerializer, GroupSerializer, MemberShipSerializer, BoardSerializer, \
    GroupAndBoardsSerializer
from ..models import UserProfileTbl, GroupTbl, MembershipTbl, BoardTbl
from ..userservices import UserORM, UserProfileHelper
from ..groupservices import GroupORM, GroupHelper
from ..boardservices import BoardORM
from ..membershipservices import MemberShipORM, MemberShipHelper
from ..services import get_md5_string, get_new_access_token, get_new_group_code, handle_uploaded_file
from ..jsonservice import LoginJsonConverter
import datetime
import uuid
from django.conf import settings
from django.utils import timezone
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from rest_framework.views import APIView, status


# Create your views here.


class Login(APIView):
    def post(self, request):
        if request.method == 'POST':
            login_json_converter = LoginJsonConverter()
            login_json = request.body
            login_json_helper = login_json_converter.load_json(login_json)
            user_name = login_json_helper.user_name  # request.POST.get('user_name')
            password = login_json_helper.password  # request.POST.get('password')
            response = dict()
            user_orm = UserORM()
            new_password = get_md5_string(password)
            user_data = user_orm.get_user_login(user_name, new_password)

            if user_data:
                # user_data.user_id = get_md5_string(str(user_data.user_id))
                user_serializer = UserSerializer(user_data)
                response.update({'status': 'success'})
                response.update({'data': user_serializer.data})
                response.update({'message': 'data retrieve successfully.!'})
                response.update({'response_code': status.HTTP_200_OK})
            else:
                response.update({'status': 'error'})
                response.update({'data': None})
                response.update({'message': 'could not login'})
                response.update({'response_code': status.HTTP_401_UNAUTHORIZED})
            return HttpResponse(json.dumps(response), content_type="application/json")


class UserRegister(APIView):
    def post(self, request):
        if request.method == 'POST':
            user_name = request.POST.get('user_name')
            password = request.POST.get('password')
            email_id = request.POST.get('emailid')
            # contact = request.POST.get('contact')
            # profile_pic = request.data['profile_pic']

            user_orm = UserORM()
            group_orm = GroupORM()
            member_ship_orm = MemberShipORM()
            response = dict()
            user_profile = UserProfileTbl()
            group_tbl = GroupTbl()
            member_ship = MembershipTbl()
            new_password = get_md5_string(password)
            access_token = get_new_access_token()
            if user_orm.get_user_name_if_exists(user_name):
                response.update({'response_code': status.HTTP_406_NOT_ACCEPTABLE})
                response.update({'message': 'user name already exists'})
                response.update({'status': 'error'})
                response.update({'data': None})
                return HttpResponse(json.dumps(response), content_type="application/json")
            user_profile_helper = UserProfileHelper(user_name, new_password, email_id, access_token,
                                                    datetime.datetime.now().now(),
                                                    datetime.datetime.now().now())
            user_orm.update_user_data(user_profile, user_profile_helper)

            try:
                group_code = get_new_group_code()
                user_profile.save()
                group_helper = GroupHelper('MyBoards', user_profile.user_id, group_code, datetime.datetime.now(),
                                           datetime.datetime.now())
                group_orm.update_group(group_tbl, group_helper)
                group_tbl.save()

                member_ship_helper = MemberShipHelper(group_tbl.group_id, group_tbl.group_name, user_profile.user_id,
                                                      user_profile.user_name, datetime.datetime.now())
                member_ship_orm.update_member(member_ship, member_ship_helper)
                member_ship.save()
            except Exception as ex:
                response.update({'response_code': status.HTTP_417_EXPECTATION_FAILED})
                response.update({'message': 'could not save details'})
                response.update({'status': 'error'})
                response.update({'data': None})
                return HttpResponse(json.dumps(response), content_type="application/json")
            finally:
                response.update({'response_code': status.HTTP_200_OK})
                response.update({'message': 'data saved successfully!'})
                response.update({'status': 'success'})
                response.update({'data': {'userName': user_profile.user_name,
                                          'emailID': user_profile.emailid,
                                          'accessToken': user_profile.access_token,
                                          'avatar_url': "",
                                          'contact': user_profile.contact}})
                return HttpResponse(json.dumps(response), content_type="application/json")


class DashBoard(APIView):
    def get(self, request, user_id):
        user_orm = UserORM()
        group_orm = GroupORM()
        board_orm = BoardORM()
        member_ship_orm = MemberShipORM()
        response = dict()
        groups_list = list()
        access_token = request.META.get('HTTP_ACCESSTOKEN')
        if user_orm.get_user_access_token(user_id, access_token):
            groups = member_ship_orm.get_groups_by_user_id(user_id)
            # groups = group_orm.get_groups_of_user(user_id)
            if groups:
                for group in groups:
                    boards = BoardSerializer(board_orm.get_all_boards(group.group_id), many=True)
                    grp = group_orm.get_group_details(group.group_id)
                    groups_list.append({'group_id': group.group_id, 'group_name': grp.group_name,
                                        'boards': boards.data, 'group_code': grp.group_code})
                response.update({'status': 'success'})
                response.update({'message': 'data retrieve successfully!'})
                response.update({'response_code': status.HTTP_200_OK})
                response.update({'data': {'groups': groups_list}})
        else:
            response.update({'status': 'error'})
            response.update({'message': 'invalid headers!'})
            response.update({'response_code': status.HTTP_401_UNAUTHORIZED})
            response.update({'data': None})
        # print json.dumps(response)
        return HttpResponse(json.dumps(response), content_type="application/json")


class Register(View):
    template_name = 'register.html'

    def get(self, request):
        body = render(request, self.template_name)
        return HttpResponse(body)


class TmpJS(APIView):
    def get(self, request, user_id):
        user_orm = UserORM()
        group_orm = GroupORM()
        board_orm = BoardORM()
        response = dict()
        groups_list = list()
        access_token = request.META.get('HTTP_ACCESSTOKEN')

        groups = group_orm.get_groups_of_user(user_id)
        if groups:
            for group in groups:
                boards = BoardSerializer(board_orm.get_all_boards(group.group_id), many=True)
                groups_list.append({'group_id': group.group_id, 'group_name': group.group_name,
                                    'boards': boards.data})
            response.update({'status': 'success'})
            response.update({'message': 'data retrieve successfully!'})
            response.update({'response_code': status.HTTP_200_OK})
            response.update({'data': {'groups': groups_list}})
        else:
            response.update({'status': 'error'})
            response.update({'message': 'invalid headers!'})
            response.update({'response_code': status.HTTP_401_UNAUTHORIZED})
            response.update({'data': None})
        return HttpResponse(json.dumps(response), content_type="application/json")


class Exp(APIView):
    template_name = "templates/tmp.html"

    def get(self, request):
        body = render(request, self.template_name)
        return HttpResponse(body)


class UploadPic(APIView):
    def post(self, request):
        if request.method == 'POST':
            response = dict()
            user_orm = UserORM()
            access_token = request.META.get('HTTP_ACCESSTOKEN')
            user_id = request.POST.get('user_id')
            print (user_id)
            if user_orm.get_user_access_token(user_id, access_token):
                image_name = settings.MEDIA_ROOT + "profile/profile_" + user_id + ".jpg"
                user = user_orm.get_user_with_user_id(user_id)
                try:
                    handle_uploaded_file(request.FILES['file'], image_name)
                    image_name = "/" + image_name
                    user.avatar_url = image_name
                    user.save()
                    response.update({'message': 'profile picture uploaded successfully!'})
                    response.update({'avatar_url': image_name})
                    response.update({'response_code': status.HTTP_200_OK})
                    response.update({'status': 'success'})
                except Exception as ex:
                    print (ex)
                    response.update({'message': 'could not upload image'})
                    response.update({'response_code': status.HTTP_406_NOT_ACCEPTABLE})
                    response.update({'status': 'error'})
            else:
                response.update({'status': 'error'})
                response.update({'message': 'invalid headers!'})
                response.update({'response_code': status.HTTP_401_UNAUTHORIZED})
                response.update({'data': None})
            return HttpResponse(json.dumps(response), content_type="application/json")
