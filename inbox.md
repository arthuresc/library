# Inbox

## Descrição:
Entende-se que Inbox é uma área ausente de uma organização para mutuo entendimento e é um espaço para Notas rápidas e etc.

## Notas:

- Arrumar depois gerenciador de conhecimento
- 

### Webpack Estudos:

- module bundler (ele serve para entregar um modulo da forma mais perfomatica)
- Ele 'empacota' todas as entradas/entries que são as dependencias do projeto
- utiliza de loaders para carregar os mais diversos tipos de arquivos
- O webpack é uma solução para a importação de dependencias já que os navegadores não entendem a importação
- Sem o webpack.config.js o webpack tem configurações default
  - Entry (entrada): é aonde fica a centralização do código do projeto, nele se encontra todos os imports e entradas de código, geralmente é um arquivo index.js
  - Output (saída): é a saída empacotada que o webpack gera apartir do projeto, ele fica na pasta configurada no webpack e por padrão é o main.js
- A ordem da importação de um `loader` do webpack importa
