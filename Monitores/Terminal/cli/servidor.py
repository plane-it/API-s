import conexao

def autenticar(empresa, codigoAutenticacao):
    conexao.mycursor.execute(f"SELECT idServ FROM tbServidor JOIN tbAeroporto ON fkAeroporto = idAeroporto JOIN tbEmpresa ON fkEmpresa = idEmpr WHERE idEmpr = {empresa} AND codAutentic = '{codigoAutenticacao}' ;")
    return conexao.mycursor.fetchall()

def buscarComponetes(fkServidor):
    conexao.mycursor.execute(f"SELECT idComp, fktipoComponente FROM tbComponente WHERE fkServ = {fkServidor};")
    return conexao.mycursor.fetchall()
