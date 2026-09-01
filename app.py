# FUNCOES:
# -> CRUD FOTOS PARA A MEMÓRIA
# -> FUNCAO PARA ACRESCENTAR ESTILO NO PDF
# -> JUNTAR FOTOS DA MEMÓRIA PARA O PDF
# -> FUNCAO PARA COLETAR DADOS DO EQUIPAMENTO
# -> 

#from cli import run
#from db import controller

from PIL import Image
import os
import datetime
from template_head.app import create_head_image
image_list: list[Image.Image] = []





def load_images(path):
    
    path = path.replace('"','')
    if not os.path.isdir(path):
        print('não é um diretorio')
        return
    
    for file in os.listdir(path):
        print(file)
    
        image_list.append(Image.open(f'{path}/{file}'))

def create_pdf(save_path : str, head_image : str, file_name : str,
                list_images : list[Image.Image])->None:
    head_image = Image.open(head_image)
    save_path += file_name
    head_image.save(
    fp=save_path,
    append_images=list_images)




folder_path = input('digite o path:')
load_images(folder_path)

template_data = {
    'equipamento' : input('DIGITE O EQUIPAMENTO:\n '),
    'patrimonio' : input('DIGITE O PATRIMONIO:\n '),
    'data' : datetime.date.strftime(datetime.datetime.now(),"%d-%m-%Y-%H-%M-%S"),
    'operador': input('DIGITE O OPERADOR:\n'),
    'mecanico' : input('DIGITE O MECANICO:\n')
}

head_image = create_head_image(template_data)

file_name = datetime.date.strftime(datetime.datetime.now(),'%d-%m-%Y-%H-%M-%S') + '.pdf'
save_path =f'./resultados/'

create_pdf(save_path,head_image,file_name,image_list)














