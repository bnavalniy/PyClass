"""
Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышениискорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.

"""


class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = int(speed)
        self.color = color
        self.name = name
        self.is_police = is_police
        print(f"\nspeed: {self.speed} color: {self.color} name:{self.name} is_police:{self.is_police}")

    def go(self):
        print("Going")

    def stop(self):
        print("Stopping")

    def turn(self, direction):
        print(f"Returning to : {direction}")

    def show_speed(self):
        print(f"Speed is: {self.speed}")


class TownCar(Car):
    def __init__(self, speed, color, name, is_police, speed_limit):
        super().__init__(speed, color, name, is_police, )
        self.speed_limit = int(speed_limit)

    def show_speed(self, speed):
        return print(f"Slow down your car") if int(speed) > self.speed_limit else print(f"Speed is: {speed}")


class SportCar(Car):
    pass


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police, speed_limit):
        super().__init__(speed, color, name, is_police, )
        self.speed_limit = speed_limit

    def show_speed(self, speed):
        return print(f"Slow down your car") if int(speed) > self.speed_limit else print(f"Speed is: {self.speed} \n")


class PoliceCar(Car):
    pass


c = Car(100, "Sil", "Car", False)
c.go()
c.turn("left")
c.stop()
c.show_speed()

t = TownCar(50, "Black", "TownCar", False, 60)
t.go()
t.turn("right")
t.stop()
t.show_speed(40)
t.show_speed(70)

s = SportCar(10, "Ref", "SportCar", False)
s.go()
s.turn("left")
s.stop()
s.show_speed()

w = WorkCar(20, "red", "WorkCar", False, 40)
t.go()
t.turn("right")
t.stop()
t.show_speed(30)
t.show_speed(50)


p = PoliceCar(100, "red", "PoliceCar", True)
s.go()
s.turn("left")
s.stop()
s.show_speed()