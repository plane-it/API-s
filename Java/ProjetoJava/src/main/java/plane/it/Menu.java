package plane.it;
;
import java.util.List;
import java.util.Objects;
import java.util.Scanner;
import com.github.britooo.looca.api.core.Looca;
import com.github.britooo.looca.api.group.discos.Volume;
import com.github.britooo.looca.api.group.processos.ProcessoGrupo;


public class Menu {

    Scanner leitor = new Scanner(System.in);
    com.github.britooo.looca.api.core.Looca looca = new Looca();

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
                    6 - Servico
                    7 - Processo
                    8 - Todos
                    9 -  Voltar ao menu inicial \n """);

            opcao = leitor.nextInt();

            if (opcao < 1 || opcao > 9){
                System.out.println("Digite uma opção válida para continuar \n");

            }else if (opcao == 9){

                break;

            } else{
                opcoesMenuCapitura(opcao);

            }
        }
    }

    public void opcoesMenuCapitura(Integer opcao) {
        List<ProcessoGrupo> processoGrupos = (List<ProcessoGrupo>) looca.getGrupoDeProcessos();
        List<Volume> volumes = looca.getGrupoDeDiscos().getVolumes();

        switch (opcao) {
            case 1:
                System.out.println(looca.getSistema().getSistemaOperacional());
                break;

            case 2:
                System.out.println(looca.getMemoria());
                break;

            case 3:

                System.out.println(looca.getProcessador().getNome());
                System.out.println(looca.getProcessador().getFrequencia());
                System.out.println(looca.getProcessador().getUso());
                System.out.println(looca.getProcessador().getNumeroCpusFisicas());
                System.out.println(looca.getProcessador().getNumeroCpusLogicas());
                break;

            case 4:
                if (!Objects.equals(looca.getSistema().getSistemaOperacional(), "Windows")) {
                    System.out.println(looca.getTemperatura());
                } else {
                    System.out.println("Com o sistema operacional Windows não é possível realizar essa captura");
                }

                break;

            case 5:

                System.out.println(looca.getGrupoDeDiscos().getTamanhoTotal());
                System.out.println("volume");
                for (Volume volume : volumes) {
                    System.out.println(volume.getNome());
                    System.out.println(volume.getTotal());
                    System.out.println(volume.getDisponivel());

                }

                break;

            case 6:
                for (ProcessoGrupo processo : processoGrupos) {
                    System.out.println(processo.getTotalProcessos());
                }

                break;

            case 7:
                //sistema
                System.out.println(looca.getSistema().getSistemaOperacional());

                //memória
                looca.getMemoria();
                //processador
                System.out.println(looca.getProcessador().getNome());
                System.out.println(looca.getProcessador().getFrequencia());
                System.out.println(looca.getProcessador().getUso());
                System.out.println(looca.getProcessador().getNumeroCpusFisicas());
                System.out.println(looca.getProcessador().getNumeroCpusLogicas());

                //temperatura
                looca.getTemperatura();

                //grupo de discos
                System.out.println(looca.getGrupoDeDiscos().getTamanhoTotal());
                System.out.println("volume");
                for (Volume volume : volumes) {
                    System.out.println(volume.getNome());
                    System.out.println(volume.getTotal());
                    System.out.println(volume.getDisponivel());

                }

                //processos
                for (ProcessoGrupo processo : processoGrupos) {
                    System.out.println(processo.getTotalProcessos());
                }

                break;
            case 9:

                System.out.println("Opção 9 selecionada: Sair");
                break;
        }
    }
}
