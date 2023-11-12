import conexao

def autenticacao(email,senha):
    conexao.mycursor.execute(f"SELECT * FROM tbColaborador WHERE email = '{email}' AND senha = '{senha}'") 
    return conexao.mycursor.fetchall()

class Usuario:
    def __init__(self, iptUsuario, iptSenha):
        self.usuario = iptUsuario
        self.senha = iptSenha

        self.CPUFisc = True
        self.CPULogc = True
        self.CPUFreq = True
        self.CPUPercent = True
        self.HDNumParcs = True
        self.HDTotal = True
        self.HDAtual = True
        self.HDPercent = True
        self.RAMTot = True
        self.RAMAtual = True
        self.RAMPercent = True

