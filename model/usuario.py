class Usuario:
    """Classe modelo de usuario

    Classe de modelo do usuário para Orientação a objetos
    """
    def __init__(self, id=None, nome=None, login=None, senha=None, perfil=None):
        self._id = id
        self._nome = nome
        self._login = login
        self._senha = senha
        self._perfil = perfil

    """Métodod Getter e Setter
    
    Métodos de controle para acesso as variáveis com segurança.
    """
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
    def login(self):
        return self._login

    @login.setter
    def login(self, valor):
        self._login = valor

    @property
    def senha(self):
        return self._senha

    @senha.setter
    def senha(self, valor):
        self._senha = valor

    @property
    def perfil(self):
        return self._perfil

    @perfil.setter
    def perfil(self, valor):
        self._perfil = valor
