import sys
from unittest import mock
import io

from test_base.test_base import AssignmentTester
from test_base.test_decorator import devin_test_decorator


class TestUi(AssignmentTester):

    def tearDown(self):
        try:
            del sys.modules['project.ui.user_interaction']
        except KeyError:
            pass

    @devin_test_decorator
    @mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_first_output(self, mock_stdout, message):
        import assignment_lesson_4.hello_world as test_file
        message.explanation = {'value': "STD_OUT_MISMATCH"}
        self.assertEqualWithMessage(mock_stdout.getvalue(), "Hello World I Love Python!\n", message)
