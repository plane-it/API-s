package plane.it.banco;

import org.apache.commons.dbcp2.BasicDataSource;
import org.springframework.jdbc.core.JdbcTemplate;

public class ConexaoSql {
    private JdbcTemplate conexaoDoBancoSql;
    public ConexaoSql() {
        BasicDataSource dataSource = new BasicDataSource();
        dataSource.setDriverClassName("com.mysql.cj.jdbc.Driver");
        dataSource.setUrl("jdbc:sqlserver://SEU_IP:44.218.73.236;databaseName=planeit");
        dataSource.setUsername("root");
        dataSource.setPassword("urubu100");

        conexaoDoBancoSql = new JdbcTemplate(dataSource);
    }

    public JdbcTemplate getConexaoBanco() {
        return conexaoDoBancoSql;
    }
}
