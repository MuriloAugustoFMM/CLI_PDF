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