import unittest

class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        #Логика следующая: чем быстрее скорость, тем меньше получится число в результате деления
        #дистанции на скорость участника. По этому показателю мы сортируем список и получаем на выходе
        #место, которое занял спортсмен и его имя
        res = sorted(([runner.name, self.full_distance / runner.speed] for runner in self.participants),
                     key=lambda x: x[1])
        return [[i + 1, res[i][0]] for i in range(len(res))]

class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_result = {}
    def setUp(self):
        self.runner1 = Runner('Usain', 10)
        self.runner2 = Runner('Andrew', 9)
        self.runner3 = Runner('Nik', 3)

    @classmethod
    def tearDownClass(cls):
        for number, tournament in cls.all_result.items():
            print(f"Номер турнира: {number}.", end= ' ')
            print("Результат: ", *tournament, end='\n')


    def test_tournament1(self):
        tour = Tournament(90, self.runner1, self.runner3)
        res = tour.start()
        TournamentTest.all_result[1] = res
        self.assertTrue(list(res)[-1][-1] == 'Nik')
    def test_tournament2(self):
        tour = Tournament(90, self.runner2, self.runner3)
        res = tour.start()
        TournamentTest.all_result[2] = res
        self.assertTrue(res[-1][-1] == 'Nik')

    def test_tournament3(self):
        tour = Tournament(90, self.runner1, self.runner2, self.runner3)
        res = tour.start()
        TournamentTest.all_result[3] = res
        self.assertTrue(res[-1][-1] == 'Nik')

if __name__ == '__main__':
    unittest.main()