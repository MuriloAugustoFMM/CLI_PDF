from __future__ import annotations
from PIL import Image, ImageDraw


class MachineForm():
    
    DADOS : dict = {
                'EQUIPAMENTO': str,
                'PATRIMONIO': str,
                'HORA': str,
                'OPERADOR': str,
                'OBRA': str   ,
                'MECANICO': str,
                'DATA': str
            }

    LARGURA, ALTURA = 800,600

    IMAGEM_DADOS : Image = None
        
    DESENHO : ImageDraw = None


    # CRIA O FORMULARIO COM OS VALORES PADRÃO
    def __init__(self):

        self.setDados(None)

        self.IMAGEM_DADOS = Image.new('RGB',(self.LARGURA,self.ALTURA),color='white')


        
    def getDados(self):
        return self.DADOS
    
    def setDados(self,dados : MachineForm.DADOS | None):
        if(dados):
            self.DADOS['EQUIPAMENTO'] = dados.DADOS['EQUIPAMENTO']
            self.DADOS['PATRIMONIO'] = dados.DADOS['PATRIMONIO']
            self.DADOS['HORA'] = dados.DADOS['HORA']
            self.DADOS['OPERADOR'] = dados.DADOS['OPERADOR']
            self.DADOS['OBRA'] = dados.DADOS['OBRA']
            self.DADOS['DATA'] = dados.DADOS['DATA']

            return
    
    def update_dados(self):
        self.DESENHO = ImageDraw.Draw(self.IMAGEM_DADOS)

        y_atual = 50    

        self.DESENHO.text((50,y_atual),'      ------FORMULARIO DA MAQUINA------',fill='black',font_size=36)
        self.DESENHO.line([0,y_atual+45,self.LARGURA,y_atual+45],fill='black',width=5)
        for chave, valor in self.DADOS.items():
            y_atual += 50
            texto_form = f'{chave} : {valor}'
            self.DESENHO.text((50,y_atual),texto_form,fill='black',font_size=36)
            self.DESENHO.line([0,y_atual+45,self.LARGURA,y_atual+45],fill='black',width=5)

    
    def ver(self):
        if(self.IMAGEM_DADOS):
            self.IMAGEM_DADOS.show()
    


meu_form = MachineForm()
dados = meu_form.DADOS
dados['EQUIPAMENTO'] = 'RETROESCAVADEIRA'
dados['PATRIMONIO'] = 'N3089609'
dados['HORA'] = '12:00'
meu_form.OPERADOR = 'LUCAS'
meu_form.OBRA = 'LOG'
meu_form.MECANICO = 'INDIO'
meu_form.DATA = '30/09/2026'
meu_form.update_dados()
meu_form.ver()

        
    