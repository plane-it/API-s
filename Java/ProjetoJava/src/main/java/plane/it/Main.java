package plane.it;

import plane.it.banco.Autenticacoes;

public class
Main {
    public static void main(String[] args) {

        Menu menu = new Menu();
        Autenticacoes autenticacoes = new Autenticacoes();

        String aeroporto = autenticacoes.autenticarUsuario(menu);
        int servidor = autenticacoes.autenticarServidor(aeroporto);

        while (true){

            menu.menuOpcoesSistema(servidor);


        }
    }
}