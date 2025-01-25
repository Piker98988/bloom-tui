import unittest
from unittest.mock import patch
import bloom
import io


class TestBloom(unittest.TestCase):
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_title(self, mock_stdout):
        bloom.title("Test Title", "-", 8, True)

        expected_output = "\n-------- Test Title --------\n"
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_title_style_and_spacing(self, mock_stdout):
        bloom.title("Styled Title", borderchar="*", borderlen=5, spacesbetween=2,
                       stylebefore=f"{bloom.styles.style.BOLD}", styleafter=f"{bloom.styles.style.ITALIC}", lfbefore=False)

        expected_output = f"{bloom.styles.style.BOLD}*****{bloom.styles.style.RESET}  Styled Title  {bloom.styles.style.ITALIC}*****{bloom.styles.style.RESET}"
        self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

    @patch("sys.stdin")
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_pinput_custom_prompt(self, mock_stdout, mock_stdin):
        mock_stdin.readline.return_value = "test"

        result = bloom.pinput("What's your name?")
        self.assertEqual(result, "test")

        expected_output = f"\nWhat's your name?{bloom.styles.style.RESET}\n?>{bloom.styles.style.RESET} "
        self.assertEqual(mock_stdout.getvalue(), expected_output)

        mock_stdin.readline.assert_called_once()

    @patch("sys.stdin")
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_pinput_default(self, mock_stdout, mock_stdin):
        mock_stdin.readline.return_value = "test"

        result = bloom.pinput("Question?", autoquestion=False)
        self.assertEqual(result, "test")

        expected_output = f"\nQuestion?{bloom.styles.style.RESET}\n>>{bloom.styles.style.RESET} "
        self.assertEqual(mock_stdout.getvalue(), expected_output)

        mock_stdin.readline.assert_called_once()

    @patch("sys.stdin")
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_pinput_lfbefore(self, mock_stdout, mock_stdin):
        mock_stdin.readline.return_value = "test"

        result = bloom.pinput("Inline Question?", lfbefore=False)
        self.assertEqual(result, "test")

        expected_output = f"Inline Question?{bloom.styles.style.RESET}\n?>{bloom.styles.style.RESET} "
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch("sys.stdin")
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_pinput_custom_prefix_style(self, mock_stdout, mock_stdin):
        mock_stdin.readline.return_value = "test"

        result = bloom.pinput("Styled prompt?", customprefix="*", prefixstyle=f"{bloom.styles.style.BOLD}")
        self.assertEqual(result, "test")

        expected_output = f"\nStyled prompt?{bloom.styles.style.RESET}\n{bloom.styles.style.BOLD}*{bloom.styles.style.RESET} "
        self.assertEqual(mock_stdout.getvalue(), expected_output)

        mock_stdin.readline.assert_called_once()


if __name__ == "__main__":
    unittest.main()
