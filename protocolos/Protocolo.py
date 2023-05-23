class Protocolo:
    def __init__(self, codigo, matricula):
        self.codigo = codigo
        self.matricula = matricula

    def solicitacao(self):
        data = [self.codigo, self.matricula]
        return data