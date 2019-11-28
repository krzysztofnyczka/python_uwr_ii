import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


class GameOfLife:
    def __init__(self, size):
        self.size = size
        self.board = self.make_board()

    def make_board(self):
        board = np.random.randint(0, 2, (self.size, self.size))
        return board

    def neighbours(self, i, j):
        return self.board[i-1][j-1] + self.board[i-1][j] + self.board[i-1][j+1] + \
               self.board[i][j-1] + self.board[i][j+1] + self.board[i+1][j-1] +\
               self.board[i+1][j] + self.board[i+1][j+1]

    def animate(self, _):
        temp = self.board * 0
        for i in range(1, self.size-1):
            for j in range(1, self.size-1):
                neighbours = self.neighbours(i, j)
                if self.board[i][j] == 1 and (neighbours == 2 or neighbours == 3):
                    temp[i][j] = 1
                if self.board[i][j] == 0 and neighbours == 3:
                    temp[i][j] = 1
                else:
                    temp[i][j] = 0

        self.board = temp
        mat.set_data(self.board)
        return [mat]
        # plt.scatter(cells.T[0], cells.T[1])


if __name__ == "__main__":
    gol = GameOfLife(100)
    mat = plt.matshow(gol.board)
    ani = FuncAnimation(plt.gcf(), gol.animate, interval=1000)
    plt.show()