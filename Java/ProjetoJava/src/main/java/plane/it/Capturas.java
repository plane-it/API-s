package plane.it;

import com.github.britooo.looca.api.core.Looca;
import com.github.britooo.looca.api.group.discos.Volume;
import com.github.britooo.looca.api.group.processos.Processo;
import plane.it.banco.OperacoesBanco;

import java.util.List;
import java.util.Objects;

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

        System.out.println("Nucles fisícos" + looca.getProcessador().getNumeroCpusFisicas());
        operacoesBanco.nucleosProcessador(looca.getProcessador().getNumeroCpusFisicas());

        System.out.println("Nucleos lógicos" + looca.getProcessador().getNumeroCpusLogicas());
        operacoesBanco.nucleosProcessador(looca.getProcessador().getNumeroCpusLogicas());

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

        for (Processo processo : processoGrupos){

            System.out.println("PID do processo:" + processo.getPid());
            operacoesBanco.processoPid(processo.getPid());

        }

    }
}
