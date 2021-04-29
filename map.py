
class Map():
    def __init__(self):
        return
    def print_grid(self, name):
        for i in range(len(name)):
            for I in range(len(name[i])):
                x_num = "x" if name[i][I] == "1" else "."
                print(x_num, end = '')
            print('')
