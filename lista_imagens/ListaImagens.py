from PIL import Image
from ObjetoImagem import ObjetoImagem

class ListaImagens():

    IMAGEM_PADRAO : ObjetoImagem = ObjetoImagem()

    LISTA : list = [IMAGEM_PADRAO]

    def __init__(self):
        pass

    def add_imagem(self, objimagem : ObjetoImagem | None = None):
        if not objimagem:
            self.LISTA.append(ObjetoImagem())
        else:
            self.LISTA.append(objimagem)

    def rm_imagem(self,index : int | None = None ):

        if len(self.LISTA) == 0:
            return

        if index:
            try:
                self.LISTA.pop(index)
            except Exception as e:
                print(e)
        else:
            try:
                self.LISTA.pop()
            except Exception as e:
                print(e)

    def up_imagem(self,index : int = 0,objimagem : ObjetoImagem | None = None):
        
        if not objimagem:                
            self.LISTA[index] = ObjetoImagem()
        else:
            self.LISTA[index] = objimagem

    def get_imagem(self,index : int = 0):
        
        objeto = self.LISTA[index].OBJETO
        print(objeto)
        print(f'Imagem_path: {objeto['imagem_path']}')
        objeto['imagem'].show()

        

    

minha_lista = ListaImagens()
minha_lista.up_imagem()
minha_lista.get_imagem()