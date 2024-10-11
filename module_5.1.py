class House:
    def __init__(self, name, number_floor):
        self.name = name
        self.numder_of_floor = number_floor

    def go_to(self, number_floor):
        if (number_floor > self.numder_of_floor or
            number_floor < 1):
            print("Такого этажа не существует.")
        else:
            for i in range(1, number_floor+1):
                print(i)

h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)
