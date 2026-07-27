from form import form_modelo

INTERFACE_OPC_FORM = """
    SELECIONE A OPCAO:
    (1) = ADICIONAR REGISTRO
    (2) = REMOVER REGISTRO
    (3) = ALTERAR REGISTRO
    (4) = VER REGISTROS 
    (4) = VOLTAR"""


def mostrar_equipamentos():
    eq_interface = ''
    #mostrar lista com as opções do tipo
    equipamentos = form_modelo.get_equipamentos()
    for eq in equipamentos:
        eq_interface += f'-> {eq} <-\n'

    print(eq_interface)
    input('PRESSIONE ENTER PARA PROSSEGUIR')


FUNCTIONS_OPTS = [
    [form_modelo.add_equipamento, form_modelo.rm_equipamento, form_modelo.set_equipamento,mostrar_equipamentos]

    ]

