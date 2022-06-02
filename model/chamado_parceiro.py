class ChamadoParceiro:
    """Classe chamado Parceiro

    Classe de modelo de Chamado parceiro para orientação a objetos.
    """
    def __init__(self, id_chamado=None, numero_chamado=None, chamado_simpress=None, empresa_parceira=None,
                 responsavel=None, cliente=None, problema=None, observacao=None, data_abertura=None):
        self._id_chamado = id_chamado
        self._numero_chamado = numero_chamado
        self._chamado_simpress = chamado_simpress
        self._empresa_parceira = empresa_parceira
        self._responsavel = responsavel
        self._cliente = cliente
        self._problema = problema
        self._observacao = observacao
        self._data_abertura = data_abertura

    @property
    def id_chamado(self):
        return self._id_chamado

    @id_chamado.setter
    def id_chamado(self, valor):
        self._id_chamado = valor

    @property
    def numero_chamado(self):
        return self._numero_chamado

    @numero_chamado.setter
    def numero_chamado(self, valor):
        self._numero_chamado = valor

    @property
    def chamado_simpress(self):
        return self._chamado_simpress

    @chamado_simpress.setter
    def chamado_simpress(self, valor):
        self._chamado_simpress = valor

    @property
    def empresa_parceira(self):
        return self._empresa_parceira

    @empresa_parceira.setter
    def empresa_parceira(self, valor):
        self._empresa_parceira = valor

    @property
    def responsavel(self):
        return self._responsavel

    @responsavel.setter
    def responsavel(self, valor):
        self._responsavel = valor

    @property
    def cliente(self):
        return self._cliente

    @cliente.setter
    def cliente(self, valor):
        self._cliente = valor

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
    def data_abertura(self):
        return self._data_abertura

    @data_abertura.setter
    def data_abertura(self, valor):
        self._data_abertura = valor
