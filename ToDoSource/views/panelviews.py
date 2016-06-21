from rest_framework.views import APIView, status
from django.shortcuts import HttpResponse
import json
from ..models import PanelTbl
from ..userservices import UserORM
from ..panelservices import PanelORM


class AddPanel(APIView):

    def post(self, request, user_id):
        if request.method == 'POST':
            user_orm = UserORM()
            panel_orm = PanelORM()
            panel_name = request.POST.get('panel_name')
            board_id = request.POST.get('board_id')
            access_token = request.META.get('HTTP_ACCESSTOKEN')
            response = dict()
            if user_orm.get_user_access_token(user_id, access_token):
                try:
                    panel_orm.add_panel(board_id, panel_name)
                    response.update({'response_code': status.HTTP_200_OK})
                    response.update({'message': 'data saved successfully.!'})
                    response.update({'status': 'success'})
                except:
                    response.update({'response_code': status.HTTP_406_NOT_ACCEPTABLE})
                    response.update({'message': 'could not save data'})
                    response.update({'status': 'error'})
            else:
                response.update({'status': 'error'})
                response.update({'message': 'invalid headers!'})
                response.update({'response_code': status.HTTP_401_UNAUTHORIZED})
            return HttpResponse(json.dumps(response), content_type="application/json")