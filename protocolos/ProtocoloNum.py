from protocolos.Protocolo import Protocolo

class ProtrocoloNum(Protocolo):
    def __init__(self, codigo, matricula, dado):
        super().__init__(codigo, matricula)
        self.dado = dado

    def envio(self):
        data = [self.codigo, self.dado, self.matricula]
        return data
    
    def recebimento(self):
        data = [self.data]
        return data