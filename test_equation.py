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

    def test_calculate_delta(self):
        self.assertEqual(Equation(2, 3, 4).calculate_delta(), -23)
        self.assertEqual(Equation(1, 6, 8).calculate_delta(), 4)
        self.assertEqual(Equation(1.5, 2.2, -3).calculate_delta(), 22.84)
        self.assertEqual(Equation(-7, -3, 0).calculate_delta(), 9)
        self.assertEqual(Equation(0, 0, 0).calculate_delta(), 0)

    def test_solve_normal_equation(self):
        self.assertEqual(Equation(0, 3, 6).solve_normal_equation(), -2)
        self.assertEqual(Equation(0, -5.2, 8).solve_normal_equation(), 1.5384615384615383)
        self.assertEqual(Equation(0, 0, 6).solve_normal_equation(), None)
        self.assertEqual(Equation(0, 3, 0).solve_normal_equation(), 0)
        self.assertEqual(Equation(-0, 0, -0).solve_normal_equation(), None)

    def test_solve(self):
        self.assertEqual(Equation(1, 5, 6).solve(), (-3, -2))
        self.assertEqual(Equation(1, 6, 8).solve(), (-4, -2))
        self.assertEqual(Equation(-2.4, 6.7, -3).solve(), (2.231507130005483, 0.5601595366611841))
        self.assertEqual(Equation(5, 3, 6).solve(), None)
        self.assertEqual(Equation(0, 0, 0).solve(), None)

