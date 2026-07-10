import os
EQUIPAMENTOS_PATH = './form/modelos/equipamentos'

if os.path.exists(EQUIPAMENTOS_PATH):
    with open(EQUIPAMENTOS_PATH,'a') as f:
        f.write('')
        f.close()

def add_equipamento() -> str:
    eq = input('DIGITE O EQUIPAMENTO:\n\n-->  ')

    with open(EQUIPAMENTOS_PATH,'a') as f:

        f.write(f'\n{eq}')
        f.close()
    
    return 'EQUIPAMENTO REGISTRADO COM SUCESSO'

def get_equipamentos() -> list[str]:
    equipamentos = []
    with open(EQUIPAMENTOS_PATH) as f:
        equipamentos = f.read()
        equipamentos = equipamentos.split('\n')
        f.close()

    return equipamentos

def rm_equipamento():
    eq = input('DIGITE O EQUIPAMENTO:\n\n-->  ')
    equipamentos = get_equipamentos()
    t1 = len(equipamentos)
    with open(EQUIPAMENTOS_PATH,'w') as f:
        for i,equipamento in enumerate(equipamentos):
            if equipamento == eq:
                equipamentos.pop(i)
                print('EQUIPAMENTO REMOVIDO')
                input('PRESSIONE ENTER PARA PROSSEGUIR')
                continue
            f.write(f'{equipamento}\n') 
        
    if t1 == len(equipamentos):
        print('EQUIPAMENTO NÃO ENCONTRADO')
        input('PRESSIONE ENTER PARA PROSSEGUIR')
        return
    