# Código limpo [Livro]

## Regra dos escoteiros:

_"Deixa a área do acampamento mais limpa do que como você a encontrou"_

- Sempre que estiver mexendo no código e sentir que uma variável ou um método esta com o nome ruim, ou não deixa bem claro para que serve, altera-a, com muito cuidado para não quebrar é claro, mas manter sempre o código com bons nomes é sempre a melhor opção.

## Nomes que revelam o seu proposito:

Precisamos sempre usar bons nomes na hora de programar e sempre que puder melhorar eles para mantê-los atualizados.
Pra isso pensar em como cria-los é a melhor opção, pra isso precisamos pensar em:

- **POR QUE EXISTE?**
- **O QUE ELE FAZ?**
- **COMO É USADO?**

Nomes que não passam por essas perguntas não deixam claro para que servem e assim deixam mais difícil de entender a complexidade inteira.

> Por isso vou tentar escrever nomes que explicam melhor e tentar escrever antes em português e depois colocar no padrão do projeto (em inglês ou qualquer que seja a lingua)

Não use nome com palavras que tenham pouca destinção entre sí, Info e Data tem significados muito proximo Source e Destination já tem seus significados distintos e já te 'contam' o que esta acontecendo no código.

Criar palavras só porque a variavel se relaciona com outra de 'zork' e 'aZork' é horrivel

## Procure usar nomes passiveis de busca

Nomes que explicam e não são genéricos são mais faceis de serem buscados, por isso nomes maiores se sobressaem a nomes menores, um `iterador` é muito melhor do que `i`, temos muitos i's no projeto


## Nomes de Interfaces e Classes

Simplificar mas codificar, tente trabalhar com convenções como:

- Interface de Humano: IHumano
- Classe de Humano: CHumano