package plane.it;

import java.util.Scanner;

public class Menu {
    private Capturas capturas;
    private int servidor = 0;

    public void menuBoasVindas(){
        System.out.println("Seja Bem-vindo ao sistema de monitoramento de servidores Plane-it \n");

    }

    public void menuOpcoesSistema(int servidor) {
        Scanner leitor = new Scanner(System.in);
        this.servidor = servidor;
        try {
            System.out.println("""
                Menu do sistema:
                1 - Captura de dados da máquina
                2 - Sair """);

            int opcaoEscolhida = leitor.nextInt();

            if (opcaoEscolhida == 1) {
                System.out.println("Opção 1 selecionada: Captura de dados da máquina\n");
                menuCaptura();

            } else if (opcaoEscolhida == 2) {
                System.exit(0);

            } else {
                System.out.println("\nDigite um valor válido\n");
                menuOpcoesSistema(servidor);
            }

        }catch (Exception e){

            System.out.println("\nHouve um erro! Tente novamente");
            System.out.println("Erro: " + "\u001B[31m"  + e + "\u001B[0m" + "\n");
            menuOpcoesSistema(servidor);

        }
    }

    public void menuCaptura(){
        Scanner leitor = new Scanner(System.in);

        try {

            System.out.println("""
                    Captura de:
                    1 - Sistema
                    2 - Memoria
                    3 - Processador
                    4 - Temperatura
                    5 - Disco
                    6 - Processo
                    7 - Todos
                    8 -  Voltar ao menu inicial \n""");

            int opcao = leitor.nextInt();

            if (opcao < 1 || opcao > 8) {
                System.out.println("Digite uma opção válida para continuar \n");

            } else if (opcao == 8) {

                menuOpcoesSistema(servidor);

            } else {
                opcoesMenuCapitura(opcao);
                menuCaptura();
            }

        }catch (Exception e){

            System.out.println("\nHouve um erro! Tente novamente");
            System.out.println("Erro: " + e + "\n");
            menuCaptura();

        }
    }

    public void opcoesMenuCapitura(Integer opcao) {
        capturas = new Capturas(servidor);
        switch (opcao) {
            case 1 -> {       
                System.out.println("\n");
                capturas.sistemaOperacional();
                divisaoLinha();
            }
            case 2 -> {
                System.out.println("\n");
                capturas.memoria();
                divisaoLinha();
            }
            case 3 -> {
                System.out.println("\n");
                capturas.processador();
                divisaoLinha();
            }
            case 4 -> {
                System.out.println("\n");
                capturas.temperatura();
                divisaoLinha();
            }
            case 5 -> {
                System.out.println("\n");
                capturas.disco();
                divisaoLinha();
            }
            case 6 -> {
                System.out.println("\n");
                capturas.processos();
                divisaoLinha();
            }
            case 7 -> {
                //sistema

                System.out.println("+" + "-".repeat(30) + "+\n");
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
            }
            case 8 -> {
                System.out.println("Opção 9 selecionada: Sair");
                menuOpcoesSistema(servidor);
            }
        }
    }

    public void divisaoLinha(){
        System.out.println("-".repeat(45) + "\n");
    }

}
