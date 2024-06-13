import os


class Cell:
    def __init__(self, num):
        self.num = num
        self.symbol = '	'

    def __str__(self):
        return self.symbol


class Board:
    def __init__(self, n):
        self.cells = []
        self.n = n
        self.win = 5
        for i in range(n * n):
            self.cells.append(Cell(i + 1))

    def display(self):
        n = self.n
        print("	", end='')
        for i in range(n):
            print(chr(ord('A') + i), end=' ')
        print("")
        for i in range(n):

            print('	', end='')
            print('-')
            print("{:2}".format(i + 1), end="	")
            out = '|	'
            for j in range(n):
                c = self.cells[i * n + j]
                out += str(c) + '	|	'
            print(out)

        print('	', end='')
        print('-')

    def update(self, cell_num, symbol):
        if self.cells[cell_num - 1].symbol == '	':
            self.cells[cell_num - 1].symbol = symbol
            return True
        return False

    def is_game_over(self):
        n = self.n
        for i in range(n):
            for j in range(n - self.win):
                pos = i * n + j
                if self.cells[pos].symbol != '	':
                    wk = 0
                    for k in range(self.win - 1):
                        wk += self.cells[pos + k].symbol == self.cells[pos + k + 1].symbol
                    if wk == self.win - 1:
                        return True
            for j in range(n):
                for i in range(n - self.win):
                    pos = i * n + j
                    if self.cells[pos].symbol != '	':
                        wk = 0
                        for k in range(self.win - 1):
                            wk += self.cells[pos + k * n].symbol == self.cells[pos + (k + 1) * n].symbol
                        if wk == self.win - 1:
                            return True
            for i in range(n - self.win):
                for j in range(n - self.win):
                    pos = i * n + j
                    if self.cells[pos].symbol != '	':
                        wk = 0
                        for k in range(self.win - 1):
                            wk += self.cells[pos + k + k * n].symbol == self.cells[pos + (k + 1) * n + k + 1].symbol
                            if wk == self.win - 1:
                                return True
            for i in range(n - self.win):
                for j in range(self.win - 1, n):
                    pos = i * n + j
                    if self.cells[pos].symbol != '	':
                        wk = 0
                        for k in range(self.win - 1):
                            wk += self.cells[pos - k + k * n].symbol == self.cells[pos + (k + 1) * n - k - 1].symbol
                        if wk == self.win - 1:
                            return True
            for cell in self.cells:
                if cell.symbol == '	':
                    return False
            return True


class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol
        self.score = 0

    def get_move(self):
        cell_num = input(self.name + ', Напиши букву потом цифру ячейки: ')
        return cell_num.upper()


class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.num = int(input('Введите на сколькщ ячеек играть : '))
        self.board = Board(self.num)
        self.current_player = player1

    def play_turn(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(self.current_player.name + ' Ваш ход :\n')
        self.board.display()
        t = self.current_player.get_move()
        t = t.upper()
        nn = int(t[1:]) - 1
        cell_num = 1 + (ord(t[0]) - ord('A')) + nn * self.num
        while not self.board.update(cell_num, self.current_player.symbol):
            print('Это место уже занято. Попробуй ещё раз')
            t = self.current_player.get_move()
            t = t.upper()
            nn = int(t[1:]) - 1
            cell_num = 1 + (ord(t[0]) - ord('A')) + nn * self.num
        if self.board.is_game_over():
            os.system('cls' if os.name == 'nt' else 'clear')
            print(self.current_player.name + ' Победа !\n')
            self.board.display()
            self.current_player.score += 1
            return True
        if self.current_player == self.player1:
            self.current_player = self.player2
        else:
            self.current_player = self.player1
            return False

    def play_game(self):
        os.system('cls' if os.name == 'nt' else 'clear')

        print('Новая ира началась!')
        self.board = Board(self.num)
        self.current_player = self.player1
        while not self.board.is_game_over():
            if self.play_turn():
                break
        print('Результаты:')
        print(self.player1.name + ': ' + str(self.player1.score))
        print(self.player2.name + ': ' + str(self.player2.score))


name1 = input('Введите имя игрока 1 (X): ')
name2 = input('Введите имя игрока 2 (O): ')
player1 = Player(name1, 'x')
player2 = Player(name2, 'o')
game = Game(player1, player2)
while True:
    game.play_game()
    again = input('Желаете сыграть ещё раз? (Y/N):	')
    if again.lower() != 'y':
        break
print('Спасибо, за игру! ')
