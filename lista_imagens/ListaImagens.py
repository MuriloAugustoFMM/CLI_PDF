from PIL import Image
from .ObjetoImagem import ObjetoImagem

class ListaImagens():

    OBJ_IMAGEM_PADRAO : ObjetoImagem | None = None

    LISTA : list = []

    def __init__(self):
        self.OBJ_IMAGEM_PADRAO = ObjetoImagem()
        self.LISTA.append(self.OBJ_IMAGEM_PADRAO)


    def add_imagem(self, objimagem : ObjetoImagem | None = None):
        if not objimagem:
            self.LISTA.append(ObjetoImagem())
        else:
            self.LISTA.append(objimagem)


    def rm_imagem(self,index : int = -1 ):

        if len(self.LISTA) == 0:
            return

        try:
            self.LISTA.pop(index)
        except Exception as e:
            print(e)

    def up_imagem(self,index : int = -1,objimagem : ObjetoImagem | None = None):
        
        if not objimagem:                
            self.LISTA[index] = ObjetoImagem()
        else:
            self.LISTA[index] = objimagem

    def get_objimagem(self,index : int = 0) -> ObjetoImagem | None : 
        
        if self.LISTA[index]:
            return self.LISTA[index]
        

        

    