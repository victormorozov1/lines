class Way:
    def __init__(self, arr=[]):
        self.arr = arr

    def append(self, x, y):
        self.arr.append([x, y])

    def go(self):
        for i in range(len(self.arr) - 2, 0, -1):
            yield self.arr[i + 1], self.arr[i]

    def len(self):
        return len(self.arr)

    def __str__(self):
        r = ''
        for i in self.arr[:-1:]:
            r += f'({i[0]}, {i[1]}) --> '
        return r + f'({self.arr[-1][0]}, {self.arr[-1][1]})'
