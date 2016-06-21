from ToDoSource.models import *
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfileTbl
        fields = ('user_id', 'emailid', 'avatar_url', 'contact', 'access_token')


class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = BoardTbl
        fields = ('board_id', 'board_name')


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupTbl
        fields = ('group_id', 'group_name')


class MemberShipSerializer(serializers.ModelSerializer):
    class Meta:
        model = MembershipTbl
        fields = ('group_id')


class GroupAndBoardsSerializer(serializers.ModelSerializer):
    boards = BoardSerializer(many=True)

    class Meta:
        model = GroupTbl
        fields = ('group_id', 'group_name', 'boards')


class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = TasksTbl
        fields = ('task_id', 'task_name')
