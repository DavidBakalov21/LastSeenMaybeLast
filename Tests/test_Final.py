import os
import unittest
import Functions.FInal

class TestRetrieve(unittest.TestCase):
    def test__TestFinal__Report__Report(self):
        result=Functions.FInal.ShowFirst()
        self.assertEqual(result,{'Doug93': {'lastSeenDate': '2023-10-10T10:28:41.988544+00:00', 'id': '2fba2529-c166-8574-2da2-eac544d82634'}, 'Doug933': {'lastSeenDate': '2023-10-10T12:28:41.988544+00:00', 'id': '2fba2529-c166-8574-2da2-eac544d82634'}, 'Doug934': {'lastSeenDate': '2023-10-10T17:28:41.988544+00:00', 'id': '2fba2529-c166-8574-2da2-eac544d82634'}, 'Doug935': {'lastSeenDate': '2023-10-10T19:28:41.988544+00:00', 'id': '2fba2529-c166-8574-2da2-eac544d82634'}, 'Doug936': {'lastSeenDate': '2023-10-11T12:28:41.988544+00:00', 'id': '2fba2529-c166-8574-2da2-eac544d82634'}, 'Doug937': {'lastSeenDate': '2023-10-11T13:28:41.988544+00:00', 'id': '2fba2529-c166-8574-2da2-eac544d82634'}, 'Doug938': {'lastSeenDate': '2023-10-11T19:28:41.988544+00:00', 'id': '2fba2529-c166-8574-2da2-eac544d82634'}, 'Doug939': {'lastSeenDate': '2023-10-10T20:28:41.988544+00:00', 'id': '2fba2529-c166-8574-2da2-eac544d82634'}, 'Doug930': {'lastSeenDate': '2023-10-10T21:28:41.988544+00:00', 'id': '2fba2529-c166-8574-2da2-eac544d82634'}}
                         )