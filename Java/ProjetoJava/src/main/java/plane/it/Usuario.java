package plane.it;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

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

    public void AutenticarUsuario(Menu menus, OperacoesBanco operacoesBanco){
        Scanner leitorTexto = new Scanner(System.in);

        while (true) {
            menus.menuBoasVindas();
            System.out.println("Informe seu email: ");
            String email = leitorTexto.nextLine();

            System.out.println("Informe sua senha: ");
            String senha = leitorTexto.nextLine();

            if (!operacoesBanco.autenticarUsuario(senha, email)) {

                System.out.println("\nSenha ou email incorretos, digite corretamente para realizar o login \n");

            }else{
                break;
            }
        }
    }

    @Override
    public String toString() {
        return "Usuario{" +
                "cpf='" + cpf + '\'' +
                ", nome='" + nome + '\'' +
                ", email='" + email + '\'' +
                ", senha='" + senha + '\'' +
                '}';
    }
}
