# Configurações e Solução de Problemas:
Configuração da maquina Linux para uso pessoal/trabalho.
Troubleshooter de problemas que já tive antes.
Categorizados pela tecnologia usada.


## TROUBLESHOOTER

### openSuse - Erro de pptp vpn
Infelizmente ele não cria automaticamente e nem consegue usar os serviços que já possui para configurar a vpn (imagino que seja exclusivo da vpn pptp) no firewall do sistema

```bash
firewall-cmd --permanent --new-service=pptp

cat >/etc/firewalld/services/pptp.xml<<EOF
<?xml version="1.0" encoding="utf-8"?>
<service>
  <port protocol="tcp" port="1723"/>
</service>
EOF

firewall-cmd --permanent --zone=public --add-service=pptp
firewall-cmd --permanent --zone=public --add-masquerade
firewall-cmd --permanent --zone=public --add-protocol=gre
firewall-cmd --reload
```
ameatum1352
fonte: https://serverfault.com/questions/837770/pptp-passthrough-centos-7-firewalld-router-to-windows-server

### Instalando o vscode no KDE (fora de um sistema que é ou já teve Gnome)


### Deletado o grub (perdeu o grub)
Será necessário fazer uso de um pendrive com `ubuntu live`
## SNAP (repositório)

### Icone não aparece
Erro dos icones de softwares/apps não aparecendo no menu do sistema
No caso de aplicativos que forem baixados pelo repositório `snap` e não apresentam os icones ou não aparecem no menu do SO, siga:

Copie o arquivo com a extensão `.desktop` para a pasta do sistema correta:

	cp -R /snap/blender/current/yourSoftware.desktop /usr/share/applications 

***
## ZSH (terminal emulator)

### Configurando ZSH como shell principal do Sistema
Metodos diferentes para configurar o ZSH como o terminal principal do sistema.

Default:

	chsh -s $(which zsh)
	
Caso permaneça o erro:

Abra `/etc/passwd`

	sudo vim /etc/passwd

Procure pela linha contento o usuário do sistema:

	arthuresc:x:1634231:100:Arthur Escalera:/home/arthuresc:/bin/bash

e altere `bash` por `zsh`

	arthuresc:x:1634231:100:Arthur Escalera:/home/arthuresc:/bin/zsh

Reinicie o sistema.


## Droidcam
### Instalando
### Configurando 

https://askubuntu.com/questions/1235389/droidcam-unable-to-find-dev-video0

### Configurações padrão do powerline 10k
[Arquivo](needs/.p10kzsh)

https://stackoverflow.com/questions/61667666/keep-git-branch-name-untruncated-in-shell-using-p10k-oh-my-zsh-theme


### Configurando editor de texto padrão do sistema (Ubuntu & Debian based)

`sudo update-alternatives --config editor`