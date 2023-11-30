package plane.it.banco;

import org.springframework.jdbc.core.BeanPropertyRowMapper;
import org.springframework.jdbc.core.JdbcTemplate;
import plane.it.Servidores;
import plane.it.Usuario;
import plane.it.banco.tabelas.Componente;


import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.List;

public class OperacoesBanco {

    Conexao conexao = new Conexao();
    ConexaoSql conexaoSql = new ConexaoSql();
    JdbcTemplate con = conexao.getConexaoBanco();
    JdbcTemplate conSql = conexaoSql.getConexaoBanco();

    DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy/MM/dd HH:mm:ss");
    LocalDateTime dataAtual = LocalDateTime.now();
    private int servidor;

    public OperacoesBanco(){}

    public OperacoesBanco(int servidor) {
        this.servidor = servidor;
    }

    public String autenticarUsuario(String senha, String email){

        List <Usuario> listaUsuario = con.query(
                "SELECT * FROM tbColaborador WHERE senha = ? AND email = ?",
                new BeanPropertyRowMapper <>(Usuario.class),senha,email);


        if (!listaUsuario.isEmpty()){

            return listaUsuario.get(0).getFkAeroporto();

        }else {

            return null;

        }

    }

    public int autenticarServidor(String codigo,String fkAeroporto){

        List <Servidores> listaServidores = con.query(
                "SELECT * FROM tbServidor WHERE codAutentic = ? AND fkAeroporto = ?",
                new BeanPropertyRowMapper <>(Servidores.class),codigo,fkAeroporto
        );

        if (!listaServidores.isEmpty()){

            return listaServidores.get(0).getIdServidor();

        }else {

            return 1;

        }

    }

    public void sistemaOperacional(String sistemaOperacional){
        con.update("UPDATE tbServidor SET sistemaOP = ? WHERE idServ = ?;",sistemaOperacional,servidor);
        conSql.update("UPDATE tbServidor SET sistemaOP = ? WHERE idServ = ?;",sistemaOperacional,servidor);

    }

   public void  memoriaRamTotal(Long total){
        Double totalMemoria = converter(total);
        con.update("INSERT INTO tbMetrica VALUES(NULL,?,2,1)",totalMemoria);
        conSql.update("INSERT INTO tbMetrica VALUES(DEFAULT,?,2,1)",totalMemoria);
   }

   public void memoriaRamEmUso(Long memoriaEmUso,Long total){
       Double totalMemoriaEmUso = converter(memoriaEmUso);
       Double totalMemoria = converter(total);

       Boolean alerta = totalMemoriaEmUso >= (totalMemoria * 0.70);

       con.update("INSERT INTO tbRegistro VALUES(NULL,?,?,?,?,2,1)",totalMemoriaEmUso,
               formatter.format(dataAtual), alerta,servidor);
       con.update("INSERT INTO tbRegistro VALUES(DEFAULT,?,?,?,?,2,1)",totalMemoriaEmUso,
               formatter.format(dataAtual), alerta,servidor);

    }

    public void nomeProcessador(String nome){
        con.update("UPDATE tbComponente SET nome = ? WHERE idComp = 1;",nome);
        conSql.update("UPDATE tbComponente SET nome = ? WHERE idComp = 1;",nome);

    }

    public void frequenciaProcessador(Long frequencia){
        Double frequenciaTratada = (double) frequencia / 1000000000;
        con.update("INSERT INTO tbRegistro VALUES(NULL,?,?,?,?,1,2)",frequenciaTratada,
                formatter.format(dataAtual), false,servidor);
        conSql.update("INSERT INTO tbRegistro VALUES(DEFAULT,?,?,?,?,1,2)",frequenciaTratada,
                formatter.format(dataAtual), false,servidor);
    }

