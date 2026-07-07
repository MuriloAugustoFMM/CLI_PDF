# FUNCOES:
# -> CRUD FOTOS PARA A MEMÓRIA
# -> FUNCAO PARA ACRESCENTAR ESTILO NO PDF
# -> JUNTAR FOTOS DA MEMÓRIA PARA O PDF
# -> FUNCAO PARA COLETAR DADOS DO EQUIPAMENTO
# -> 

from lista_imagens.ListaImagens import ListaImagens
from lista_imagens.ObjetoImagem import ObjetoImagem
from PIL import Image
IMAGE_LIST = ListaImagens()
imagem_01 = Image.open('./MOCK/imagensTeste/image_01.jpg')
imagem_01 = ObjetoImagem(imagem_01)
imagem_02 = Image.open('./MOCK/imagensTeste/image_02.jpg')
imagem_02 = ObjetoImagem(imagem_02)
imagem_03 = Image.open('./MOCK/imagensTeste/image_03.jpg')
imagem_03 = ObjetoImagem(imagem_03)
imagem_04 = Image.open('./MOCK/imagensTeste/image_04.jpg')
imagem_04 = ObjetoImagem(imagem_04)
imagem_05 = Image.open('./MOCK/imagensTeste/image_05.jpg')
imagem_05 = ObjetoImagem(imagem_05)

IMAGE_LIST.add_imagem(imagem_01)
IMAGE_LIST.add_imagem(imagem_02)
IMAGE_LIST.add_imagem(imagem_03)
IMAGE_LIST.add_imagem(imagem_04)
IMAGE_LIST.add_imagem(imagem_05)






#CRUD.upload_Images(input(),IMAGE_LIST)

print(IMAGE_LIST.LISTA)

IMAGE_LIST.get_objimagem(0).get_imagem().show()

IMAGE_LIST.up_imagem(0,IMAGE_LIST.LISTA[1])


IMAGE_LIST.LISTA[0].get_imagem().show()


