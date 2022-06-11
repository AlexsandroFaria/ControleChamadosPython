class FecharChamadoParceiro:
    """Classe Fechar chamado Parceiro

     Classe de modelo de Fechar chamado de parceiro para orientação a objetos.
    """
    def __init__(self, id_fechar_chamado_parceiro=None, empresa_parceira=None, numero_chamado_parceiro=None,
                 chamado_simpress=None, responsavel_parceiro=None, nome_cliente=None, solucao_chamado_parceiro=None,
                 data_fechamento_chamado_parceiro=None):
        self._id_fechar_chamado_parceiro = id_fechar_chamado_parceiro
        self._empresa_parceira = empresa_parceira
        self._numero_chamado_parceiro = numero_chamado_parceiro
        self._chamado_simpress = chamado_simpress
        self._responsavel_parceiro = responsavel_parceiro
        self._nome_cliente = nome_cliente
        self._solucao_chamado_parceiro = solucao_chamado_parceiro
        self._data_fechamento_chamado_parceiro = data_fechamento_chamado_parceiro

    @property
    def id_fechar_chamado_parceiro(self):
        return self._id_fechar_chamado_parceiro

    @id_fechar_chamado_parceiro.setter
    def id_fechar_chamado_parceiro(self, valor):
        self._id_fechar_chamado_parceiro = valor

    @property
    def empresa_parceira(self):
        return self._empresa_parceira

    @empresa_parceira.setter
    def empresa_parceira(self, valor):
        self._empresa_parceira = valor

    @property
    def numero_chamado_parceiro(self):
        return self._numero_chamado_parceiro

    @numero_chamado_parceiro.setter
    def numero_chamado_parceiro(self, valor):
        self._numero_chamado_parceiro = valor

    @property
    def chamado_simpress(self):
        return self._chamado_simpress

    @chamado_simpress.setter
    def chamado_simpress(self, valor):
        self._chamado_simpress = valor

    @property
    def responsavel_parceiro(self):
        return self._responsavel_parceiro

    @responsavel_parceiro.setter
    def responsavel_parceiro(self, valor):
        self._responsavel_parceiro = valor

    @property
    def nome_cliente(self):
        return self._nome_cliente

    @nome_cliente.setter
    def nome_cliente(self, valor):
        self._nome_cliente = valor

    @property
    def solucao_chamado_parceiro(self):
        return self._solucao_chamado_parceiro

    @solucao_chamado_parceiro.setter
    def solucao_chamado_parceiro(self, valor):
        self._solucao_chamado_parceiro = valor

    @property
    def data_fechamento_chamado_parceiro(self):
        return self._data_fechamento_chamado_parceiro

    @data_fechamento_chamado_parceiro.setter
    def data_fechamento_chamado_parceiro(self, valor):
        self._data_fechamento_chamado_parceiro = valor
