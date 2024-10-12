class House:
    houses_history = []
    def __new__(cls, *args):
        if args:
            name = args[0]
            cls.houses_history.append(name)
        else:
            print("Название дома не указано!")
        return object.__new__(cls)
    def __init__(self, name, number_floor):
        self.name = name
        self.number_of_floor = number_floor

    def __del__(self):
        print(f'{self.name} снесён, но он останется в истории.')
    def __len__(self):
        return self.number_of_floor

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floor}."

    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floor == other.number_of_floor
        return self.number_of_floor == other

    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floor < other.number_of_floor
        return self.number_of_floor < other

    def le(self, other):
        if isinstance(other, House):
            return self.number_of_floor < other.number_of_floor
        return self.number_of_floor <= other

    def __gt__(self, other):
        if isinstance(other, House):
            return self.number_of_floor > other.number_of_floor
        return self.number_of_floor > other

    def __ge__(self, other):
        if isinstance(other, House):
            return self.number_of_floor >= other.number_of_floor
        return self.number_of_floor >= other

    def __ne__(self, other):
        if isinstance(other, House):
            return self.number_of_floor != other.number_of_floor
        return self.number_of_floor != other

    def __add__(self, other):
        if isinstance(other, House):
            return House(self.name, self.number_of_floor + other.number_of_floor)
        return House(self.name, self.number_of_floor + other)

    def __iadd__(self, other):
        if isinstance(other, House):
            return House(self.name, self.number_of_floor + other.number_of_floor)
        return House(self.name, self.number_of_floor + other)
    def __radd__(self, other):
        if isinstance(other, House):
            return House(self.name, self.number_of_floor + other.number_of_floor)
        return House(self.name, self.number_of_floor + other)

    def go_to(self, number_floor):
        if (number_floor > self.number_of_floor or
            number_floor < 1):
            print("Такого этажа не существует.")
        else:
            for i in range(1, number_floor+1):
                print(i)

h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)