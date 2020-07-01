from abc import ABC, abstractmethod
import json

storages = []


def main_menu():
    c = ""
    while True:
        print("MAIN MENU:\n1.Список хранилищ\n2.Добавить\n3.Выход")
        user_input = input("Ваш выбор: ")
        if user_input == "1":
            stores_menu()
        if user_input == "2":
            add_item()
        if user_input == "3":
            break


def stores_menu():
    ind = 0
    for i, s in enumerate(storages, 1):
        ind += i
        print(f"{i}. {s.name}")
    print(f"{ind} Предыдущее меню")
    user_input = input("Ваш выбор: ")
    if user_input == "1":
        print(storages[0])
    if user_input == "2":
        print(storages[1])
    return user_input


def add_item():
    print(f"Add printer press p")
    print(f"Add scanner press s")
    print(f"Add copier press c")
    user_input = input("Your choice: ")
    obj = ""
    if 'p' in user_input:
        producer = input("Type producer: ")
        model = input("Type model: ")
        id_num = input("Type id_num: ")
        ip = input("Type ip: ")
        obj = Copier(producer, model, id_num, ip)
    if 's' in user_input:
        producer = input("Type producer:")
        model = input("Type model: ")
        id_num = input("Type id_num: ")
        sheet_format = input("Type sheet_format: ")
        obj = Scanner(producer, model, id_num, sheet_format)
    if 'c' in user_input:
        producer = input("Type producer: ")
        model = input("Type model: ")
        id_num = input("Type id_num only digits: ")
        is_colored = input("Type is_colored True/False: ")
        obj = Scanner(producer, model, id_num, is_colored)
    obj.validate()
    s = int(input(f"Press 0 add to Tallinn \nPress 1 add to Riga: "))
    storages[s].add_to_store(obj)


def transferring(file_name, storage_from, storage_to, obj):
    storage_from.write_to_json(file_name, obj)
    storage_to.add_to_store_from_file(file_name)


class Technics(ABC):
    def __init__(self, producer, model, id_num):
        self.producer = producer
        self.model = model
        self.id_num = int(id_num)

    @abstractmethod
    def __str__(self):
        return str(f"#Producer: {self.producer} \n#Model: {self.model} \n#Id: {self.id_num}\n")

    def validate(self):
        try:
            if not str(self.id_num).isdigit():
                raise OwnError("id should be a digit")
        except OwnError as err:
            print(err)


class Printer(Technics):
    def __init__(self, producer, model, id_num, ip):
        super().__init__(producer, model, id_num)
        self.ip = ip

    def __str__(self):
        return super().__str__() + str(f"#Equipment type: {type(self).__name__} \n#Ip: {self.ip}")


class Scanner(Technics):
    def __init__(self, producer, model, id_num, sheet_format):
        super().__init__(producer, model, id_num)
        self.sheet_format = sheet_format

    def __str__(self):
        return super().__str__() + str(f"#Equipment type: {type(self).__name__} \n#Sheet_format: {self.sheet_format}")


class Copier(Technics):
    def __init__(self, producer, model, id_num, is_colored):
        super().__init__(producer, model, id_num)
        self.is_colored = is_colored

    def __str__(self):
        return super().__str__() + str(f"#Equipment type: {type(self).__name__} \n#Is_colored: {self.is_colored}")


class Storage:
    def __init__(self, name):
        self.box = {}
        self.name = name

    def __str__(self):
        return str(self.box) + self.name

    def __delitem__(self, key):
        self.box.pop(key)

    def add_to_store(self, Technics):
        key = type(Technics).__name__ + str(Technics.id_num)
        self.box.update({key: Technics})

    def add_to_store_from_file(self, file_name):
        data = self.read_from_json(file_name)
        for key, value in dict(data).items():
            self.box.update({key: value})

    @staticmethod
    def write_to_json(file_name, Technics):
        key = type(Technics).__name__ + str(Technics.id_num)
        with open(file_name, "w", encoding="utf-8") as file:
            json.dump({key: Technics.__dict__}, file, ensure_ascii=False)

    @staticmethod
    def read_from_json(file_name):
        with open(file_name) as file:
            return json.load(file)

    def transfer(self, Technics):
        key = type(Technics).__name__ + str(Technics.id_num)
        self.write_to_json("transfer.json", Technics)
        self.__delitem__(key)


class OwnError(Exception):
    def __init__(self, msg):
        self.message = msg


store_tallinn = Storage("Tallinn")
storages.append(store_tallinn)
store_riga = Storage("Riga")
storages.append(store_riga)

cop_1 = Copier("hp", 'hpm', 1, True)
cop_2 = Copier("hp", 'hrt', 2, False)
scan_1 = Scanner("Vos", "VOS1", 1, "A4")
scan_2 = Scanner("Vo", "VOL1", 2, "A4")
printer_1 = Printer("MAD", "MAD01", 1, "192.168.0.1")
printer_2 = Printer("MAD", "MAD11", 2, "192.168.0.2")
printer_3 = Printer("MADC", "MASD11", 3, "192.168.0.2")

store_tallinn.add_to_store(cop_1)
store_tallinn.add_to_store(scan_1)
store_tallinn.add_to_store(printer_1)
store_tallinn.add_to_store(printer_3)

store_riga.add_to_store(cop_1)
store_riga.add_to_store(scan_1)
store_riga.add_to_store(printer_2)
print(store_tallinn)
print(store_riga)
print("")
store_tallinn.transfer(printer_3)
transferring("transfer.json", storage_from=store_tallinn, storage_to=store_riga, obj=printer_3)
print(store_tallinn)
print(store_riga)
print("")

main_menu()
