package plane.it;

import java.util.List;
import java.util.Objects;
import java.util.Scanner;
import com.github.britooo.looca.api.core.Looca;
import com.github.britooo.looca.api.group.discos.Volume;
import com.github.britooo.looca.api.group.processos.Processo;

public class Menu {

    Scanner leitor = new Scanner(System.in);
    com.github.britooo.looca.api.core.Looca looca = new Looca();
    OperacoesBanco operacoesBanco = new OperacoesBanco();
    List <Processo> processoGrupos = looca.getGrupoDeProcessos().getProcessos();
    Capturas capturas = new Capturas();

    public void menuBoasVindas(){

       System.out.println("Seja Bem-vindo ao sistema de monitoramento de servidores Plane-it ");

    }

    public void menuOpcoesSistema() {

        while (true) {

            System.out.println("""
                Menu do sistema:
                1 - Captura de dados da máquina
                2 - Sair """);

            Integer opcaoEscolhida = leitor.nextInt();

            if (opcaoEscolhida == 1){
              break;

            } else if (opcaoEscolhida == 2) {
                System.exit(0);

            }else{
                System.out.println("Digite um valor válido");

            }

        }
    }

    public void menuCaptura(){
        Integer opcao = 0;
        System.out.println("Opção 2 selecionada: Captura de dados da máquina\n");

        while (true) {
            System.out.println("""
                    Captura de:
                    1 - Sistema
                    2 - Memoria
                    3 - Processador
                    4 - Temperatura
                    5 - Disco
                    6 - Processo
                    7 - Todos
                    8 -  Voltar ao menu inicial \n """);

            opcao = leitor.nextInt();

            if (opcao < 1 || opcao > 8){
                System.out.println("Digite uma opção válida para continuar \n");

            }else if (opcao == 8){

                break;

            } else{
                opcoesMenuCapitura(opcao);

            }
        }
    }

    public void opcoesMenuCapitura(Integer opcao) {

        List<Volume> volumes = looca.getGrupoDeDiscos().getVolumes();

        switch (opcao) {
            case 1:
                System.out.println("\n");
                capturas.sistemaOperacional();
                divisaoLinha();
                break;

            case 2:
                System.out.println("\n");
                capturas.memoria();
                divisaoLinha();
                break;

            case 3:
                System.out.println("\n");
                capturas.processador();
                divisaoLinha();
                break;

            case 4:
                System.out.println("\n");
                capturas.temperatura();
                divisaoLinha();
                break;

            case 5:
                System.out.println("\n");
                capturas.disco();
                divisaoLinha();
                break;

            case 6:
                System.out.println("\n");
                capturas.processos();
                divisaoLinha();
                break;

            case 7:
                //sistema

                System.out.println("+" + "-".repeat(30) + "+\n" );
                capturas.sistemaOperacional();
                divisaoLinha();

                //memória
                capturas.memoria();
                divisaoLinha();

                //processador
                capturas.processador();

                //temperatura
                capturas.temperatura();
                System.out.println("\n");
                divisaoLinha();


                //grupo de discos
                capturas.disco();
                System.out.println("\n");
                divisaoLinha();


                //processos
                capturas.processos();
                System.out.println("\n");
                divisaoLinha();
                break;
            case 8:

                System.out.println("Opção 9 selecionada: Sair");
                break;
        }
    }

    public void divisaoLinha(){
        System.out.println("-".repeat(45) + "\n");
    }
}
