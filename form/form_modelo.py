import os



#---- CRUD EQUIPAMENTOS----
EQUIPAMENTOS_PATH = './form/modelos/equipamentos'

if not os.path.exists(EQUIPAMENTOS_PATH):
    with open(EQUIPAMENTOS_PATH,'a') as f:
        f.write('EQUIPAMENTOS:\n')
        f.close()

def add_equipamento() -> str:
    eq = input('DIGITE O EQUIPAMENTO:\n\n-->  ')
    eq = eq.split('\n')[0]
    eq = eq.strip()
    with open(EQUIPAMENTOS_PATH,'a') as f:

        f.write(f'@{eq}\n')
        f.close()
    
    return 'EQUIPAMENTO REGISTRADO COM SUCESSO'

def get_equipamentos() -> list[str]:
    equipamentos = []
    with open(EQUIPAMENTOS_PATH) as f:
        lista = f.read()
        lista = lista.split('\n')
        for item in lista:
            if item.startswith('@'):
                equipamentos.append(item.replace('@',''))
        f.close()

    return equipamentos

def rm_equipamento():
    eq = input('DIGITE O EQUIPAMENTO:\n\n-->  ')
    equipamentos = get_equipamentos()
    t1 = len(equipamentos)
    for i,equipamento in enumerate(equipamentos):
         if equipamento == eq:
            equipamentos.pop(i)
    if t1 == len(equipamentos):        
        print('EQUIPAMENTO NAO ENCONTRADO')
        input('PRESSIONE ENTER PARA PROSSEGUIR:')
        return
    
    with open(EQUIPAMENTOS_PATH,'w') as f:
        for eq in equipamentos:
            f.write(f'{eq}\n')

    print('EQUIPAMENTO REMOVIDO COM SUCESSO')
    print('PRESSIONE ENTER PARA PROSSEGUIR:')


def set_equipamento():
    set_interface = 'EQUIPAMENTOS CADASTRADOS:\n\n'
    equipamentos = get_equipamentos()
    if len(equipamentos) == 0:
        print('SEM EQUIPAMENTOS CADASTRADOS')
        input('PRESSIONE ENTER PARA PROSSEGUIR:')
        return
    for i,eq in enumerate(equipamentos):
        set_interface += f'\({i}) = {eq}\n'
    set_interface += '\n<----------------------------->\n'
    print(set_interface)
    try:
        eq_old = int(input('SELECIONE O EQUIPAMENTO QUE DESEJA MUDAR:\n\n--> '))

    except Exception as e:
        print(e)
        input('PRESSIONE ENTER PARA PROSSEGUIR')
        return

    if eq_old not in range(len(equipamentos)):
        print('VALOR INVALIDO')
        input('PRESSIONE ENTER PARA PROSSEGUIR:')
        return
    
    eq_novo = input('QUAL O NOVO EQUIPAMENTO:')

    try:
        equipamentos[eq_old] = eq_novo
    except Exception as e :
        print(e)

    with open(EQUIPAMENTOS_PATH, 'w') as f:
        for i in equipamentos:
            f.write(f'@{i}\n')

    print('EQUIPAMENTO MUDADO COM SUCESSO')
    print('PRESSIONE ENTER PARA PROSSEGUIR:')
        


#-----CRUD PATRIMONIOS-----