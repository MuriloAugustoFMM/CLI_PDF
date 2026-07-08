from PIL import Image
from .ObjetoImagem import ObjetoImagem

class ListaImagens():

    OBJ_IMAGEM_PADRAO : ObjetoImagem | None = None

    LISTA : list[ObjetoImagem] = []

    LISTA_IMAGENS : list[Image.Image] = []

    def __init__(self):
        self.OBJ_IMAGEM_PADRAO = ObjetoImagem()
        self.LISTA.append(self.OBJ_IMAGEM_PADRAO)
        self.LISTA_IMAGENS.append(self.OBJ_IMAGEM_PADRAO.get_imagem())


    def add_objimagem(self, objimagem : ObjetoImagem | None = None, img_path : str | None = None):
        if not objimagem and img_path:
            novo_objimagem = ObjetoImagem(imagem_path=img_path)
            self.LISTA.append(novo_objimagem)
            self.LISTA_IMAGENS.append(novo_objimagem.get_imagem())
        else:
            self.LISTA.append(objimagem)
            self.LISTA_IMAGENS.append(objimagem.get_imagem())


    def rm_imagem(self,index : int = -1 ):

        if len(self.LISTA) == 0:
            return

        try:
            self.LISTA.pop(index)
            self.LISTA_IMAGENS.pop(index)
        except Exception as e:
            print(e)

    def up_imagem(self,index : int = -1,objimagem : ObjetoImagem | None = None):
        
        if not objimagem:               
            novo_objimagem = ObjetoImagem()
            self.LISTA[index] = novo_objimagem
            self.LISTA_IMAGENS[index] = novo_objimagem.get_imagem()
        else:
            self.LISTA[index] = objimagem
            self.LISTA_IMAGENS[index] = objimagem.get_imagem()

    def get_objimagem(self,index : int = 0) -> tuple[ObjetoImagem,Image.Image] | tuple[None,None] : 
        
        if self.LISTA[index] and self.LISTA_IMAGENS[index]:
            return (self.LISTA[index], self.self.LISTA_IMAGEN[index])
        
        return (None,None)
        

        

    