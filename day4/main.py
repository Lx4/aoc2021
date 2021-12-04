
# print an X instead of the number if read


class Board:
    size = 5

    def __init__(self):
        self.rows = []
        self.winning = False

    def add_row(self, row):
        self.rows.append(row)

    def cross_number(self, num):
        for row in self.rows:
            for i in range(Board.size):
                if row[i] == num:
                    row[i] = 'X'

    def is_winning(self):
        # check rows
        for row in self.rows:
            win = True
            for num in row:
                if num is not 'X':
                    win = False
            if win == True:
                self.winning = True
                return True
        # check columns
        for i in range(Board.size):
            win = True
            for j in range(Board.size):
                if self.rows[j][i] is not 'X':
                    win = False
                    continue
            if win == True:
                self.winning = True
                return True
        return False

    def sum(self):
        total = 0
        for row in self.rows:
            for i in range(Board.size):
                if row[i] is not 'X':
                    total += row[i]
        return total

    def print_board(self):
        for row in self.rows:
            print(row)


bingo = []
with open("input") as infile:
    numbers = [int(n) for n in infile.readline().rstrip('\n').split(',')]
    input = infile.readlines()
    for line in input:
        # new line, create a Board
        if line == '\n':
            board = Board()
            bingo.append(board)
        else:
            row = [int(n) for n in line.rstrip('\n').split()]
            board.add_row(row)

    # data = [list(line.rstrip("\n")) for line in infile.readlines()]


# def part1():
#     for num in numbers:
#         # print("handling", num)
#         for board in bingo:
#             # print("new board")
#             board.cross_number(num)
#             # board.print_board()
#             if board.is_winning() == True:
#                 print("a board has win after num", num)
#                 print("answer part 1 is", board.sum() * num)
#                 return


def part2():
    total_boards = len(bingo)
    print("Number of boards", total_boards)
    for num in numbers:
        # print("handling", num)
        for i in range(len(bingo)):
            # print("new board")
            board = bingo[i]
            board.cross_number(num)
            # board.print_board()
            if board.is_winning() == True:
                print("a board has win after num", num)
                print("answer part 2 is", board.sum() * num)
            count = 0
            for b in bingo:
                if b.winning:
                    count += 1
                if (count == total_boards):
                    print("winning boards:", count)
                    return
            


# part1()
part2()
