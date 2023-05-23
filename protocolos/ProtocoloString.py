from protocolos.Protocolo import Protocolo

class ProtrocoloString(Protocolo):
    def __init__(self, codigo, matricula, tamanho, dado):
        super().__init__(codigo, matricula)
        self.tamanho = tamanho
        self.dado = dado

    def envio(self):
        data = [self.codigo, self.tamanho, self.dado, self.matricula]
        return data
    
    def recebimento(self):
        data = [self.tamanho, self.data]
        return data