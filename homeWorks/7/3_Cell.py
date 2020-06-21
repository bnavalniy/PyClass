class Cell:
    def __init__(self, cells):
        self.cells = int(cells)

    def __str__(self):
        return str(f"Quantity of cells: {self.cells}")

    def __add__(self, other):
        return self.cells + other.cells

    def __sub__(self, other):
        delta = self.cells - other.cells
        return delta if delta > 0 else str(f"{self.cells} should be greater then {other.cells}")

    def __mul__(self, other):
        return Cell(self.cells * other.cells)

    def __truediv__(self, other):
        return Cell(int(self.cells / other.cells))

    def make_order(self, columns):
        cells_to_print = self.cells
        for i in range(3):
            if divmod(cells_to_print, columns)[0] != 0:
                cells_to_print -= columns
                for c in range(columns):
                    print("*", end='')
            else:
                for c in range(self.cells % columns):
                    print("*", end='')
            print("")


c_1 = Cell(2)
c_2 = Cell(3)
print(c_1 + c_2)
print(c_1 - c_2)
print(c_1 * c_2)
print(c_2 / c_1)

c_3 = Cell(13)
c_3.make_order(5)
