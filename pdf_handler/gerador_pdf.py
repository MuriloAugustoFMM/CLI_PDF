from lista_imagens.ListaImagens import ListaImagens
from form.MachineDraw import MachineDraw
from datetime import datetime
import os

DEFAULT_PATH = './resultados'

if not os.path.exists(DEFAULT_PATH):
    os.mkdir(DEFAULT_PATH)

def gerar_pdf(obj_lista_imagens : ListaImagens| None = None,formulario : MachineDraw | None = MachineDraw(),
              save_path : str = DEFAULT_PATH):
    
    print('CRIANDO PDF-----')

    if not obj_lista_imagens:
        return

    lista_imagens = obj_lista_imagens.LISTA_IMAGENS
    imagem_head = formulario.getImagem()

    nome_arquivo = formulario.DADOS.PATRIMONIO +'-'+ formulario.DADOS.DATA
    save_path += f'/{nome_arquivo}.pdf'

    for image in lista_imagens:
        print(image)
    os
    imagem_head.save(
        fp=save_path,
        append_images= lista_imagens[1:]
    )