class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calc_asphalt_mass(self):
        # Например: 20м * 5000м * 25кг * 5см = 12500 т
        return self._width * self._length * 25 * 1


r = Road(20, 100)
print(r.calc_asphalt_mass())
