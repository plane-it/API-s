package plane.it;

import org.springframework.jdbc.core.BeanPropertyRowMapper;
import org.springframework.jdbc.core.JdbcTemplate;

import java.util.List;
import java.util.Scanner;

public class OperacoesBanco {

    Conexao conexao = new Conexao();
    JdbcTemplate con = conexao.getConexaoDoBanco();

    public Boolean autenticarUsuario(String senha, String email){

        List <Usuario> listaUsuario = con.query(
                "SELECT * FROM tbColaborador WHERE senha = ? AND email = ?",
                new BeanPropertyRowMapper <>(Usuario.class),
                senha,email);

        return !listaUsuario.isEmpty();

    }

}
