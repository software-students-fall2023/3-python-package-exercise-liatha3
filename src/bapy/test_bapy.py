import pytest
from bapy import puhoo, fooloo, fuh, wuhoo


# fuh should call the correct callable based on the condition
def test_fuh():
    assert fuh(True, lambda: 1, lambda: 0) == 1
    assert fuh(False, lambda: 1, lambda: 0) == 0

    # Test that non-callables raise an error
    with pytest.raises(ValueError):
        fuh(True, "not a callable", lambda: 0)