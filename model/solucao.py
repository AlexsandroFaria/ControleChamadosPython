class Solucao:
    """Classe modelo de solução

    Classe de modelo de solução para Orientação a objetos
    """
    def __init__(self, id=None, solucao=None, descricao=None):
        self._id = id
        self._solucao = solucao
        self._descricao = descricao

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, valor):
        self._id = valor

    @property
    def solucao(self):
        return self._solucao

    @solucao.setter
    def solucao(self, valor):
        self._solucao = valor

    @property
    def descricao(self):
        return self._descricao

    @descricao.setter
    def descricao(self, valor):
        self._descricao = valor
