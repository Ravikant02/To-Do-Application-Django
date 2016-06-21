from models import BoardTbl, GroupTbl
import datetime


class BoardORM(object):

    def get_all_boards(self, group_id):
        result = BoardTbl.objects.filter(group_id=group_id)
        if len(result) > 0:
            return result
        else:
            return None

    def update_board(self, board, board_helper):
        pass

    def get_board_by_board_id(self, board_id):
        result = BoardTbl.objects.filter(board_id=board_id)
        if len(result) > 0:
            return result[0]
        else:
            return None

    def add_board(self, board_name, group_id):
        board = BoardTbl()
        board.board_name = board_name
        board.group_id = group_id
        board.created_dttm = datetime.datetime.now()
        try:
            board.save()
        except Exception as ex:
            raise ex

    def delete_board(self, board_id):
        try:
            BoardTbl.objects.filter(board_id=board_id).delete()
        except Exception as ex:
            raise ex