from equation import Equation
from unittest.mock import patch
import unittest


class TestEquation(unittest.TestCase):

    @patch('equation.input')
    def test_ask_for_input(self, mock_inputs):
        """Test ask_for_input method when some inputs cannot be cast to float"""

        mock_inputs.side_effect = ['a', '/', 'test', '3']
        answer = Equation.ask_for_input()
        self.assertIsInstance(answer, float)
        self.assertEqual(answer, 3)

    @patch('equation.input')
    def test_ask_for_input_2(self, mock_inputs):
        mock_inputs.side_effect = ['-1.3', 2, '5']
        answer = Equation.ask_for_input()
        self.assertIsInstance(answer, float)
        self.assertEqual(answer, -1.3)

    @patch('equation.input')
    def test_ask_for_input_3(self, mock_inputs):
        mock_inputs.side_effect = ['a', 'testetest', 'b']
        self.assertRaises(StopIteration, Equation.ask_for_input)

    @patch('equation.input')
    def test_ask_for_continue(self, mock_inputs):
        mock_inputs.side_effect = [543, 'test', 't']
        self.assertTrue(Equation.ask_for_continue())

    @patch('equation.input')
    def test_ask_for_continue_2(self, mock_inputs):
        mock_inputs.side_effect = [543, 'N', 't']
        self.assertFalse(Equation.ask_for_continue())

