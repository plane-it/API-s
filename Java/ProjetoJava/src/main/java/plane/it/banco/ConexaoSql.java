package plane.it.banco;

import org.apache.commons.dbcp2.BasicDataSource;
import org.springframework.jdbc.core.JdbcTemplate;

public class ConexaoSql {
    private JdbcTemplate conexaoDoBancoSql;
    public ConexaoSql() {
        BasicDataSource dataSource = new BasicDataSource();
        dataSource.setDriverClassName("com.microsoft.sqlserver.jdbc.SQLServerDriver");
        dataSource.setUrl("jdbc:sqlserver://44.218.73.236:1433;databaseName=planeit");
        dataSource.setUsername("planeit");
        dataSource.setPassword("planeit123");

        conexaoDoBancoSql = new JdbcTemplate(dataSource);
    }

    public JdbcTemplate getConexaoBanco() {
        return conexaoDoBancoSql;
    }
}
