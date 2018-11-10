import palindromo_manual
import pytest

#
def test_palindromo_manual():
    assert palindromo_manual.is_palindromo(1234) == False

    assert palindromo_manual.is_palindromo(1234321) == True

    assert palindromo_manual.is_palindromo('') == False

    assert palindromo_manual.is_palindromo('hola') == False

    assert palindromo_manual.is_palindromo('holaloh') == True

    assert palindromo_manual.is_palindromo('h') == True