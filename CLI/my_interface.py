import subprocess
from cli.my_compoent import my_component
class my_interface():

    opts : dict = {}
    counter : int = 1
    component : my_component
    name : str = ''

    def __init__(self, name : str):
        self.opts[0] = self.get_back
        self.component = my_component(self.opts)
        self.name = name

    def get_back(self):
        return

    def clear_screen(self):
        subprocess.call(args='cls')

    def add_opt(self,interface : my_interface):
        self.opts[self.counter] = interface
        self.increment_counter()
        self.add_component()

    def increment_counter(self):
        self.counter += 1

    def decrement_counter(self):
        self.counter -= 1

    def add_component(self,):
        self.component = 