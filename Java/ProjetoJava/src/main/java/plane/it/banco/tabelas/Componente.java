package plane.it.banco.tabelas;

public class Componente {
    private String idComp;
    private String nome;
    private String fktipoComponente;
    private String preco;
    private String fkServ;

    public Componente() {

    }

    public Componente(String idComp, String nome, String fktipoComponente, String preco, String fkServ) {
        this.idComp = idComp;
        this.nome = nome;
        this.fktipoComponente = fktipoComponente;
        this.preco = preco;
        this.fkServ = fkServ;
    }

    public String getIdComp() {
        return idComp;
    }

    public void setIdComp(String idComp) {
        this.idComp = idComp;
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public String getFktipoComponente() {
        return fktipoComponente;
    }

    public void setFktipoComponente(String fktipoComponente) {
        this.fktipoComponente = fktipoComponente;
    }

    public String getPreco() {
        return preco;
    }

    public void setPreco(String preco) {
        this.preco = preco;
    }

    public String getFkServ() {
        return fkServ;
    }

    public void setFkServ(String fkServ) {
        this.fkServ = fkServ;
    }

    @Override
    public String toString() {
        return "Componente{" +
                "idComp=" + idComp +
                ", nome='" + nome + '\'' +
                ", fktipoComponente=" + fktipoComponente +
                ", preco=" + preco +
                ", fkServ=" + fkServ +
                '}';
    }
}
