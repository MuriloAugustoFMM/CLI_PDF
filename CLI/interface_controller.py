from cli import config, menu
from .components.menu_options.options import OptMain, OptConfig, MenuOption

class InterfaceController():


    def __init__(self):
        #start point
        self._main_menu = OptMain('menu_principal')

        #other menu options
        _config = OptConfig('configuracoes')

        #tuple of menu options
        self.menu_option_tuple : tuple[MenuOption] = (_config,)

    def render(self, index : int) -> None:
        try:
            opt_menu = self.menu_option_tuple[index]
            opt_menu.render()
            
        except IndexError as e:
            raise e('OPCAO DE MENU INVALIDA')
        
    
    def start(self) -> None:
       
       self._main_menu.render(self.get_name_list())


    def get_name_list(self)-> list[str]:
        name_list = []
        for opt_menu in self.menu_option_tuple:
            name_list.append(opt_menu.name)
        return name_list
        


    
        