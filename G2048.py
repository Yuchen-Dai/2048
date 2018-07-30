import random, operator, copy


class GameOverError(Exception):
    pass



class Board:

    def __init__(self, row, col):
        self._board = []
        self._row = row
        self._col = col
        for r in range(row):
            self._board.append([])
            for c in range(col):
                self._board[r].append(0)

    def get_board(self):
        return self._board

    def print_board(self):
        bline = ''
        bline = '-' * (self._col * 5 + 2)
            
        mline = '|' + ' ' * self._col * 5 + '|'

        
        print(bline)
        for row in self._board:
            print(mline)
            line = '|'
            for col in row:
                if not col:
                    col = ' '
                line += f'{col: ^5}'
            print(line + '|')
        print(mline)
        print(bline)

    def create_random_block(self):
        air = self._get_air()
        length = len(air)
        block = air[random.randint(0, length - 1)]
        self._board[block[0]][block[1]] = 2


    def _get_air(self):
        result = []
        for row in range(self._row):
            for col in range(self._col):
                if not self._board[row][col]:
                    result.append((row, col))
        return result

    def right(self):
        old_board = copy.deepcopy(self._board)
        for row in range(self._row):
            for col in range(self._col -1, -1, -1):
                for compare in range(col -1, -1, -1):
                    now = self._board[row][col]
                    comp = self._board[row][compare]
                    if now and comp and now == comp:
                        self._board[row][col] += comp
                        self._board[row][compare] = 0
                        break
        for row in range(self._row):
            self._board[row].sort(key = self._sort)
        return move(old_board, self._board)

    
    def left(self):
        old_board = copy.deepcopy(self._board)
        for row in range(self._row):
            for col in range(self._col):
                for compare in range(col + 1, self._col):
                    now = self._board[row][col]
                    comp = self._board[row][compare]
                    if now and comp and now == comp:
                        self._board[row][col] += comp
                        self._board[row][compare] = 0
                        break
        for row in range(self._row):
            self._board[row].sort(key = self._sort, reverse = True)
        return move(old_board, self._board)

    def _sort(self, a):
        if a != 0:
            return 1
        return 0


    def down(self):
        old_board = copy.deepcopy(self._board)
        for col in range(self._col):
            for row in range(self._row - 1, -1, -1):
                for compare in range(row - 1, -1, -1):
                    now = self._board[row][col]
                    comp = self._board[compare][col]
                    if now and comp and now == comp:
                        self._board[row][col] += comp
                        self._board[compare][col] = 0
                        break
        for col in range(self._col):
            result = []
            for row in range(self._row):
                result.append(self._board[row][col])
            result.sort(key = self._sort)
            for row in range(self._row):
                self._board[row][col] = result[row]
        return move(old_board, self._board)

    def up(self):
        old_board = copy.deepcopy(self._board)
        for col in range(self._col):
            for row in range(self._row):
                for compare in range(row + 1, self._row):
                    now = self._board[row][col]
                    comp = self._board[compare][col]
                    if now and comp and now == comp:
                        self._board[row][col] += comp
                        self._board[compare][col] = 0
                        break
        for col in range(self._col):
            result = []
            for row in range(self._row):
                result.append(self._board[row][col])
            result.sort(key = self._sort, reverse = True)
            for row in range(self._row):
                self._board[row][col] = result[row]
        return move(old_board, self._board)

    def check_gameover(self):
        if len(self._get_air()):
            return
        for row in range(self._row):
            for col in range(self._col - 1):
                if self._board[row][col] == self._board[row][col +1]:
                    return
        for col in range(self._col):
            for row in range(self._row - 1):
                if self._board[row][col] == self._board[row + 1][col]:
                    return
        raise GameOverError

def move(list1, list2)-> bool:
    row = 0
    for r in list1:
        col = 0
        for c in r:
            if c != list2[row][col]:
                return True
            col += 1
        row += 1
    return False

    
if __name__ == '__main__':
    a = Board(4,4)
    a.create_random_block()
    while True:
        a.print_board()
        cmd = input('[u] or [d] or [l] or [r] or [q] or [r]?\n')
        if cmd == 'u':
            a.up()
            a.create_random_block()
        elif cmd == 'd':
            a.down()
            a.create_random_block()
        elif cmd == 'l':
            a.left()
            a.create_random_block()
        elif cmd == 'r':
            a.right()
            a.create_random_block()
        elif cmd == 'q':
            break
        elif cmd == 'r':
            a = Board(4,4)
            a.create_random_block()
        
