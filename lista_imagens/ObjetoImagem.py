from PIL import Image
class ObjetoImagem():

    OBJETO : dict[str,Image.Image] | None = None
    
    PATH_PADRAO = './lista_imagens/default_imagem$$.jpg'

    IMAGEM_PADRAO = Image.open(PATH_PADRAO)

    def __init__(self):
        self.OBJETO = {'imagem': self.IMAGEM_PADRAO, 'imagem_path' : self.PATH_PADRAO}