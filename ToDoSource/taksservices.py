__author__ = 'ravikant'
from .models import TasksTbl
import datetime


class TaskORM(object):

    def get_tasks_by_panel_id(self, panel_id):
        result = TasksTbl.objects.filter(panel_id=panel_id)
        if len(result) > 0:
            return result
        else:
            return None

    def add_task(self, task_name, panel_id, board_id):
        tasks_tbl = TasksTbl()
        tasks_tbl.board_id = board_id
        tasks_tbl.panel_id = panel_id
        tasks_tbl.task_name =task_name
        tasks_tbl.lastupd_dttm = datetime.datetime.now()
        try:
            tasks_tbl.save()
        except:
            raise

    def is_task_id_exists(self,board_id, panel_id, task_id):
        result = TasksTbl.objects.filter(board_id=board_id, panel_id=panel_id, task_id=task_id)
        if len(result) > 0:
            return True
        else:
            return False

    def delete_task(self, board_id, panel_id, task_id):
        try:
            TasksTbl.objects.filter(board_id=board_id, panel_id=panel_id, task_id=task_id).delete()
        except:
            raise

    def move_task(self, board_id, panel_id, task_id):
        try:
            task_table = TasksTbl.objects.get(board_id=board_id, task_id=task_id)
            task_table.panel_id = panel_id
            task_table.lastupd_dttm = datetime.datetime.now()
            task_table.save()
        except:
            raise


