import conexao

def autenticar(empresa, codigoAutenticacao):
    conexao.mycursor.execute(f"SELECT idServ FROM tbServidor JOIN tbAeroporto ON fkAeroporto = idAeroporto JOIN tbEmpresa ON fkEmpresa = idEmpr WHERE idEmpr = {empresa} AND codAutentic = '{codigoAutenticacao}' ;")
    return conexao.mycursor.fetchall()

def buscarComponetes(fkServidor):
    conexao.mycursor.execute(f"SELECT idComp, fktipoComponente FROM tbComponente WHERE fkServ = {fkServidor};")
    return conexao.mycursor.fetchall()

def metricas(id):
    conexao.mycursor.execute(f"SELECT valor, fkUnidadeMedida, idMetrica FROM tbMetrica WHERE fkComponente = {id};")
    return conexao.mycursor.fetchall()

def verifExistenciaSpecs(idComponente):
    conexao.mycursor.execute(f"SELECT * FROM tbSpecs WHERE fkComponente = {idComponente};")
    resultado = conexao.mycursor.fetchall()
    print(f"idComponente: {idComponente}, resultado: {resultado}")  # Debugging line
    if resultado:
        return True
    else:
        return False

