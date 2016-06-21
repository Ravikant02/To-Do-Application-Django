__author__ = 'ravikant'
from .models import PanelTbl
import datetime


class PanelORM(object):

    def get_panel_by_board_id(self, board_id):
        result = PanelTbl.objects.filter(board_id=board_id)
        if len(result) > 0:
            return result
        else:
            return None

    def add_panel(self, board_id, panel_name):
        panel_tbl = PanelTbl()
        panel_tbl.board_id = board_id
        panel_tbl.panel_name = panel_name
        panel_tbl.create_dttm = datetime.datetime.now()
        panel_tbl.lastupd_dttm = datetime.datetime.now()
        try:
            panel_tbl.save()
        except:
            raise