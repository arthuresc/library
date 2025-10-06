# UX / UI

## Design System - Organizando o "design" do seu projeto
  Criar projetos para web ou embarcados necessita de um bom design para que o seu usuário consiga ter uma boa experiência, acontece que criar esses projetos precisa a cada dia cada vez mais agilidade e qualidade, mas para isso foi criada a maneira de organizar e abstrair os elementos gráficos de um projeto com a ferramenta de design chamada de Design System.

  O foco é organizar e abstrair para facilitar a criação padronizada dentro de um projeto. Mas no Design System temos também alguns padrões de organização e o mais escolhido é o Atomic Design, excelente, muito replicado, por isso facil de encontrar material na internet, e sua abstração é simples.

  A sua separação é por:
    - Atomos:
      - Tipografia: As fontes e cada mudança de tamanho dela dentro do projeto, se houver mais de 1 separar BEM separado
      - Cores: TODAS AS CORES que são aplicadas no seu projeto, inclusive de terceiros e as do seu logo
      - Espaçamentos: Seja internos de caixas, entre um texto e uma imagem, altura de linha, tudo que for relevante no seu projeto precisa estar aqui pois trará mais predibilidade ao construir o código do projeto. Nomear os tamanhos caso use frameworks de terceiros (converse com o seu time de frontend) é bem interessante para agilizar. Se preciso e possivel documentar o arredondamento de bordas aqui.
      - Logo: O seu logo e suas possiveis aplicações no projeto, não precisa ser documentado alem disso.
      - Icones: Os icones usados no seu projeto, fica até mais facil identificar caso algum deles saia muito do padrão imaginado/estipulado. Não esqueça de aplicar todos os icones em um tamanho padrão mas documente os possiveis tamanhos que podem ser usados no projeto. Caso seu projeto faça uso de diferentes cursores aqui também pode ser documentado eles.
      - Sombras: As sombras padrão do projeto, não faça MUITOS exemplos, deixe sucinto para as situações corretas.
      - 