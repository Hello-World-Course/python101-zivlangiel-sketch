import sys
from unittest import mock
import io

from test_base.test_base import AssignmentTester, Message
from test_base.test_decorator import devin_test_decorator


class TestUi(AssignmentTester):
    side_effect_input = ['Michael', '9', '3']

    def tearDown(self):
        try:
            del sys.modules['project.ui.user_interaction']
        except KeyError:
            pass

    @devin_test_decorator
    @mock.patch('sys.stdout', new_callable=io.StringIO)
    @mock.patch('builtins.input', side_effect=['Michael', '9', '3'])
    def test_first_input(self, mock_input, mock_stdout, message):
        import project.ui.user_interaction as test_file
        message.explanation = {'value': "INPUT_REQUEST_MISMATCH", 'params': {'order': 1}}
        self.assertEqualWithMessage(mock_input.call_args_list[0][0][0],
                                    "Hello, whats your name", message)

    @mock.patch('sys.stdout', new_callable=io.StringIO)
    @mock.patch('builtins.input', side_effect=side_effect_input)
    @devin_test_decorator
    def test_second_input(self, mock_input, mock_stdout, message):
        import project.ui.user_interaction as test_file
        message.explanation = {'value': "INPUT_REQUEST_MISMATCH", 'params': {'order': 2}}
        message.args = [TestUi.side_effect_input[0]]
        self.assertEqualWithMessage(mock_input.call_args_list[1][0][0],
                                    "Michael, please choose board size", message)

    @devin_test_decorator
    @mock.patch('sys.stdout', new_callable=io.StringIO)
    @mock.patch('builtins.input', side_effect=side_effect_input)
    def test_third_input(self, mock_input, mock_stdout, message):
        import project.ui.user_interaction as test_file
        message.explanation = {'value': "INPUT_REQUEST_MISMATCH", 'params': {'order': 3}}
        message.args = [TestUi.side_effect_input[1]]
        self.assertEqualWithMessage(mock_input.call_args_list[2][0][0],
                                    "Michael, for board size 9, choose number of mines to allocate", message)

    @devin_test_decorator
    @mock.patch('sys.stdout', new_callable=io.StringIO)
    @mock.patch('builtins.input', side_effect=side_effect_input)
    def test_name_var(self, mock_input, mock_stdout, message):
        import project.ui.user_interaction as test_file
        message.explanation = {'value': "GLOBAL_VAR_MISMATCH", 'params': {'var_name': 'name'}}
        message.args = [TestUi.side_effect_input[0]]
        self.assertEqualWithMessage(test_file.name, "Michael", message)

    @devin_test_decorator
    @mock.patch('sys.stdout', new_callable=io.StringIO)
    @mock.patch('builtins.input', side_effect=side_effect_input)
    def test_board_size(self, mock_input, mock_stdout, message):
        import project.ui.user_interaction as test_file
        message.explanation = {'value': "GLOBAL_VAR_MISMATCH", 'params': {'var_name': 'board_size'}}
        message.args = [TestUi.side_effect_input[1]]
        self.assertEqualWithMessage(test_file.board_size, 9, message)

    @devin_test_decorator
    @mock.patch('sys.stdout', new_callable=io.StringIO)
    @mock.patch('builtins.input', side_effect=side_effect_input)
    def test_number_of_mines(self, mock_input, mock_stdout, message):
        import project.ui.user_interaction as test_file
        message.explanation = {'value': "GLOBAL_VAR_MISMATCH", 'params': {'var_name': 'number_of_mines'}}
        message.args = [TestUi.side_effect_input[2]]
        self.assertEqualWithMessage(test_file.number_of_mines, 3, message)
