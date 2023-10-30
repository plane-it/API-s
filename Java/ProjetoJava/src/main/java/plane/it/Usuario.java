package plane.it;

public class Usuario {
    private  String cpf;
    private String nome;
    private String email;

    private String fkAeroporto;


    public void setCpf(String cpf) {
        this.cpf = cpf;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public void setFkAeroporto(String fkAeroporto) {
        this.fkAeroporto = fkAeroporto;
    }

    public String getFkAeroporto() {
        return fkAeroporto;
    }

    @Override
    public String toString() {
        return "Usuario{" +
                "cpf='" + cpf + '\'' +
                ", nome='" + nome + '\'' +
                ", email='" + email + '\'' +
                ", fkAeroporto='" + fkAeroporto + '\'' +
                '}';
    }
}
