from __future__ import annotations
from PIL import Image, ImageDraw
from MachineForm import MachineForm


class MachineDraw():
    
    LARGURA, ALTURA = 800,600

    IMAGEM_DADOS : Image = None
        
    DESENHO : ImageDraw = None

    DADOS : MachineForm = None

    MAPA_DADOS : dict[MachineForm] = None


    # CRIA O FORMULARIO COM OS VALORES PADRÃO
    def __init__(self):
        
        self.DADOS = MachineForm()

        self.setDados(None)

        self.IMAGEM_DADOS = Image.new('RGB',(self.LARGURA,self.ALTURA),color='white')

        
    def getDados(self):
        return self.DADOS
    
    def getImagem(self):
        return self.IMAGEM_DADOS
    
    def setDados(self,dados : MachineForm | None):
        if(dados):
            self.DADOS.EQUIPAMENTO = dados.EQUIPAMENTO
            self.DADOS.PATRIMONIO = dados.PATRIMONIO
            self.DADOS.HORA = dados.HORA
            self.DADOS.OPERADOR = dados.OPERADOR
            self.DADOS.OBRA = dados.OBRA 
            self.DADOS.MECANICO = dados.MECANICO
            self.DADOS.DATA = dados.DATA
            return
    
    def update_dados(self):
        self.DESENHO = ImageDraw.Draw(self.IMAGEM_DADOS)

        self.__map_dados__()

        y_atual = 50    

        self.DESENHO.text((50,y_atual),'      ------FORMULARIO DA MAQUINA------',fill='black',font_size=36)
        self.DESENHO.line([0,y_atual+45,self.LARGURA,y_atual+45],fill='black',width=5)
        for chave, valor in self.MAPA_DADOS.items():
            y_atual += 50
            texto_form = f'{chave} : {valor}'
            self.DESENHO.text((50,y_atual),texto_form,fill='black',font_size=36)
            self.DESENHO.line([0,y_atual+45,self.LARGURA,y_atual+45],fill='black',width=5)

    def __map_dados__(self):

        dados = self.DADOS

        self.MAPA_DADOS = {
            'EQUIPAMENTO' : dados.EQUIPAMENTO,
            'PATRIMONIO' : dados.PATRIMONIO,
            'HORA' : dados.HORA,
            'OPERADOR' : dados.OPERADOR,
            'OBRA' : dados.OBRA,
            'MECANICO' : dados.MECANICO,
            'DATA' : dados.DATA
        }

    def ver(self):
        if(self.IMAGEM_DADOS):
            self.IMAGEM_DADOS.show()
    


meu_form = MachineDraw()
dados = meu_form.DADOS
dados.EQUIPAMENTO = 'RETROESCAVADEIRA'
dados.PATRIMONIO = 'N3089609'
dados.HORA = '12:00'
dados.OPERADOR = 'LUCAS'
dados.OBRA = 'LOG'
dados.MECANICO = 'INDIO'
dados.DATA = '30/09/2026'
meu_form.update_dados()
meu_form.ver()

        
    