import os
from pasta_handler import upload_pasta_imagens
from form.MachineDraw import MachineDraw
from form.MachineForm import MachineForm
import os
from datetime import datetime
from pdf_handler import gerador_pdf

def interface_menu_principal():
    
    MENU_ERROR = '' 
    MENU_OPTS = ['1','2','3']
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        comando : int | None = None
        if MENU_ERROR :
            print(f"Erro: !!! {MENU_ERROR} !!!\n")
        print("""Digite o comando desejado:
            (1) = Novo PDF
            (2) = Configurações
            (3) = Sair""")
        
        comando = input()
        MENU_ERROR = ''

        if comando not in MENU_OPTS:
            MENU_ERROR = 'COMANDO NÃO RECONHECIDO'
            continue
            
        if comando == MENU_OPTS[0]:

            form_img = interface_set_formulario()
            if form_img == None:
                MENU_ERROR = 'FORMULARIO CANCELADO'
                continue

            lista_imagens = interface_updload_imagem()
            if type(lista_imagens) == str :
                MENU_ERROR = lista_imagens
                continue
            if  len(lista_imagens.LISTA) == 1 :
                MENU_ERROR = 'LISTA DE IMAGENS VAZIA'
                continue

            gerador_pdf.gerar_pdf(lista_imagens,form_img)
            print('pdf_criado')
            continue
        elif comando == MENU_OPTS[1]:
            pass

        else:
            print('Programa encerrado')
            break


def interface_config():
    CONFIG_OPTS = ['1','2']
    print("""Escolha a opção:
          (1) = DEFINIR PASTA PADRAO
          (2) = VOLTAR""")


def interface_set_formulario() -> MachineDraw | None:
    FORM_OPTS = ['1','2','4','5','6','7','8','9']
    dados_form = MachineForm()
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        
        print(f"""Preencha o formulário:
            --------------------------------------
                (1) EQUIPAMENTO: {dados_form.EQUIPAMENTO}
                (2) PATRIMONIO: {dados_form.PATRIMONIO}
                (-) DATA: {dados_form.DATA}
                (4) HORIMETRO: {dados_form.HORA}
                (5) MECANICO: {dados_form.MECANICO}
                (6) OBRA: {dados_form.OBRA}
                (7) OPERADOR: {dados_form.OPERADOR}
            --------------------------------------
                (8) = Voltar
                (9) = Confirmar
                """)
        comando = input()

        dados_form.DATA = datetime.now().strftime("%d-%m-%Y")

        if comando == FORM_OPTS[0]:
            os.system('cls' if os.name == 'nt' else 'clear')
            dados_form.EQUIPAMENTO = input('Digite o nome do equipamento:\n\n-->  ')
        
        elif comando == FORM_OPTS[1]:
            os.system('cls' if os.name == 'nt' else 'clear')
            dados_form.PATRIMONIO = input('Digite o patrimonio:\n\n-->  ')
        
        elif comando == FORM_OPTS[2]:
            os.system('cls' if os.name == 'nt' else 'clear')
            dados_form.HORA = input('Digite o horimetro da maquina:\n\n-->  ')

        elif comando == FORM_OPTS[3]:
            os.system('cls' if os.name == 'nt' else 'clear')
            dados_form.MECANICO = input('Digite o nome do mecanico:\n\n-->  ')

        elif comando == FORM_OPTS[4]:
            os.system('cls' if os.name == 'nt' else 'clear')
            dados_form.OBRA = input('Digite o nome da obra:\n\n-->  ')

        elif comando == FORM_OPTS[5]:
            os.system('cls' if os.name == 'nt' else 'clear')
            dados_form.OPERADOR = input('Digite o nome do operador:\n\n-->  ')

        elif comando == FORM_OPTS[6]:
            return None

        elif comando == FORM_OPTS[7]:
            img_formulario = MachineDraw(dados_form)
            return img_formulario

        continue

    
def interface_updload_imagem():
    UPLOAD_OPTS = ['1','2']

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')

        print("""Selecione o tipo de upload
            (1) = DEFAULT FOLDER 
            (2) = CAMINHO DE PASTA COM IMAGENS""")
        
        comando = input()

        lista_imagens = []

        os.system('cls' if os.name == 'nt' else 'clear')

        if comando not in UPLOAD_OPTS:
            print('COMANDO NÃO RECONHECIDO')
            continue
        
        if comando == UPLOAD_OPTS[0]:
            pasta_padrao = upload_pasta_imagens.get_pasta_padrao()

            lista_imagens = upload_pasta_imagens.upload_Images(pasta_padrao)

        elif comando == UPLOAD_OPTS[1]:

            print("""Informe o caminho da pasta de imagens:""")
            caminho = input()

            lista_imagens = upload_pasta_imagens.upload_Images(caminho)
                
        return lista_imagens


interface_menu_principal()

    

    