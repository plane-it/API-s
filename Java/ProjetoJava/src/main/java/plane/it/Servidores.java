package plane.it;

public class Servidores {
    private int idServ;
    private String apelido;

    public void setIdServ(int idServ) {
        this.idServ = idServ;
    }

    public void setIdServ(String idServidor) {
        this.idServ = idServ;
    }

    public void setApelido(String apelido) {
        this.apelido = apelido;
    }

    public int getIdServidor() {
        return idServ;
    }

    @Override
    public String toString() {
        return "Servidores{" +
                "idServidor='" + idServ + '\'' +
                ", apelido='" + apelido + '\'' +
                '}';
    }
}
