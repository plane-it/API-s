package plane.it;

import org.springframework.jdbc.core.BeanPropertyRowMapper;
import org.springframework.jdbc.core.JdbcTemplate;

import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.List;

public class OperacoesBanco {

    Conexao conexao = new Conexao();
    JdbcTemplate con = conexao.getConexaoDoBanco();
    DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy/MM/dd HH:mm:ss");
    LocalDateTime dataAtual = LocalDateTime.now();

    public Boolean autenticarUsuario(String senha, String email){
        List <Usuario> listaUsuario = con.query(
                "SELECT * FROM tbColaborador WHERE senha = ? AND email = ?",
                new BeanPropertyRowMapper <>(Usuario.class),
                senha,email);

        return !listaUsuario.isEmpty();

    }

    public void sistemaOperacional(String sistemaOperacional){
        con.update("UPDATE tbServidor SET sistemaOP = ? WHERE idServ = 1;",sistemaOperacional);

    }

   public void  memoriaRamTotal(Long total){
        Double totalMemoria = converter(total);
        con.update("INSERT INTO tbMetrica VALUES(NULL,?,2,1)",totalMemoria);
   }

   public void memoriaRamEmUso(Long memoriaEmUso,Long total){
       Double totalMemoriaEmUso = converter(memoriaEmUso);
       Double totalMemoria = converter(total);

       Boolean alerta = totalMemoriaEmUso >= (totalMemoria * 0.70);

       con.update("INSERT INTO tbRegistro VALUES(NULL,?,?,?,1,2,1)",totalMemoriaEmUso,
               formatter.format(dataAtual), alerta);

    }

    public void nomeProcessador(String nome){
        con.update("UPDATE tbComponente SET nome = ? WHERE idComp = 1;",nome);
    }

    public void frequenciaProcessador(Long frequencia){
        Double frequenciaTratada = (double) frequencia / 1000000000;
        con.update("INSERT INTO tbRegistro VALUES(NULL,?,?,?,1,1,2)",frequenciaTratada,
                formatter.format(dataAtual), false);
    }

    public void usoProcessador(Double uso){
        con.update("INSERT INTO tbRegistro VALUES(NULL,?,?,?,1,1,2)",uso, formatter.format(dataAtual), false);

    }

    public void nucleosProcessador(Integer nuclesFisicos){
        con.update("INSERT INTO tbRegistro VALUES(NULL,?,?,?,1,null,4)",nuclesFisicos,
                formatter.format(dataAtual), false);
    }

    public void temperatura(Double temperatura){
        con.update("INSERT INTO tbRegistro VALUES(NULL,?,?,?,1,1,3)",temperatura, formatter.format(dataAtual),
                false);

    }

    public void volumeTotal(Long volumeTotal){
        Double volumeTotalTratado = converter(volumeTotal);
        con.update("INSERT INTO tbMetrica VALUES(NULL,?,3,1)",volumeTotalTratado);
    }

    public void volumeEmUso(Long volumeDisponivel,Long volumeTotal){
        Double volumeEmUsoTratado = converter(volumeTotal) - converter(volumeDisponivel);
        con.update("INSERT INTO tbRegistro VALUES(NULL,?,?,?,1,3,4)",volumeEmUsoTratado,
                formatter.format(dataAtual),false);

    }

    public void processoPid(Integer pid){
        con.update("INSERT INTO tbProcessos VALUES(NULL,?,?,1)",pid,formatter.format(dataAtual));
    }

    public void quatidadeProcessos(Integer quatidadeProcessos){
        con.update("INSERT INTO tbRegistro VALUES(NULL,?,?,?,1,NULL,5)",quatidadeProcessos,
                formatter.format(dataAtual),false);
    }

   public Double converter(Long medida){
       Double converterMemoria = (double) medida / 1000000000;
       return (double) Math.floor(converterMemoria);
   }
}
