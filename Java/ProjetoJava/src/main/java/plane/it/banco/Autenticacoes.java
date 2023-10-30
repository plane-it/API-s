package plane.it.banco;

import plane.it.Menu;

import java.util.Scanner;

public class Autenticacoes {

    OperacoesBanco operacoesBanco = new OperacoesBanco();
    public String autenticarUsuario(Menu menu){
        Scanner leitorTexto = new Scanner(System.in);
        String resultadoAutenticacao = "";
        try {
            menu.menuBoasVindas();
            System.out.println("Informe seu email: ");
            String email = leitorTexto.nextLine();

            System.out.println("Informe sua senha: ");
            String senha = leitorTexto.nextLine();

            resultadoAutenticacao = operacoesBanco.autenticarUsuario(senha, email);

            if (resultadoAutenticacao == null) {

                System.out.println("\nSenha ou email incorretos, digite corretamente para realizar o login \n");
                autenticarUsuario(menu);
            }

            return resultadoAutenticacao;

        }catch (Exception e){
            System.out.println("Houve um erro, tente novamente");
            System.out.println("Erro: " + e);
            autenticarUsuario(menu);

        }

        return resultadoAutenticacao;
    }

    public int autenticarServidor(String fkAeroporto){
        Scanner leitorTexto = new Scanner(System.in);

        try {

            System.out.println("Informe o código de autenticação do servidor: ");
            String codigo = leitorTexto.nextLine();

            int resultadoAutenticacao = operacoesBanco.autenticarServidor(codigo, fkAeroporto);

            if (resultadoAutenticacao == 0) {

                System.out.println("\nCódigo de autenticação incorretos\n");
                autenticarServidor(fkAeroporto);

            }else {

                return resultadoAutenticacao;

            }

        }catch (Exception e){
            System.out.println("Houve um erro, tente novamente");
            System.out.println("Erro: " + e);
            autenticarServidor(fkAeroporto);
        }

        return 0;

    }

}
