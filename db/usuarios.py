class Usuario():

    con = None

    def __init__(self,con):
        self.con = con


    def criar_usuario(self, nome:str, ultimo_nome:str,celular:str=None):
        cursor = self.con.cursor()
        cursor.execute('INSERT INTO usuarios (nome,ultimo_nome,celular) VALUES (?,?,?)',(nome,ultimo_nome,celular))
        self.con.commit()

    def sel_usuario(self,index:int=None)->list:
        cursor = self.con.cursor()
        if not index:
            cursor.execute('SELECT * FROM usuarios')

        else:
            cursor.execute('SELECT * FROM usuarios WHERE usuario_id = ?',(index,))

        return cursor.fetchall()

    def alt_usuario_nome(self,index:int,nome:str):
        cursor = self.con.cursor()
        cursor.execute('UPDATE usuarios SET nome = ? WHERE usuario_id = ?',(nome,index))
        self.con.commit()

    def alt_usuario_ultimo_nome(self,index:int,ultimo_nome:str):
        cursor = self.con.cursor()
        cursor.execute('UPDATE usuarios SET ultimo_nome = ? WHERE usuario_id = ?',(ultimo_nome,index))
        self.con.commit()

    def alt_usuario_cel(self,index:int,cel:str):
            cursor = self.con.cursor()
            cursor.execute('UPDATE usuarios SET celular = ? WHERE usuario_id = ?',(cel,index))
            self.con.commit()

    def del_usuario(self,index:int):
        cursor = self.con.cursor()
        cursor.execute('DELETE FROM usuarios WHERE usuario_id = ?',(index,))
    
            
