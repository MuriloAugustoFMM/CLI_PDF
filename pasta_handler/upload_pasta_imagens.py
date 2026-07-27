from PIL import Image as i
from lista_imagens.ListaImagens import ListaImagens
from lista_imagens.ObjetoImagem import ObjetoImagem
import zipfile
import os

DEFAULT_FOLDER : str = './pasta_aux_imagens'
DEFAULT_FOLDER_FILE : str = './pasta_handler/default_folder'

if not os.path.isdir(DEFAULT_FOLDER):
    os.mkdir(DEFAULT_FOLDER)

def upload_Images(image_path : str = DEFAULT_FOLDER)-> ListaImagens | None:

    imagens_lista = ListaImagens()
    
    #Recebe um diretorio contendo imagens ou o caminho de uma imagem

    image_path = image_path.replace('"',"").replace("'","")
    

    if image_path.endswith('.zip'):
        try:
            with zipfile.ZipFile(image_path,'r') as arquivo_zip:
                
                print(image_path.replace('.zip',''))
                input()
                arquivo_zip.extractall(f'{image_path.replace('.zip','')}')
                arquivo_zip.close()
                #os.remove(image_path)
        except FileNotFoundError:
            
            raise FileNotFoundError('ARQUIVO ZIP NAO ENCONTRADO')
            
        image_path = image_path.replace('.zip','')
    
    if os.path.isdir(image_path):

        lista_imagens = os.listdir(image_path)

        for i,image in enumerate(lista_imagens):

            img_path = '/'.join([image_path,image])
            if i == 0:
                imagens_lista.up_imagem(0,img_path=img_path)
                continue
            imagens_lista.add_objimagem(img_path=img_path)   

        if len(imagens_lista.LISTA_IMAGENS) < 1:
            raise Exception('PASTA VAZIA')
        
    
    return imagens_lista      



def set_pasta_padrao(pasta_path : str ) -> str:
    pasta_path = pasta_path.replace('"','').replace("'",'')

    if not os.path.isdir(pasta_path):
        return 'DIRETORIO NAO ENCONTRADO'
    
    with open(DEFAULT_FOLDER_FILE, 'w') as f:
        f.write(pasta_path)  
        f.close()    

    return 'CAMINHO PADRAO DEFINIDO COM SUCESSO!'

def update_pasta_padrao():
    with open(DEFAULT_FOLDER_FILE,'r') as f:
        DEFAULT_FOLDER = f.read()
        f.close()

def get_pasta_padrao():
    update_pasta_padrao()
    return DEFAULT_FOLDER