    public void usoProcessador(Double uso){
        con.update("INSERT INTO tbRegistro VALUES(NULL,?,?,?,?,1,2)",uso, formatter.format(dataAtual), false,
                servidor);
        conSql.update("INSERT INTO tbRegistro VALUES(DEFAULT,?,?,?,?,1,2)",uso, formatter.format(dataAtual), false,
                servidor);


    }

    public void nucleosProcessador(Integer nuclesFisicos){
        con.update("INSERT INTO tbRegistro VALUES(NULL,?,?,?,?,null,4)",nuclesFisicos,
                formatter.format(dataAtual), false,servidor);
        conSql.update("INSERT INTO tbRegistro VALUES(DEFAULT,?,?,?,?,null,4)",nuclesFisicos,
                formatter.format(dataAtual), false,servidor);
    }

    public void temperatura(Double temperatura){
        con.update("INSERT INTO tbRegistro VALUES(NULL,?,?,?,?,1,3)",temperatura, formatter.format(dataAtual),
                false,servidor);
        conSql.update("INSERT INTO tbRegistro VALUES(DEFAULT,?,?,?,?,1,3)",temperatura, formatter.format(dataAtual),
                false,servidor);

    }

    public void volumeTotal(Long volumeTotal){
        Double volumeTotalTratado = converter(volumeTotal);
        con.update("INSERT INTO tbMetrica VALUES(NULL,?,3,1)",volumeTotalTratado);
        conSql.update("INSERT INTO tbMetrica VALUES(DEFAULT,?,3,1)",volumeTotalTratado);
    }

    public void volumeEmUso(Long volumeDisponivel,Long volumeTotal){
        Double volumeEmUsoTratado = converter(volumeTotal) - converter(volumeDisponivel);
        con.update("INSERT INTO tbRegistro VALUES(NULL,?,?,?,?,3,4)",volumeEmUsoTratado,
                formatter.format(dataAtual),false,servidor);
        conSql.update("INSERT INTO tbRegistro VALUES(DEFAULT,?,?,?,?,3,4)",volumeEmUsoTratado,
                formatter.format(dataAtual),false,servidor);

    }



    public void quatidadeProcessos(Integer quatidadeProcessos){
        con.update("INSERT INTO tbRegistro VALUES(NULL,?,?,?,?,NULL,5)",quatidadeProcessos,
                formatter.format(dataAtual),false,servidor);
        conSql.update("INSERT INTO tbRegistro VALUES(DEFAULT,?,?,?,?,NULL,5)",quatidadeProcessos,
                formatter.format(dataAtual),false,servidor);
    }

   public Double converter(Long medida){
       Double converterMemoria = (double) medida / 1000000000;
       return (double) Math.floor(converterMemoria);
   }

    public List<Componente> buscarComponentes(Integer idServidor){
        return con.query("SELECT * FROM tbComponente WHERE fkServ = ?;",
                new BeanPropertyRowMapper<>(Componente.class),
                idServidor);
    }

    public boolean verificarExistencia(int fkComponente, int fkUnidadeMedida) {
        String sql = "SELECT COUNT(*) FROM tbSpecs WHERE fkComponente = ? AND fkUnidadeMedida = ?";

        int count = con.queryForObject(sql, Integer.class, fkComponente, fkUnidadeMedida);

        // Se count for maior que zero, significa que a combinação já existe na tabela
        return count > 0;
    }

    public boolean cadastrarSpcecs(Double valor, String fkComp, Integer fkMedida) {
        if (fkComp == null) {
            System.out.println("fkComp is null");
            return false;
        }

        try {
            if (verificarExistencia(Integer.parseInt(fkComp), fkMedida)) {
                return false;
            }

            String sql = "INSERT INTO tbSpecs (valor, fkComponente, fkUnidadeMedida) VALUES (?, ?, ?)";
            con.update(sql, valor, fkComp, fkMedida);
            conSql.update(sql, valor, fkComp, fkMedida);
            return true;

        } catch (Exception e) {
            System.out.println("An unexpected error occurred");
            e.printStackTrace();
            return false;
        }
    }
}
