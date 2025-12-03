# Docker

### TROUBLESHOOTER

#### Erros de permissão mais comuns
https://phoenixnap.com/kb/cannot-connect-to-the-docker-daemon-error

#### Configurações

##### Entrada automatica no boot
Configure Docker to start on boot
Most current Linux distributions (RHEL, CentOS, Fedora, Debian, Ubuntu 16.04 and higher) use systemd to manage which services start when the system boots. On Debian and Ubuntu, the Docker service is configured to start on boot by default. To automatically start Docker and Containerd on boot for other distros, use the commands below:

 sudo systemctl enable docker.service
 sudo systemctl enable containerd.service
To disable this behavior, use disable instead.

 sudo systemctl disable docker.service
 sudo systemctl disable containerd.service

### Parametros

- `-d`: esta informando que o container precisa rodar em background (não ficar consumindo a tela inteira com os dados)
- `-p`: especifica a porta que o container vai utilizar e a porta que ele vai simular
  - a porta que esta antes dos `:` se refere a do nosso host e a após é a que utilizaremos para acessar ele
- 

## COMANDOS

### ps
Verifica os containers em execução no momento.

```bash
docker ps
```

### run
Cria um container.

```bash
docker run [...]
```


### pull
O comando `pull` baixa uma imagem para o seu computador.

```bash
docker pull tutum/mongodb
```

### info
Imprime na tela todas as informações da docker

```bash
docker info
```

### 



### 

## Teórico

Objetos

## Dúvidas
- Qual a diferença entre `docker ps` e `docker-compose ps` 