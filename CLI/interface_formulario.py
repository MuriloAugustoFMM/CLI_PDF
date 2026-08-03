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