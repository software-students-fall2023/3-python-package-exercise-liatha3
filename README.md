# babPy

## Team Members
 - [Athena Leong](https://github.com/aleong2002)
 - [Harry Minsky](https://github.com/hminsky2002)
 - [Lianna Poblete](https://github.com/liannnaa)

## Project Description

"babPy" is a whimsical Python package designed to make coding concepts more accessible and fun for young children and beginners. Specifically, children who have not yet developed speech patterns but understand on an instinctive level what a for loop is.  This package replaces traditional functions and built-in class names with playful and nonsensical baby words, creating an entertaining and imaginative way to introduce coding principles to very young learners.

Key Feature of babPy:

Nonsensical Naming: babPy replaces standard Python function and class names with baby words and playful terms. For example, it might rename "print" to "puhoo" and "if" to "fuh."

## INSTALL US TODAY WITH PIP INSTALL BABPY

## Instructions

- Using babPy is as easy as 1 2 3 4 5 6 7 8. Take, for example, the function 'fuh'
  ```python
  def fuh(condition, if_true, if_false):
    """
    If Statement for babies.
    
    :param condition: Boolean condition to evaluate.
    :param if_true: Callable to execute if the condition is True.
    :param if_false: Callable to execute if the condition is False.
    :return: The result of either the if_true or if_false callable.
    """
    
    if callable(if_true) and callable(if_false):
        return if_true() if condition else if_false()
    else:
        raise ValueError("Both if_true and if_false must be callable.")

  ```

which can be used in tandem with another function, puhoo
```python
from babpy import fuh,puhoo

    fuh(1 == 2, puhoo("yay"), puhoo("boo"))

```
which will print boo, as 1 does not equal 2.



## Testing and Further Development
if you want to work on/add to babpy, just download this respository. Dependencies can be installed via pipenv and we would welcome more contributions to our special vocublary.

### [pyPi LINK](https://pypi.org/project/babPy/0.0.3/)