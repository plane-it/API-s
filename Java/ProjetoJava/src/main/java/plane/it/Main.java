package plane.it;

import com.github.britooo.looca.api.core.Looca;
import com.github.britooo.looca.api.group.discos.Disco;
import com.github.britooo.looca.api.group.discos.DiscoGrupo;
import com.github.britooo.looca.api.group.discos.Volume;
import com.github.britooo.looca.api.group.processos.Processo;
import com.github.britooo.looca.api.group.processos.ProcessoGrupo;
import com.github.britooo.looca.api.group.rede.Rede;
import com.github.britooo.looca.api.group.rede.RedeInterface;
import org.springframework.jdbc.core.JdbcTemplate;

import javax.swing.*;
import java.util.ArrayList;
import java.util.List;
import java.util.Objects;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Conexao conexao = new Conexao();
        JdbcTemplate con = conexao.getConexaoDoBanco();

        Scanner leitorTexto = new Scanner(System.in);

        Boolean sairMenu = false;



        System.out.println("""
                    Seja Bem-vindo ao sistema de monitoramento de servidores Plane-it
                    Informe o seu email:
                    """);
        String email = leitorTexto.nextLine();

        System.out.println("Informe sua senha:");
        String senha = leitorTexto.nextLine();

        if (Empresa.autenticarUsuario(email, senha)){
            do {
                System.out.println("""
                        Menu do sistema:
                        1 - Captura de dados da máquina
                        2 - Sair
                        """);

                int opcao = leitorTexto.nextInt();

                switch (opcao) {

                    case 1:

                        Looca looca = new Looca();

                        System.out.println("Opção 2 selecionada: Captura de dados da máquina");

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
                        
                        9 -  Voltar ao menu inicial
                        """);

                        int opcaoSist = leitorTexto.nextInt();
                        List<ProcessoGrupo> processoGrupos = (List<ProcessoGrupo>) looca.getGrupoDeProcessos();

                        List<Volume> volumes = looca.getGrupoDeDiscos().getVolumes();

                        switch (opcaoSist){
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
                                if (!Objects.equals(looca.getSistema().getSistemaOperacional(), "Windows")){
                                    System.out.println(looca.getTemperatura());
                                } else {
                                    System.out.println("Com o sistema operacional Windows não é possível realizar essa captura");
                                }

                                break;

                            case 5:

                                System.out.println(looca.getGrupoDeDiscos().getTamanhoTotal());
                                System.out.println("volume");
                                for(Volume volume :volumes){
                                    System.out.println(volume.getNome());
                                    System.out.println(volume.getTotal());
                                    System.out.println(volume.getDisponivel());

                                }

                                break;

                            case 6:
                                for (ProcessoGrupo processo : processoGrupos){
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
                                for(Volume volume :volumes){
                                    System.out.println(volume.getNome());
                                    System.out.println(volume.getTotal());
                                    System.out.println(volume.getDisponivel());

                                }

                                //processos
                                for (ProcessoGrupo processo : processoGrupos){
                                    System.out.println(processo.getTotalProcessos());
                                }

                                break;
                            case 9:

                                System.out.println("Opção 9 selecionada: Sair");
                                break;
                        }


                        break;
                    case 3:
                        sairMenu = true;
                        System.out.println("Opção 3 selecionada: Sair");
                        break;
                    default:
                        System.out.println("Opção inválida. Tente novamente.");
                        break;
                }
            } while (!sairMenu);
        } else {
            System.out.println("Erro na autentificação");
        }


    }
}