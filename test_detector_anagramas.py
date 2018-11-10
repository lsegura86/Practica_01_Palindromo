import detector_anagramas
import pytest

# Prueba el metodo de deteccion de anagramas
def test_anagramas():
    assert detector_anagramas.detector_anagramas('123', '123') == True
    assert detector_anagramas.detector_anagramas('abcde', 'edab') == False
    assert detector_anagramas.detector_anagramas('hola12', '12laho') == True
    assert detector_anagramas.detector_anagramas('3#a', 'a#3') == True
    assert detector_anagramas.detector_anagramas('a', 'edab') == False
    assert detector_anagramas.detector_anagramas('345', 'b') == False
    assert detector_anagramas.detector_anagramas('', 'edab') == False
    assert detector_anagramas.detector_anagramas(123, 321) == True
    assert detector_anagramas.detector_anagramas(123, '321') == True