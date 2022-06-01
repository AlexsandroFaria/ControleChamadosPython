class FecharChamado():
    def __init__(self, id=None, numero=None, contrato=None, nome_cliente=None, contato=None, telefone=None,
                 problema=None, tipo=None, solucao=None, status=None, data_fechamento=None):
        self._id = id
        self._numero = numero
        self._contrato = contrato
        self._nome_cliente = nome_cliente
        self._contato = contato
        self._telefone = telefone
        self._problema = problema
        self._tipo = tipo
        self._solucao = solucao
        self._status = status
        self._data_fechamento = data_fechamento

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, valor):
        self._id = valor

    @property
    def numero(self):
        return self._numero

    @numero.setter
    def numero(self, valor):
        self._numero = valor

    @property
    def contrato(self):
        return self._contrato

    @contrato.setter
    def contrato(self, valor):
        self._contrato = valor

    @property
    def nome_cliente(self):
        return self._nome_cliente

    @nome_cliente.setter
    def nome_cliente(self, valor):
        self._nome_cliente = valor

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
    def problema(self):
        return self._problema

    @problema.setter
    def problema(self, valor):
        self._problema = valor

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
    def status(self):
        return self._status

    @status.setter
    def status(self, valor):
        self._status = valor

    @property
    def data_fechamento(self):
        return self._data_fechamento

    @data_fechamento.setter
    def data_fechamento(self, valor):
        self._data_fechamento = valor
