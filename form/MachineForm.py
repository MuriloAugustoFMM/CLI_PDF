class MachineForm():
    
    EQUIPAMENTO: str = ''
    PATRIMONIO: str = ''
    HORA: str = ''
    OPERADOR: str = ''
    OBRA: str  = ''
    MECANICO: str = ''
    DATA: str = ''
            

    MOCK_DADOS = {
        'EQUIPAMENTO' : 'RETROESCAVADEIRA',
        'PATRIMONIO' : 'N3173558',
        'HORA' : '12:41',
        'OPERADOR' : 'HEBERTH',
        'MECANICO' : 'COCERINHA',
        'DATA' : '06/07/2026'
    }

    def __init__(self):
        self.EQUIPAMENTO = self.MOCK_DADOS['EQUIPAMENTO']
        self.PATRIMONIO = self.MOCK_DADOS['PATRIMONIO']
        self.HORA = self.MOCK_DADOS['HORA']
        self.OPERADOR = self.MOCK_DADOS['OPERADOR']
        self.MECANICO = self.MOCK_DADOS['MECANICO']
        self.DATA = self.MOCK_DADOS['DATA']