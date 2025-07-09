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

### classe Date: 