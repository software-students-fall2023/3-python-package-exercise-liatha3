import pytest
from bapy import fooloo

class Tests:
    def test_sanity_check(self):
        expected = True
        actual = True
        assert actual == expected, "Expected True to be equal to True"
    
    def test_fooloo_valid():
        result = []
        def test_function(x):
            result.append(x)
        fooloo(5, 1, test_function)
        assert result == [1, 2, 3, 4, 5]

    def test_fooloo_invalid():
        def not_lambda_function(x):
            return x
        with pytest.raises(SystemExit) as error:
            fooloo(5, 1, not_lambda_function)
        assert "The 'operation' argument must be a lambda function" in str(error.value)

    def test_fooloo_n_less_than_1():
        result = []
        def test_function(x):
            result.append(x)
        fooloo(1, 5, test_function)
        assert result == []

if __name__ == "__main__":
    pytest.main()