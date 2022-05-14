class Cliente:
    """Classe de cliente

    Classe de modelo de Cliente para orientação a objetos.
    """
    def __init__(self, contrato=None, nome=None, endereco=None, contato=None, telefone=None, email=None):
        self._contrato = contrato
        self._nome = nome
        self._endereco = endereco
        self._contato = contato
        self._telefone = telefone
        self._email = email

    @property
    def contrato(self):
        return self._contrato

    @contrato.setter
    def contrato(self, valor):
        self._contrato = valor

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        self._nome = valor

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
