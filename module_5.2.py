class House:
    def __init__(self, name, number_floor):
        self.name = name
        self.numder_of_floor = number_floor

    def __len__(self):
        return self.numder_of_floor

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.numder_of_floor}."

    def go_to(self, number_floor):
        if (number_floor > self.numder_of_floor or
            number_floor < 1):
            print("Такого этажа не существует.")
        else:
            for i in range(1, number_floor+1):
                print(i)

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

# __str__
print(h1)
print(h2)

# __len__
print(len(h1))
print(len(h2))