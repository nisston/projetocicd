import pytest
from app import gerar_mensagem

def test_gerar_mensagem_sucesso():
    resultado = gerar_mensagem("Aluno")
    assert "Olá, Aluno!" in resultado

def test_gerar_mensagem_vazia():
    with pytest.raises(ValueError):
        gerar_mensagem("")