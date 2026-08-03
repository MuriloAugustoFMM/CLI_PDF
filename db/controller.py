#ARQUIVO controller.py
import sqlite3
from .marca import Marca
from .modelo import Modelo
from .usuarios import Usuario



with sqlite3.connect('./db/sistema.db') as con:
    con.execute('PRAGMA foreign_keys = ON')
    
    marca = Marca(con)
    modelo = Modelo(con)
    usuario = Usuario(con)

    



