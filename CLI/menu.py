import os
from lista_imagens import upload_pasta_imagens
from form.MachineDraw import MachineDraw
from form.MachineForm import MachineForm
from datetime import datetime
from pdf_handler import gerador_pdf

MENU_OPTS = ['1','2']


def interface_menu_principal():

    comando : int | None = None

    print("""
          Digite o comando desejado:
            (1) = Novo PDF 
            (2) = Sair
          """)
    
    comando = input()
    
    if comando not in MENU_OPTS:
        print('COMANDO NÃO RECONHECIDO')
        return
    
    if comando == MENU_OPTS[0]:
        form_img = interface_set_formulario()
        lista_imagens = interface_updload_imagem()
        gerador_pdf.gerar_pdf(lista_imagens,form_img)
        print('pdf_criado')
    else:
        print('Programa encerrado')
        


def interface_set_formulario():

    dados_form = MachineForm()

    print("""Preencha o formulário:""")
    dados_form.EQUIPAMENTO = input('Qual o tipo de equipamento?')
    dados_form.PATRIMONIO = input('Qual o patrimonio?')
    dados_form.DATA = datetime.now().strftime('%d.%m.%y %H-%M-%S')
    dados_form.HORA = input('Qual o horimetro?')
    dados_form.MECANICO = input('Qual o mecanico?')
    dados_form.OBRA = input('Qual a obra?')
    dados_form.OPERADOR = input('Qual o operador?')
    
    img_formulario = MachineDraw(dados_form)

    return img_formulario
    
    

def interface_updload_imagem():
    print("""Informe o caminho da pasta de imagens:""")
    caminho = input()
    caminho = caminho.replace('"',"").replace("'","")

    lista_imagens = upload_pasta_imagens.upload_Images(caminho)
    print(lista_imagens.LISTA_IMAGENS)
    return lista_imagens


interface_menu_principal()

    

    