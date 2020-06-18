class Stationery:
    def __init__(self, title):
        self.title = title
        print(f"\nTitle {title}")

    def draw(self):
        return print("Draw Stationery")


class Pen(Stationery):
    def draw(self):
        return print(f"Draw Pen")


class Pencil(Stationery):
    def draw(self, ):
        return print(f"Draw Pencil")


class Handle(Stationery):
    def draw(self):
        return print(f"Draw Handle")


s = Stationery("st")
s.draw()

pen = Pen("Pn")
pen.draw()

pencil = Pencil("Pencil")
pencil.draw()

handle = Handle("Handle")
handle.draw()
