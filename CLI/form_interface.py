from form import form_modelo

INTERFACE_OPC_FORM = """
    SELECIONE A OPCAO:
    (1) = ADICIONAR REGISTRO
    (2) = REMOVER REGISTRO
    (3) = ALTERAR REGISTRO 
    (4) = VOLTAR"""






FUNCTIONS_OPTS = [[form_modelo.add_equipamento, form_modelo.rm_equipamento]]



def mostrar_equipamentos():
    eq_interface = ''
    #mostrar lista com as opções do tipo
    equipamentos = form_modelo.get_equipamentos()
    for eq in equipamentos:
        eq_interface += f'-> {eq} <-'

    return eq_interface


def estruc_eq():
    string = ''
    for eq in form_modelo.get_equipamentos():
        string += f'-> {eq} <-'

    return string

INTERFACE_OPC_EQ : str = estruc_eq()

