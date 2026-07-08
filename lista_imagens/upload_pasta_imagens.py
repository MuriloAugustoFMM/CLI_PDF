from PIL import Image as i
from lista_imagens.ListaImagens import ListaImagens
from lista_imagens.ObjetoImagem import ObjetoImagem
import os

def upload_Images(image_path : str)-> ListaImagens| None:

    imagens_lista = ListaImagens()
    
    #Recebe um diretorio contendo imagens ou o caminho de uma imagem

    if not os.path.exists(image_path):
        return None
    
    if os.path.isdir(image_path):

        for image in os.listdir(image_path):
            img_path = '/'.join([image_path,image])
            imagens_lista.add_objimagem(img_path=img_path)   
        print('\n---LISTA CRIADA COM SUCESSO!---\n')

    else:
        obj_imagem = ObjetoImagem(imagem_path=image_path)
        imagens_lista.append(obj_imagem)
        print('Imagem salva com sucesso')
    
    return imagens_lista      