package plane.it;

import java.util.ArrayList;
import java.util.List;

public class Usuario {

    private  String cpf;
    private String nome;
    private  String email;
    private String senha;





    public Usuario() {
    }

    public Usuario(String cpf, String nome, String email, String senha) {
        this.cpf = cpf;
        this.nome = nome;
        this.email = email;
        this.senha = senha;

    }

    public Boolean autenticaCPF(String cpf, String email){
        Boolean autenticado = false;
        if (!cpf.equals(getCpf()) && !email.equals(getEmail())){
            autenticado = true;
        } else {
            autenticado = false;
        }
        return autenticado;
    }


    public String getCpf() {
        return cpf;
    }

    public void setCpf(String cpf) {
        this.cpf = cpf;
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public String getSenha() {
        return senha;
    }

    public void setSenha(String senha) {
        this.senha = senha;
    }
}
