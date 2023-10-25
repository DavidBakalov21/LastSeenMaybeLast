import os
import unittest
import Functions.RetrieveReport

class TestRetrieve(unittest.TestCase):
    DIR = os.path.dirname(os.path.abspath(__file__))
    def test__TestRetrieve__Report__Report(self):
        csv = os.path.join(TestRetrieve.DIR, 'Report')
        result=Functions.RetrieveReport.RetriveDat(csv)
        self.assertEqual(result,['Report Name: Rep1\n', '2fba2529-c166-8574-2da2-eac544d82634:\n', "\t[{'min time': 3600.0}, {'max time': 25200.0}, {'dailyAverage': 43200.0}, {'WeeklyAverage': 43200.0}]\n", '2fba2529-c166-8574-2da2-eac544d826341:\n', "\t[{'min time': 3600.0}, {'max time': 25200.0}, {'dailyAverage': 43200.0}, {'WeeklyAverage': 43200.0}]\n", '\n', 'Report Name: Rep2\n', '2fba2529-c166-8574-2da2-eac544d82634:\n', "\t[{'min time': 3600.0}, {'max time': 25200.0}, {'dailyAverage': 43200.0}, {'WeeklyAverage': 43200.0}]\n", '2fba2529-c166-8574-2da2-eac544d826341:\n', "\t[{'min time': 3600.0}, {'max time': 25200.0}, {'dailyAverage': 43200.0}, {'WeeklyAverage': 43200.0}]\n", '\n']
)