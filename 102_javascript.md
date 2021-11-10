# Javascript

## Operator (Operadores)

### Double Exclamation ou Double Bang (hihi)

Não são considerados um operador já que são o uso do operador `!` duplamente, sendo que quando se usa somente `!` ele trata de tranformar um valor `falsey` ou `truthy` em `false` ou `true` e depois inverte o seu valor por se tratar de um `NOT` mas quando usado o `!!` ele acaba fazendo exatamente a mesma coisa porém invertendo o valor 2 vezes, logo, retornando ao valor original. Ele é o literalmente o uso de dois operadores `!`.

Ex de resultado `true`
```
function test(){
  return !!{nome: "Arthur"}
};
```

Ex de resultado `false`
```
function test(){
  return !!undefined
};
```

## Arrays

### .reduce

Ele resolve os elementos iterados de um array dando ao dev o iterado em questão e a soma (o resultado de cada callback do total já iterado) de todos os outros

Exemplo com `String`

```
var arrayDo = [ 'A', 'r', 't', 'h', 'u', 'r' ]

arrayDo.reduce((completo, letra) => `${completo}${letra}` )
'Arthur'
```

### inserir novo elemento no final

Há duas maneiras de fazer a mesma ação.

Exemplo 1:

```
array[array.length] = value
```

Exemplo 2:

```
array.push(value)
```

### inserir novo elemento no inicio

Uma maneira de criar um metodo para se ter esse resultado seria você iterar o array de tras pra frente e depois inserindo cada elemento num espaço anterior e assim ficando em aberto o espaço do primeiro elemento (elemento `0`)
Ou fazer uso do metodo `unshift`

Exemplo 1:

```
function insertFirstPosition(value){
  for(let i = array.length; i >= 0; i--){
    array[i] = array[i - 1];
  }
  array[0] = value;
}

insertFirstPosition(37);
```

Exemplo 2:

```
array.unshift(37);
```

## Funções

### Arrow functions =>

Elas tem a propria lexidade, logo os `this` dentro delas não referenciam ao mesmo de fora e sim à ela propria.
