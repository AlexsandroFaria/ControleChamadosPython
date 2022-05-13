class Parceiro:
    """Classe modelo de Parceiro

    Classe modelo de parceiro para orientação a objetos
    """
    def __init__(self, id, nome, contato, telefone):
        self._id = id
        self._nome = nome
        self._contato = contato
        self._telefone = telefone

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, valor):
        self._id = valor

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        self._nome = valor

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
    def contato(self, valor):
        self._telefone = valor