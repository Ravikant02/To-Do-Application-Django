from rest_framework.views import APIView, status
from django.shortcuts import HttpResponse
import json
from ..userservices import UserORM
from ..taksservices import TaskORM


class AddTask(APIView):

    def post(self, request, user_id):
        if request.method == 'POST':
            user_orm = UserORM()
            task_orm = TaskORM()
            task_name = request.POST.get('task_name')
            panel_id = request.POST.get('panel_id')
            board_id = request.POST.get('board_id')
            access_token = request.META.get('HTTP_ACCESSTOKEN')
            response = dict()
            if user_orm.get_user_access_token(user_id, access_token):
                try:
                    task_orm.add_task(task_name, panel_id, board_id)
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


class DeleteTask(APIView):
    def get(self, request, user_id, board_id, panel_id, task_id):
        if request.method == 'GET':
            user_orm = UserORM()
            task_orm = TaskORM()

            access_token = request.META.get('HTTP_ACCESSTOKEN')
            #access_token = 'APP-5CNV9CVNND'
            response = dict()
            if user_orm.get_user_access_token(user_id, access_token):
                try:
                    if task_orm.is_task_id_exists(board_id, panel_id, task_id):
                        task_orm.delete_task(board_id, panel_id, task_id)
                        response.update({'response_code': status.HTTP_200_OK})
                        response.update({'message': 'task deleted successfully.!'})
                        response.update({'status': 'success'})
                    else:
                        response.update({'response_code': status.HTTP_406_NOT_ACCEPTABLE})
                        response.update({'message': 'could not delete task'})
                        response.update({'status': 'error'})
                except:
                    response.update({'response_code': status.HTTP_406_NOT_ACCEPTABLE})
                    response.update({'message': 'could not delete task'})
                    response.update({'status': 'error'})
            else:
                response.update({'status': 'error'})
                response.update({'message': 'invalid headers!'})
                response.update({'response_code': status.HTTP_401_UNAUTHORIZED})
            return HttpResponse(json.dumps(response), content_type="application/json")


class MoveTask(APIView):
    def get(self, request, user_id, board_id, panel_id, task_id):
        if request.method == 'GET':
            user_orm = UserORM()
            task_orm = TaskORM()

            access_token = request.META.get('HTTP_ACCESSTOKEN')
            response = dict()
            if user_orm.get_user_access_token(user_id, access_token):
                try:
                    task_orm.move_task(board_id, panel_id, task_id)
                    response.update({'response_code': status.HTTP_200_OK})
                    response.update({'message': 'task updated successfully.!'})
                    response.update({'status': 'success'})
                except Exception as ex:
                    response.update({'response_code': status.HTTP_406_NOT_ACCEPTABLE})
                    response.update({'message': 'could not update task'})
                    response.update({'status': ex})
            else:
                response.update({'status': 'error'})
                response.update({'message': 'invalid headers!'})
                response.update({'response_code': status.HTTP_401_UNAUTHORIZED})
            return HttpResponse(json.dumps(response), content_type="application/json")