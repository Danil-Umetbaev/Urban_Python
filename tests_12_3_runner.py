import unittest
class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name





class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, "Временно заморозили")
    def test_walk(self):
        test_runner = Runner('Usain')
        for _ in range(10):
            test_runner.walk()
        self.assertEqual(test_runner.distance, 50)

    @unittest.skipIf(is_frozen, "Временно заморозили")
    def test_run(self):
        test_runner = Runner("Usain")
        for _ in range(10):
            test_runner.run()
        self.assertEqual(test_runner.distance, 100)

    @unittest.skipIf(is_frozen, "Временно заморозили")
    def test_challenge(self):
        test_walker = Runner('Walker')
        test_runner = Runner('Runner')
        for _ in range(10):
            test_walker.walk()
            test_runner.run()
        self.assertNotEqual(test_runner.distance, test_walker.distance)

if __name__ == '__main__':
    unittest.main()