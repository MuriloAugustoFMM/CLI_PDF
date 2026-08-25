from collections.abc import Callable


def interface_menu_principal(program_interfaces : list[tuple[int,str]]) -> str:
    
    comando : int | None = None

    output_str = 'OPCOES:'
    for index,_interface in program_interfaces:
        output_str +=f'({index}){_interface}' 
    
    print(output_str)
        
    comando = input()
        
    if comando not in MENU_OPTS:
        print('status da operação: COMANDO NÃO RECONHECIDO')
        input('PRESSIONE ENTER PARA CONTINUAR')
            


    




    

    