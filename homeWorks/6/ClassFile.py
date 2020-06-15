class Trans:
    def __init__(self, name, model, year):
        self.auto_name = name
        self.auto_year = year
        self.auto_model = model
        print(f"Name{self.auto_name} Year {self.auto_year} Model {self.auto_model} ")


class Auto(Trans):
    # атрибуты
    global_count = 0

    # методы
    def on_start(self):
        print("Go")

    def on_stop(self):
        print("Stop")


auto_1 = Auto("Jora", "g5", 2012)
auto_1 = Auto("Jorsa",  "25", 2011)
