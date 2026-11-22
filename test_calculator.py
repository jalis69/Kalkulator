"""Testy jednostkowe klasy Calculator."""
 
import runpy
 
import pytest
 
from calculator import Calculator
 
 
def test_sum():
    assert Calculator(5, 8).sum() == 13
 
 
def test_sub():
    assert Calculator(15, 8).sub() == 7
 
 
def test_mul():
    assert Calculator(8, 2).mul() == 16
 
 
def test_div():
    assert Calculator(5, 2).div() == 2.5
 
 
def test_div_by_zero():
    with pytest.raises(ZeroDivisionError, match="Nie można dzielić przez zero"):
        Calculator(5, 0).div()
 
 
def test_main(capsys):
    runpy.run_module("calculator", run_name="__main__")
    output = capsys.readouterr().out
 
    assert output.splitlines() == [
        "Dodawanie: 7",
        "Odejmowanie: 3",
        "Dzielenie: 2.5",
        "Mnozenie: 10",
        "Błąd: Nie można dzielić przez zero.",
    ]