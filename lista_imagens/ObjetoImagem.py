from PIL import Image
class ObjetoImagem():

    OBJETO : dict[str,Image.Image] | None = None
    
    PATH_PADRAO = './lista_imagens/default_imagem$$.jpg'

    IMAGEM_PADRAO = Image.open(PATH_PADRAO)

    def __init__(self, imagem : Image.Image | None = None, imagem_path : str | None = None):
        self.set_imagem(imagem,imagem_path)
        

    
    def set_imagem(self,im : Image.Image | None = None, im_path : str | None = None):

        if im:
            self.OBJETO = {'imagem': im, 'imagem_path' : im_path}

        elif im_path:

            try:
                imagem_aux = Image.open(im_path)
                self.OBJETO = {'imagem': imagem_aux, 'imagem_path' : im_path}
            except Exception as e:
                print('Não foi possível salvar a imagem informada pelo path')
                print(e)

        else:
            self.OBJETO = {'imagem': self.IMAGEM_PADRAO, 'imagem_path' : self.PATH_PADRAO}


    def get_imagem(self):
        if self.OBJETO['imagem']:
            return self.OBJETO['imagem']