package plane.it;

public class Main {
    public static void main(String[] args) {

        Menu menu = new Menu();
        OperacoesBanco operacoesBanco = new OperacoesBanco();
        Usuario usuario = new Usuario();
        
        usuario.AutenticarUsuario(menu,operacoesBanco);

        while (true){

            menu.menuOpcoesSistema();
            menu.menuCaptura();

        }
    }
}