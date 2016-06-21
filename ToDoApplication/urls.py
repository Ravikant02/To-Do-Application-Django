"""ToDoApplication URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from ToDoSource.views.panelviews import *
from ToDoSource.views.taskviews import *
from ToDoSource.views.userviews import *
from ToDoSource.views.boardviews import *

urlpatterns = [
    url(r'^api/admin/', admin.site.urls),
    url(r'^api/tmp/(?P<user_id>.*)$', TmpJS.as_view(), name='dashboard'),
    url(r'^api/dashboard/(?P<user_id>.*)$', DashBoard.as_view(), name='dashboard'),
    url(r'^api/signup/', UserRegister.as_view(), name='user_register'),
    url(r'^api/register/', Register.as_view(), name='register'),
    url(r'^api/login/', Login.as_view(), name='user_login'),
    url(r'^api/upload/avatar/', UploadPic.as_view(), name='avatar_upload'),
    url(r'^api/reminder/email/', EmailReminder.as_view(), name='email_reminder'),
    url(r'^api/board/(?P<user_id>.*)/(?P<board_id>.*)$', GetBoardDetails.as_view(), name='board'),
    url(r'^api/share/group/', ShareGroup.as_view(), name='share_group'),
    url(r'^api/join/group/(?P<user_id>.*)/(?P<group_code>.*)$', JoinGroup.as_view(), name='join_group'),
    url(r'^api/addboard/(?P<user_id>.*)/(?P<board_name>.*)/(?P<group_id>.*)$',
        AddBoard.as_view(), name='add_board'),
    url(r'^api/deleteboard/(?P<user_id>.*)/(?P<board_id>.*)$', DeleteBoard.as_view(), name='delete_board'),
    url(r'^api/addgroup/(?P<user_id>.*)/(?P<group_name>.*)$', AddGroup.as_view(), name='add_group'),
    url(r'^api/deletetask/(?P<user_id>.*)/(?P<board_id>.*)/(?P<panel_id>.*)/(?P<task_id>.*)$',
        DeleteTask.as_view(), name='delete_task'),
    url(r'^api/movetask/(?P<user_id>.*)/(?P<board_id>.*)/(?P<panel_id>.*)/(?P<task_id>.*)$',
        MoveTask.as_view(), name='delete_task'),
    url(r'^api/addpanel/(?P<user_id>.*)$', AddPanel.as_view(), name='add_panel'),
    url(r'^api/addtask/(?P<user_id>.*)$', AddTask.as_view(), name='add_task'),
    url(r'^tmp/', Exp.as_view(), name='exp'),

]
