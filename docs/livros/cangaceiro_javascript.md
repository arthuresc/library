# Cangaceiro Javascript

## Atualizações

### Problema: Deixar propriedades de classe __private__
- No livro é repassado para deixar a propriedade de certa classe privada você coloca ela com underline (_) na frente, pois até o momento do livro não se tinha como fazer isso nativamente. Mas hoje com a sintaxe ```#``` (usa-se: ```#propriedadeDeClasseX = valorDePropriedade```) 

### Conhecimento: Arquivo de inicialização do projeto
- No livro me é passado a convenção que é necessário criar um arquivo de inicialização do projeto
- A criação do `app.js` é feita e é dito que por convenção, por `app.js` não possuir classe declarada ele não tem a primeira letra em maiúscula (Paskal Case)
-  

### Por que precisamos usar o `.bind` em `document.querySelector` para funcionar o alias?
- Internamente ao `querySelector` ele faz referência ao `document`
- Por isso, ao usarmos o método `.bind` em uma variável que perde o contexto (no caso aqui o `document`, mas mais usualmente pode ser o `this`)
- Assim ele devolve o contexto 
  - De qual maneira, não sei, não sei se é referenciando ou criando uma cópia literal do que foi perdido o contexto
- Quando passo um método para outro contexto (seja dentro de uma função, seja passando como callback para alguma função do JavaScript), ele pode perder sua referência original, ou seja, o this pode deixar de apontar para o objeto onde o método foi criado. Para resolver isso, existem duas soluções principais:
  - Você pode criar uma função (por exemplo, uma arrow function) no local onde tem acesso ao objeto original, garantindo que o método seja chamado com o contexto correto. Assim, o código "volta" para o objeto certo para executar o método.
  - Ou, não importa para onde o método seja levado, você pode fixar o contexto dele usando .bind(), garantindo que o this dentro do método sempre aponte para o objeto desejado, independentemente de onde ele for chamado.
>"O `document.querySelector()` é uma função que pertence ao objeto `document`, chamaremos tal função de método. Internamente, o `querySelector` tem uma chamada para o `this`, que é o contexto no qual o método é chamado, no caso `document`."
[livro Cangaceiro Javascript, 2016]

### static, mas porque?:
- É usado para definir métodos ou variaveis de uma classe que não usa instancias (propriedades, que só são criadas quando há a instanciação da classe) da classe
- Em resumo, se a classe possui propriedades que precisam serem passadas quando se *instancía* ela o static não tem o porque de existir já que usar ele é se esperar você não precisar instanciar a classe no seu código e por isso não acabar colocar valor nas propriedades da classe com o constructor.

### Proxy, uma solução para cascatear:
- Ele cria uma 'cópia' do objeto passado como primeiro parametro e usa das funções `get`, `set` e `apply` internas para você conseguir cascatear logicas para o uso de maneira simples mas com uma lógica aplicada, por exemplo settar um dado de uma propriedade ser (o `apply` ainda não sei ao certo como usar, preciso especificar antes de passar para o [[101_javascript]])

### Padrão: __Error-First-Callback__
- É um padrão muito usado em código assincrono, primeiro executa as verificações de erro possiveis para depois executar o código.

### Aninhando `Promises`(com o `.then()`): retorne a proxima Promise no `.then()` atual.
- A ideia é que seria necessário aninhar as Promises pois os dados que voltam delas compõem o mesmo `array`.
- E pra isso é só retornar o método que você precisa buscar logo em seguida do primeiro que você já fez a busca. (p.280)
- Pratica "saudável" pois consegue evitar você criar um série de resoluções de Promises para buscar todos os valores e cascateia tudo nos `.then()`
- Cascateamento é melhor do que Aninhamento

### Testando igualdade em 2 objetos
- Uma estratégia bem usada se quiser testar se os 2 objetos inteiros são iguais é colocar cada um em string de json `JSON.stringfy(objeto)` e então comparar as duas strings resultantes
- strings, numbers e outros tipos _**literais**_ podem ser comparados, mas objetos eles serão sempre diferentes mesmo quando identicos.
- 
