from typing import Any, override

from .menu_option import MenuOption
class OptMain(MenuOption):

    @override
    def __init__(self,name : str):
        self.name = name
        
    
    @override
    def render(self, *args,**kwargs)-> Any:
        list_opt_name = args[0]
        output_str = self.get_listed_options_string(list_opt_name)
        print(output_str)
        input('PRESSIONE ENTER')
        

    @override
    def get_listed_options_string(self,options_list)->str:
        output_str = 'SELECIONE UMA OPCAO:\n'
        for index,name in enumerate(options_list):
                    output_str += f'({index})->{name}\n'

        return output_str
                        

class OptPdf(MenuOption):

     @override
     def __init__(self,name : str):
         pass
    
     @override
     def render(self, *args,**kwargs)-> Any:
         pass 
    
     @override
     def get_listed_options_string(self,options_list):
         pass

class OptConfig(MenuOption):

    @override
    def __init__(self,name : str):
        self.name = name
        
        
    @override
    def render(self, *args,**kwargs)-> Any:
        pass

    @override
    def get_listed_options_string(self,options_list)->str:
        pass