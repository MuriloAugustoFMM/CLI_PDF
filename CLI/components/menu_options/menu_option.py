from collections.abc import Callable
from abc import ABC, abstractmethod
from typing import Any

class MenuOption(ABC):

    

    @abstractmethod
    def __init__(self,name : str):
        pass

    @abstractmethod
    def render(self, *args,**kwargs)-> Any:
        pass 

    @abstractmethod
    def get_listed_options_string(self,options_list):
        pass

    