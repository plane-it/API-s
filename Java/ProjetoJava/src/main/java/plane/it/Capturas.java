package plane.it;

import com.github.britooo.looca.api.core.Looca;
import com.github.britooo.looca.api.group.discos.Volume;
import com.github.britooo.looca.api.group.processos.Processo;
import plane.it.banco.OperacoesBanco;
import plane.it.banco.tabelas.Componente;

import java.util.ArrayList;
import java.util.List;
import java.util.Objects;

import static java.lang.Math.pow;

public class Capturas {
    private Looca looca = new Looca();
    private OperacoesBanco operacoesBanco;
    private List <Processo> processoGrupos = looca.getGrupoDeProcessos().getProcessos();
    private List<Volume> volumes = looca.getGrupoDeDiscos().getVolumes();


    public Capturas(int servidor) {
        this.operacoesBanco =  new OperacoesBanco(servidor);
    }

    public void sistemaOperacional(){

        System.out.println("Sistema Oepracional: " + looca.getSistema().getSistemaOperacional());
        operacoesBanco.sistemaOperacional(looca.getSistema().getSistemaOperacional());

    }

    public void memoria(){
        System.out.println(looca.getMemoria());
        operacoesBanco.memoriaRamTotal(looca.getMemoria().getTotal());
        operacoesBanco.memoriaRamEmUso(looca.getMemoria().getEmUso(),looca.getMemoria().getTotal());
    }


    public void processador(){
        System.out.println("Processador:");
        System.out.println("Modelo:" + looca.getProcessador().getNome());
        operacoesBanco.nomeProcessador(looca.getProcessador().getNome());

        System.out.println("Frequência:" + looca.getProcessador().getFrequencia());
        operacoesBanco.frequenciaProcessador(looca.getProcessador().getFrequencia());

        System.out.println("Em uso: "+ looca.getProcessador().getUso() + "%");
        operacoesBanco.usoProcessador(looca.getProcessador().getUso());


    }

    public void temperatura(){

        System.out.println("Temperatura:");
        if (!Objects.equals(looca.getSistema().getSistemaOperacional(), "Windows")) {
            System.out.println(looca.getTemperatura());
            operacoesBanco.temperatura(looca.getTemperatura().getTemperatura());

        } else {
            System.out.println("Com o sistema operacional Windows não é possível realizar essa captura");
            operacoesBanco.temperatura(0.00);

        }
    }

    public void disco(){

        System.out.println("Disco: ");
        System.out.println("Tamanho total de todos os discos: " + looca.getGrupoDeDiscos().getTamanhoTotal());
        for (Volume volume : volumes) {
            System.out.println("Nome do disco: " + volume.getNome());

            System.out.println("Tamanho total:" +  volume.getTotal());
            operacoesBanco.volumeTotal(volume.getTotal());

            System.out.println("Disponível: " + volume.getDisponivel());
            operacoesBanco.volumeEmUso(volume.getDisponivel(),volume.getTotal());

        }
    }

    public void processos(){
        System.out.println("Processos:");
        System.out.println("Quantidade de processos:" + processoGrupos.size());
        operacoesBanco.quatidadeProcessos(processoGrupos.size());
    }

    public void specs(Integer idServidor){
        List<Componente> componentes = operacoesBanco.buscarComponentes(idServidor);
        List<Integer> idComponentes = new ArrayList<>();

        String idCPU = null;
        String idRAM = null;
        String idDisco = null;

        for (Componente componente : componentes) {
            if (componente.getFktipoComponente().equals("1")) {
                idCPU = componente.getIdComp();
            } else if (componente.getFktipoComponente().equals("2")) {
                idRAM = componente.getIdComp();
            } else if (componente.getFktipoComponente().equals("3")) {
                idDisco = componente.getIdComp();
            }
        }

        long ram = looca.getMemoria().getTotal();
        Double ramGb = ram / pow(1024, 3);

        long disco = looca.getGrupoDeDiscos().getTamanhoTotal();
        Double discoGb = disco / pow(1024, 3);

        long hertz = looca.getProcessador().getFrequencia();
        Double cpuMhz = hertz / pow(10, 6);

        System.out.println(String.format("""
                        +--------------------------------+
                        | Ram: %.2f GB                  |
                        | Disco: %.2f GB               |
                        | CPU: %.2f MHz               | 
                        +--------------------------------+
                        | Inserindo no banco de dados... |
                        +--------------------------------+
                        """, ramGb, discoGb, cpuMhz));

        if (operacoesBanco.cadastrarSpcecs(cpuMhz, idCPU, 4)) {
            System.out.println("Especificações de CPU cadastradas com sucesso!");
        } else {
            System.out.println("Especificações de CPU já cadastradas!");
        }
        if (operacoesBanco.cadastrarSpcecs(ramGb, idRAM, 3)) {
            System.out.println("Especificações de RAM cadastradas com sucesso!");
        } else {
            System.out.println("Especificações de RAM já cadastradas!");
        }
        if (operacoesBanco.cadastrarSpcecs(discoGb, idDisco, 3)) {
            System.out.println("Especificações de Disco cadastradas com sucesso!");
        } else {
            System.out.println("Especificações de Disco já cadastradas!");
        }

        System.out.println("\n");
    }
}
