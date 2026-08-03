class my_component():

    options_names = list[str]
    content = ''

    def __init__(self, opts : dict):
        self.options_names = []

    def add_option_name(self,option_name:str):
        self.options_names.append(option_name)

    def rem_option_name(self,index:int):
        self.options_names.pop(index)

    def show_content(self):
        print(self.content)

    def get_content(self)-> str:
        return self.content

    def set_content(self):
        content = '--INICIO--\n'
        options_names = self.options_names

        for i,item in enumerate(options_names):
            content += f'({i+1}) -> {item}\n'
            
        content += '--FIM--\n'
        self.content = content