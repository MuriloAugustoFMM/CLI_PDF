def interface_menu_principal():
    
    comando : int | None = None
    
    print("""Digite o comando desejado:
        (1) = Novo PDF
        (2) = Configurações
        (3) = Sair
        """)
        
    comando = input()
        
    if comando not in MENU_OPTS:
        print('status da operação: COMANDO NÃO RECONHECIDO')
        input('PRESSIONE ENTER PARA CONTINUAR')
            
    if comando == MENU_OPTS[0]:

        form_img = interface_set_formulario()
        if type(form_img) != MachineDraw:
            print(f'status da operação: ERRO AO CRIAR FORMULARIO')
            input('PRESSIONE ENTER PARA CONTINUAR')
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


    




    

    