class Marca():

    con = None

    def __init__(self, con):
        self.con = con
        
    def criar_marca(self,nome:str,):
        cursor = self.con.cursor()
        cursor.execute('INSERT INTO marcas (nome) VALUES (?)',(nome,))
        self.con.commit()

    def sel_marca(self,index : int = None)->list:
        cursor = self.con.cursor()

        if not index:
            cursor.execute(f'SELECT * FROM marcas')
        else:
            cursor.execute(f'SELECT * FROM marcas WHERE marca_id=?',(index,))
        
        return cursor.fetchall()

    def del_marca(self,index:int):
        cursor = self.con.cursor()
        cursor.execute(f'DELETE FROM marcas WHERE marca_id={index}')
        self.con.commit()

    def alt_marca(self,index:int,nome:str):
        cursor = self.con.cursor()
        cursor.execute('UPDATE marcas SET nome = ? WHERE marca_id = ?',(nome,index))
        self.con.commit()

