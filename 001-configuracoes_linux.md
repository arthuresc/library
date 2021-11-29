# Configurações e Solução de Problemas:
Configuração da maquina Linux para uso pessoal/trabalho.
Troubleshooter de problemas que já tive antes.
Categorizados pela tecnologia usada.

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

