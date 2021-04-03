from django.http import HttpResponse, HttpResponseBadRequest

from .game_utils import can_game_proceed, create_board, play


def tic_tac_toe_view(request):
    board_str = request.GET.get("board")
    if can_game_proceed(board_str):
        board = create_board(board_str)
        return HttpResponse(play(board))
    else:
        return HttpResponseBadRequest("Invalid board or board state")
