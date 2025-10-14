# Configurações e soluções de problemas KDE

## KWIN + Latte Dock

A barra de Titulo dos programas, quando maximizados sumia, o problema é que o latte dock tem uma configuração para retirar esse comportamento por isso esse erro
Para resolver basta:

- Ir até `~/.config` | `cd /.config`
- Abrir com o vim o `lattedockrc` | `vim lattedockrc`
- Alterar a opção `UniversalSettings` para `false`
- Alterar a opção`BorderlessMaximizedWindows` para `true`
- Reinicie o sistema e reabra o latte-dock

