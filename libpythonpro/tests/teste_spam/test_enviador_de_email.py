import pytest

from libpythonpro.spam.enviador_de_email import Enviador, EmailInvalido


def test_criar_enviador_de_email():
    enviador= Enviador()
    assert enviador is not None


@pytest.mark.parametrize(
    'remetente',
    ['renzo@python.pro.br', 'foo@bar.com.br'],
)
def test_remetente(remetente):
    enviador=Enviador()
    resultado=enviador.enviar(
        remetente,
        'luciano@python.pro.br',
        'Cursos python pro',
        'Primeira turma Guido Van Rossum aberta'
    )
    assert remetente in resultado


@pytest.mark.parametrize(
    'remetente',
    [' ', 'renzo']
)
def test_remetente_invalido(remetente):
    enviador=Enviador()
    with pytest.raises(EmailInvalido):
        enviador.enviar(
            remetente,
            'luciano@python.pro.br',
            'Cursos python pro',
            'Primeira turma Guido Van Rossum aberta'
    )
