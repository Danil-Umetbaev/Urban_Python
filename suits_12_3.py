import unittest
import tests_12_3_runner, tests_12_3_tourament
runST = unittest.TestSuite()
runST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3_runner.RunnerTest))
runST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3_tourament.TournamentTest))
start = unittest.TextTestRunner(verbosity=2)
start.run(runST)
