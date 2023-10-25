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
                System.out.println(looca.getSistema().getSistemaOperacional());
                operacoesBanco.sistemaOperacional(looca.getSistema().getSistemaOperacional());

                break;

            case 2:
                System.out.println(looca.getMemoria());
                operacoesBanco.memoriaRamTotal(looca.getMemoria().getTotal());
                operacoesBanco.memoriaRamEmUso(looca.getMemoria().getEmUso(),looca.getMemoria().getTotal());

                break;

            case 3:

                System.out.println(looca.getProcessador().getNome());
                operacoesBanco.nomeProcessador(looca.getProcessador().getNome());

                System.out.println(looca.getProcessador().getFrequencia());
                operacoesBanco.frequenciaProcessador(looca.getProcessador().getFrequencia());

                System.out.println(looca.getProcessador().getUso());
                operacoesBanco.usoProcessador(looca.getProcessador().getUso());

                System.out.println(looca.getProcessador().getNumeroCpusFisicas());
                operacoesBanco.nucleosProcessador(looca.getProcessador().getNumeroCpusFisicas());

                System.out.println(looca.getProcessador().getNumeroCpusLogicas());
                operacoesBanco.nucleosProcessador(looca.getProcessador().getNumeroCpusLogicas());

                break;

            case 4:

                if (!Objects.equals(looca.getSistema().getSistemaOperacional(), "Windows")) {
                    System.out.println(looca.getTemperatura());
                    operacoesBanco.temperatura(looca.getTemperatura().getTemperatura());

                } else {
                    System.out.println("Com o sistema operacional Windows não é possível realizar essa captura");
                    operacoesBanco.temperatura(0.00);

                }

                break;

            case 5:

                System.out.println(looca.getGrupoDeDiscos().getTamanhoTotal());
                System.out.println("volume");
                for (Volume volume : volumes) {
                    System.out.println(volume.getNome());

                    System.out.println(volume.getTotal());
                    operacoesBanco.volumeTotal(volume.getTotal());

                    System.out.println(volume.getDisponivel());
                    operacoesBanco.volumeEmUso(volume.getDisponivel(),volume.getTotal());

                }

                break;

            case 6:

                System.out.println(processoGrupos.size());
                operacoesBanco.quatidadeProcessos(processoGrupos.size());

                for (Processo processo : processoGrupos){

                    System.out.println(processo.getPid());
                    operacoesBanco.processoPid(processo.getPid());

                    }

                break;

            case 7:
                //sistema
                System.out.println(looca.getSistema().getSistemaOperacional());
                operacoesBanco.sistemaOperacional(looca.getSistema().getSistemaOperacional());

                //memória
                System.out.println(looca.getMemoria());
                operacoesBanco.memoriaRamTotal(looca.getMemoria().getTotal());
                operacoesBanco.memoriaRamEmUso(looca.getMemoria().getEmUso(),looca.getMemoria().getTotal());

                //processador
                System.out.println(looca.getProcessador().getNome());
                operacoesBanco.nomeProcessador(looca.getProcessador().getNome());

                System.out.println(looca.getProcessador().getFrequencia());
                operacoesBanco.frequenciaProcessador(looca.getProcessador().getFrequencia());

                System.out.println(looca.getProcessador().getUso());
                operacoesBanco.usoProcessador(looca.getProcessador().getUso());

                System.out.println(looca.getProcessador().getNumeroCpusFisicas());
                operacoesBanco.nucleosProcessador(looca.getProcessador().getNumeroCpusFisicas());

                System.out.println(looca.getProcessador().getNumeroCpusLogicas());
                operacoesBanco.nucleosProcessador(looca.getProcessador().getNumeroCpusLogicas());

                //temperatura
                if (!Objects.equals(looca.getSistema().getSistemaOperacional(), "Windows")) {
                    System.out.println(looca.getTemperatura());
                    operacoesBanco.temperatura(looca.getTemperatura().getTemperatura());

                } else {
                    System.out.println("Com o sistema operacional Windows não é possível realizar essa captura");
                    operacoesBanco.temperatura(0.00);

                }


                //grupo de discos
                System.out.println(looca.getGrupoDeDiscos().getTamanhoTotal());
                System.out.println("volume");
                for (Volume volume : volumes) {
                    System.out.println(volume.getNome());

                    System.out.println(volume.getTotal());
                    operacoesBanco.volumeTotal(volume.getTotal());

                    System.out.println(volume.getDisponivel());
                    operacoesBanco.volumeEmUso(volume.getDisponivel(),volume.getTotal());
                }

                //processos
                System.out.println(processoGrupos.size());
                operacoesBanco.quatidadeProcessos(processoGrupos.size());

                for (Processo processo : processoGrupos){

                    System.out.println(processo.getPid());
                    operacoesBanco.processoPid(processo.getPid());

                }

                break;
            case 8:

                System.out.println("Opção 9 selecionada: Sair");
                break;
        }
    }
}
