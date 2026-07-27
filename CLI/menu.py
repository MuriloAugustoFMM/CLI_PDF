import os
from pasta_handler import upload_pasta_imagens
from form import form_modelo
from CLI import form_interface
from form.MachineDraw import MachineDraw
from form.MachineForm import MachineForm
import os
from datetime import datetime
from pdf_handler import gerador_pdf

def interface_menu_principal():
    
    MENU_OPTS = ['1','2','3']
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        comando : int | None = None
        print("""Digite o comando desejado:
            (1) = Novo PDF
            (2) = Configurações
            (3) = Sair""")
        
        comando = input()
        
        if comando not in MENU_OPTS:
            print('status da operação: COMANDO NÃO RECONHECIDO')
            input('PRESSIONE ENTER PARA CONTINUAR')
            continue
            
        if comando == MENU_OPTS[0]:

            form_img = interface_set_formulario()
            if type(form_img) != MachineDraw:
                print(f'status da operação: ERRO AO CRIAR FORMULARIO')
                input('PRESSIONE ENTER PARA CONTINUAR')
                continue
            else:
                print(f'status da operação: formulario criado com sucesso')
                input('PRESSIONE ENTER PARA CONTINUAR')
            

            lista_imagens = interface_updload_imagem()

            gerador_pdf.gerar_pdf(lista_imagens,form_img)
            print('pdf_criado')
            continue
        elif comando == MENU_OPTS[1]:
            interface_config()

        else:
            print('Programa encerrado')
            break


def interface_config():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        CONFIG_OPTS = ['1','2','3']
        print("""Escolha a opção:
            (1) = DEFINIR PASTA PADRAO
            (2) = DEFINIR OPÇÕES DO FORMULARIO
            (3) = VOLTAR""")
        
        comando = input()

        if comando not in CONFIG_OPTS:
            print('status da operação: COMANDO INVÁLIDO')
            input('PRESSIONE ENTER PARA PROSSEGUIR')
            continue

        if comando == CONFIG_OPTS[0]:
            caminho = input('Digite o caminho:\n\n-->  ')
            res = upload_pasta_imagens.set_pasta_padrao(caminho)                
            print(f'status da operação: {res}')
            input('PRESSIONE ENTER PARA PROSSEGUIR:')
            continue

        elif comando == CONFIG_OPTS[1]:
            interface_def_form()
        elif comando == CONFIG_OPTS[2]:
            return
        

def interface_def_form():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("""Selecione qual campo definir os valores do formulário:
            (1) EQUIPAMENTO
            (2) PATRIMONIO
            (3) HORIMETRO
            (4) MECANICO
            (5) OBRA
            (6) OPERADOR
            (7) VOLTAR""")
        comando : int
        try: 
            comando = int(input())

        except Exception as e :
            print(e)

        if comando > 7 or comando < 0 :
            print('COMANDO NÃO EXISTENTE')
            input('PRESSIONE ENTER PARA PROSSEGUIR:')
            continue

        os.system('cls' if os.name == 'nt' else 'clear')
        print(form_interface.INTERFACE_OPC_FORM)    
        try:

            sub_comando = int(input())

        except Exception as e:
            print(e)

        os.system('cls' if os.name == 'nt' else 'clear')
        if comando == 7:
            return
        else:
            form_interface.FUNCTIONS_OPTS[comando-1][sub_comando-1]()
            

    #mostrar opções de edicao

def interface_set_formulario() -> MachineDraw | str:
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
            return 'FORMULARIO CANCELADO'

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
        caminho = ''
        if comando not in UPLOAD_OPTS:
            print('status operação: COMANDO NÃO RECONHECIDO')
            input('PRESSIONE ENTER PARA PROSSEGUIR')
            continue
        
        if comando == UPLOAD_OPTS[0]:
            
            caminho = upload_pasta_imagens.get_pasta_padrao()

        elif comando == UPLOAD_OPTS[1]:

            print("""Informe o caminho da pasta de imagens:""")
            caminho = input()

        try:
            lista_imagens = upload_pasta_imagens.upload_Images(caminho)

        except FileNotFoundError:
                print(f'status da operação: {FileNotFoundError}')
                input('PRESSIONE ENTER PARA PROSSEGUIR')
                continue
        
        
        return lista_imagens


interface_menu_principal()

    

    