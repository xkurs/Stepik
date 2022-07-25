class ReversiBoard(object):
    """        a   b   c   d   e   f   g   h
        8
        ...
        1
    """
    board = [[-1, -1, -1, -1, -1, -1, -1, -1],
             [-1, -1, -1, -1, -1, -1, -1, -1],
             [-1, -1, -1, -1, -1, -1, -1, -1],
             [-1, -1, -1,  0,  1, -1, -1, -1],
             [-1, -1, -1,  1,  0, -1, -1, -1],
             [-1, -1, -1, -1, -1, -1, -1, -1],
             [-1, -1, -1, -1, -1, -1, -1, -1],
             [-1, -1, -1, -1, -1, -1, -1, -1]]

    @classmethod
    def interpret_transcript(cls, move_str):
        move_str = move_str.lower()
        move_str = move_str.replace("a", "1")
        move_str = move_str.replace("b", "2")
        move_str = move_str.replace("c", "3")
        move_str = move_str.replace("d", "4")
        move_str = move_str.replace("e", "5")
        move_str = move_str.replace("f", "6")
        move_str = move_str.replace("g", "7")
        move_str = move_str.replace("h", "8")
        move_str = move_str.replace(" ", "0")
        move_colorxy = [(int(i // 2 % 2), int(move_str[i]), int(move_str[i+1])) for i in range(0, len(move_str), 2)]
        print(move_colorxy)
        return 'I', 'W', 'I', 10, 3


ReversiBoard.interpret_transcript('D3c5F6F5e6e3d6f7g6')      # output: ('I', 'W', 'I', 10, 3)
ReversiBoard.interpret_transcript('d3c5f6  f5e6e3d6f7g6')    # output: ('E', None, None, None, None)
