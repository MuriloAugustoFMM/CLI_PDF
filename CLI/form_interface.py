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

