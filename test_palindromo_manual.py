import palindromo_manual
import pytest

#
def test_palindromo_manual():
    res = palindromo_manual.is_palindromo(1234)
    print(res)
    assert res == False

    res = palindromo_manual.is_palindromo(1234321)
    print(res)
    assert res == True

    res = palindromo_manual.is_palindromo('')
    print(res)
    assert res == False

    res = palindromo_manual.is_palindromo('hola')
    print(res)
    assert res == False

    res = palindromo_manual.is_palindromo('holaloh')
    print(res)
    assert res == True

    res = palindromo_manual.is_palindromo('h')
    print(res)
    assert res == True