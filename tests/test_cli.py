import pytest

from src.cli import _read_file, cli


class TestCLITool:

    def test_read_file__exception_not_raised(self):
        filename = "example.txt"
        try:
            _read_file(filename)
        except FileNotFoundError as exc:
            pytest.fail(f"FileNotFoundError: {exc}")

    @pytest.mark.parametrize("filename", ["./tests/test_data/empty_data.txt",
                                          "./tests/test_data/valid_data.txt",
                                          "./tests/test_data/non_valid_data__missing_args.txt",
                                          "./tests/test_data/non_valid_data__wrong_commands.txt"])
    def test_cli(self, filename):
        try:
            cli(filename)
        except Exception as exc:
            pytest.fail(f"Error during processing {filename}: {exc}")
