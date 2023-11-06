import pytest
from bapy import puhoo

class Tests:
    def test_puhoo_string(capsys):
        puhoo("Hello, World!")
        captured = capsys.readouterr()
        assert captured.out == "Hello, World!\n"

    def test_puhoo_multiple_arguments(capsys):
        puhoo("Hello", "World")
        captured = capsys.readouterr()
        assert captured.out == "Hello World\n"

    def test_puhoo_number(capsys):
        puhoo(1)
        captured = capsys.readouterr()
        assert captured.out == "1"
    
    def test_puhoo_object(capsys):
        puhoo({"a":"b"})
        captured = capsys.readouterr()
        assert captured.out == "{'a': 'b'}"


