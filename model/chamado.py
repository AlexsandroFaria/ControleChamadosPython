class Chamado:
    """Classe Chamado

    Classe de modelo de Chamado para orientação a objetos.
    """
    def __init__(self, id=None,
                 numero_chamado=None,
                 numero_contrato=None,
                 nome_cliente=None,
                 endereco=None,
                 contato=None,
                 telefone=None,
                 email=None,
                 problema=None,
                 observacao=None,
                 status=None,
                 tipo=None,
                 solucao=None,
                 data_abertura=None,
                 data_atualizacao=None,):
        self._id = id
        self._numero_chamado = numero_chamado
        self._numero_contrato = numero_contrato
        self._nome_cliente = nome_cliente
        self._endereco = endereco
        self._contato = contato
        self._telefone = telefone
        self._email = email
        self._problema = problema
        self._observacao = observacao
        self._status = status
        self._tipo = tipo
        self._solucao = solucao
        self._data_abertura = data_abertura
        self._data_atualizacao = data_atualizacao

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, valor):
        self._id = valor

    @property
    def numero_chamado(self):
        return self._numero_chamado

    @numero_chamado.setter
    def numero_chamado(self, valor):
        self._numero_chamado = valor

    @property
    def numero_contrato(self):
        return self._numero_contrato

    @numero_contrato.setter
    def numero_contrato(self, valor):
        self._numero_contrato = valor

    @property
    def nome_cliente(self):
        return self._nome_cliente

    @nome_cliente.setter
    def nome_cliente(self, valor):
        self._nome_cliente = valor

    @property
    def endereco(self):
        return self._endereco

    @endereco.setter
    def endereco(self, valor):
        self._endereco = valor

    @property
    def contato(self):
        return self._contato

    @contato.setter
    def contato(self, valor):
        self._contato = valor

    @property
    def telefone(self):
        return self._telefone

    @telefone.setter
    def telefone(self, valor):
        self._telefone = valor

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, valor):
        self._email = valor

    @property
    def problema(self):
        return self._problema

    @problema.setter
    def problema(self, valor):
        self._problema = valor

    @property
    def observacao(self):
        return self._observacao

    @observacao.setter
    def observacao(self, valor):
        self._observacao = valor

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, valor):
        self._status = valor

    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, valor):
        self._tipo = valor

    @property
    def solucao(self):
        return self._solucao

    @solucao.setter
    def solucao(self, valor):
        self._solucao = valor

    @property
    def data_abertura(self):
        return self._data_abertura

    @data_abertura.setter
    def data_abertura(self, valor):
        self._data_abertura = valor

    @property
    def data_atualizacao(self):
        return self._data_atualizacao

    @data_atualizacao.setter
    def data_atualizacao(self, valor):
        self._data_atualizacao = valor
