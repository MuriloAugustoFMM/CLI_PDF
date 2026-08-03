class Modelo():

    con = None

    def __init__(self, con):
        self.con = con

    def criar_modelo(self,nome:str,):
        cursor = self.con.cursor()
        cursor.execute('INSERT INTO modelos (nome) VALUES (?)',(nome,))
        self.con.commit()
    
    def sel_modelo(self,index : int = None)->list:
        cursor = self.con.cursor()
    
        if not index:
            cursor.execute(f'SELECT * FROM modelos')
        else:
            cursor.execute(f'SELECT * FROM modelos WHERE modelo_id=?',(index,))
            
        return cursor.fetchall()
    
    def del_modelo(self,index:int):
        cursor = self.con.cursor()
        cursor.execute(f'DELETE FROM modelos WHERE modelo_id={index}')
        self.con.commit()
    
    def alt_modelo(self,index:int,nome:str):
        cursor = self.con.cursor()
        cursor.execute('UPDATE modelos SET nome = ? WHERE modelo_id = ?',(nome,index))
        self.con.commit()
    
