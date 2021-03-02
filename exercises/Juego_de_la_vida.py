import random
import time

class GameOfLife():
    def __init__(self, map, times):
        self.map = map
        self.times = times
        self.n = len(map)

    def get_quantity_neighbors(self, row, col):
        neighbors = 0
        if row-1 >= 0 and  col-1 >= 0 and self.map[row-1][col-1]: neighbors += 1
        if row-1 >= 0 and self.map[row-1][col]: neighbors += 1
        if row-1 >= 0 and  col+1 < self.n and self.map[row-1][col+1]: neighbors += 1
        if col-1 >= 0 and self.map[row][col-1]: neighbors += 1
        if col+1 < self.n and self.map[row][col+1]: neighbors += 1
        if row+1 < self.n and col-1 >= 0 and self.map[row+1][col-1]: neighbors += 1
        if row+1 < self.n and self.map[row+1][col]: neighbors += 1
        if row+1 < self.n and col+1 < self.n and self.map[row+1][col+1]: neighbors += 1
        return neighbors

    def run(self):
        for cicle in range(self.times):
            print('cicle {} of {}'.format(cicle, self.times))
            map = []
            for row in range(self.n):
                line = []
                for col in range(self.n):
                    neighbors = self.get_quantity_neighbors(row, col)
                    status_cell = 1 if neighbors == 2 or neighbors == 3 else 0
                    line.append(status_cell)
                map.append(line)
            self.map = map
            self.draw_map()
            time.sleep(3)
        print('end')

    def draw_map(self):
        print('-'*self.n)
        for line in self.map:
            for cell in line:
                print('█', end='') if cell else print(' ', end='')
            print()
        print('-'*self.n)

def main():
    times = 5
    n = 10
    matriz= []
    for i in range(n):
        l = []
        for j in range(n): l.append(random.randint(0,1))
        matriz.append(l)

    game = GameOfLife(matriz, times)
    game.run()

if __name__ == '__main__':
    main()
