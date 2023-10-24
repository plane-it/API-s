package plane.it;

import com.github.britooo.looca.api.core.Looca;

public class Main {
    public static void main(String[] args) {

        Menu menu = new Menu();
        OperacoesBanco operacoesBanco = new OperacoesBanco();
        Usuario usuario = new Usuario();


        Boolean sairMenu = false;

        // FIM DA INICIALIZAÇÃO

        usuario.AutenticarUsuario(menu,operacoesBanco);

        do{

            menu.menuOpcoesSistema();
            menu.menuCaptura();

        }while(!sairMenu);

    }
}