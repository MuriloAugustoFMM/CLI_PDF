from PIL import Image as i
import os

def upload_Images(image_path : str, images_list : list):

    #Recebe um diretorio contendo imagens ou o caminho de uma imagem

    if os.path.exists(image_path):

        if os.path.isdir(image_path):

            print('O caminho é um diretório:\n')

            images_dir = image_path
            for image in os.listdir(image_path):
                img_path = '/'.join([image_path,image])
                try:
                    print(f'\t--> imagem: {img_path}')
                    img = i.open(img_path)
                    print('\tImagem Salva com sucesso')
                except Exception:
                    print('\tFalha ao salvar imagem\n\n')
                    print(f"caminho: {image} não é uma imagem válida")
                    continue
                
                print('\n---LISTA CRIADA COM SUCESSO!---\n')

                images_list.append(img)
            
            return images_list

        try:
            images_list.append(i.open(image_path))
            print('Imagem salva com sucesso')
        except Exception:
            print(f'caminho: {img-path} não é uma imagem válida') 

        return images_list      