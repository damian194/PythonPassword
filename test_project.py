import os
import pytest
from finalproject.project import request_password, save_password, load_passwords

@pytest.fixture
def test_password():
    return "TestPassword123"

def test_request_password_valid():
    with pytest.raises(SystemExit):
        input_values = ["TestPassword123\n"]
        input_mock = lambda _: input_values.pop(0)

        with pytest.raises(SystemExit):
            request_password()

def test_request_password_invalid():
    with pytest.raises(SystemExit):
        input_values = ["short\n", "NoDigitsHere\n", "NoUpperCase\n", "ValidPassword123\n"]
        input_mock = lambda _: input_values.pop(0)

        with pytest.raises(SystemExit):
            request_password()

def test_save_password(test_password):
    save_password(test_password)

    with open('passwords.txt', 'r') as file:
        passwords = file.readlines()
        assert test_password + '\n' in passwords

def test_load_passwords(test_password, capsys):
    save_password(test_password)

    load_passwords()
    captured = capsys.readouterr()
    assert f"Stored passwords:\n1. {test_password}\n" in captured.out

def test_load_passwords_no_file(capsys):
    with pytest.raises(SystemExit):
        load_passwords()
        captured = capsys.readouterr()
        assert "No passwords stored.\n" in captured.out

def pytest_sessionfinish(session, exitstatus):
    if os.path.exists("passwords.txt"):
        os.remove("passwords.txt")


