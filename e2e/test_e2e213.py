import os
import unittest
from unittest.mock import patch
import main


class E2E210(unittest.TestCase):

    DIR = os.path.dirname(os.path.abspath(__file__))
    csv = os.path.join(DIR, 'Report')

    @patch('builtins.input',
           side_effect=['2', '13',csv])
    def test_get_historical_data(self, mock_input):
        result = main.main()
        self.assertEqual(result,['Report Name: Rep1\n', '2fba2529-c166-8574-2da2-eac544d82634:\n', "\t[{'min time': 3600.0}, {'max time': 25200.0}, {'dailyAverage': 43200.0}, {'WeeklyAverage': 43200.0}]\n", '2fba2529-c166-8574-2da2-eac544d826341:\n', "\t[{'min time': 3600.0}, {'max time': 25200.0}, {'dailyAverage': 43200.0}, {'WeeklyAverage': 43200.0}]\n", '\n', 'Report Name: Rep2\n', '2fba2529-c166-8574-2da2-eac544d82634:\n', "\t[{'min time': 3600.0}, {'max time': 25200.0}, {'dailyAverage': 43200.0}, {'WeeklyAverage': 43200.0}]\n", '2fba2529-c166-8574-2da2-eac544d826341:\n', "\t[{'min time': 3600.0}, {'max time': 25200.0}, {'dailyAverage': 43200.0}, {'WeeklyAverage': 43200.0}]\n", '\n'])