# tests/test_publico.py
import pytest
from src.soluciones import evaluar_numero

def test_ejemplo_basico():
    assert evaluar_numero(5) == "positivo", "El número 5 debe ser positivo"
    assert evaluar_numero(-3) == "negativo", "El número -3 debe ser negativo"
