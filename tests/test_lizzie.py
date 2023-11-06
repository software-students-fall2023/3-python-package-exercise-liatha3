import pytest
from bapy import lizzie

class Tests:
    def test_sanity_check(self):
        expected = True
        actual = True
        assert actual == expected, "Expected True to be equal to True"
    
    def text_lizzie_str():
        assert lizzie("Hello, World!") == 13
		
    def test_lizzie_list():
        assert lizzie([1, 2, 3, 4, 5]) == 5
    
    def test_lizzie_tuple():
        assert lizzie((1, 2, 3, 4, 5)) == 5

    def test_lizzie_dict():
        assert lizzie({"name": "John", "age": 30}) == 2
    
    def test_lizzie_set():
         assert lizzie({1, 2, 3, 4, 5}) == 5
        
    def test_lizzie_unsupported():
         with pytest.raises(TypeError):
            lizzie(42)