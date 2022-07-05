# Javascript

## Coerção de tipo em contextos booleanos

### Truthy
Todos os valores que quando avaliados no contexto booleano ele se traduzem em `true`

Exemplos:

`if (true)`

`if ({})`

`if ([])`

`if (42)`

`if ("foo")`

`if (new Date())`

`if (-42)`

`if (3.14)`

`if (-3.14)`

`if (Infinity)`

`if (-Infinity)`

### Falsy
Todos os valores que quando avaliados no contexto booleano ele se traduzem em `false`


Exemplos:

`if (false)`

`if (null)`

`if (undefined)`

`if (0)`

`if (NaN)`

`if ('')`

`if (document.all) [1]`

***
## Operator (Operadores)

### && em operação ternária
É usado como operador comparativo mas se usado em uma ternaria com somente 1 comparação, o qe seria a segunda comparação se torna o retorno da ternaria

Exemplo em que o retorno será a string:
```js
total > 10000 && 'Você esta gastando muito';
```

### delete
É um operador para exclusão de elementos, inclusive elementos dentro de objetos ou arrays, mas não recomendado o uso pois ele classifica o espaço posteriormente como `undefined`, nesse caso (em objetos ou arrays) o melhor são as funções já existentes.

```js
delete number[2]
```

### Double Exclamation ou Double Bang (hihi)

Não são considerados um operador já que são o uso do operador `!` duplamente, sendo que quando se usa somente `!` ele trata de tranformar um valor `falsey` ou `truthy` em `false` ou `true` e depois inverte o seu valor por se tratar de um `NOT` mas quando usado o `!!` ele acaba fazendo exatamente a mesma coisa porém invertendo o valor 2 vezes, logo, retornando ao valor original. Ele é o literalmente o uso de dois operadores `!`.

Ex de resultado `true`
```js
function test(){
  return !!{nome: "Arthur"}
};
```

Ex de resultado `false`
```js
function test(){
  return !!undefined
};
```

### Double pipe (||)

São usados para dar a condição a opção de OU (OR) mas se usado de maneira ternaria pode representar a possibilidade condicional de retorno de um valor sendo um deles `truthy`

```js
const items = item || selectedItems,
```

***
## Arrays

### Destructuring (desestruturar)

É fazer as referencias à indices do array de maneira mais rapida mas visualmente invertida

Por que:

```js
const calcularPerimetro = [4, 
  function (lado) {
    return 4 * lado
  },
];

/*aonde se inicia o destructuring*/
const [ lados, perimetro ] = calcularPerimetro

/* nesse momento existe uma 'variavel' lados e outra perimetro que se referem aos indices do array calcularPerimetro */
```
### .splice

A função retira ou insere elementos dentro de um array independente da ordem pois ele possui controle do local de inicio de entrada ou saida.

Exemplo de uso:

number.splice(5, 0, 6, 7, 2);

| array 	| função 	| arg1 	| arg2 	| arg3 	| arg4 	| arg5 	|
|:-----:	|:------:	|:----:	|:----:	|:----:	|:----:	|:----:	|
| number 	| .splice |   5  	|   0  	|  6   	|   7  	|   2  	|

arg1: A posição a partir que será realizadas as tarefas da função (inserir ou excluir elementos do array)
arg2: A quantidade de elementos à serem excluídos a partir da posição referenciada no arg1
arg3...5: Os elementos novos que serão inseridos a partir da posição referenciada no arg1


### .reduce

Ele resolve os elementos iterados de um array dando ao dev o iterado em questão e a soma (o resultado de cada callback do total já iterado) de todos os outros

Exemplo com `String`

```js
var arrayDo = [ 'A', 'r', 't', 'h', 'u', 'r' ]

arrayDo.reduce((completo, letra) => `${completo}${letra}` )
'Arthur'
```

### inserir novo elemento no final

Há duas maneiras de fazer a mesma ação.

Exemplo 1:

```js
array[array.length] = value
```

Exemplo 2:

```js
array.push(value)
```

### inserir novo elemento no inicio

Uma maneira de criar um metodo para se ter esse resultado seria você iterar o array de tras pra frente e depois inserindo cada elemento num espaço anterior e assim ficando em aberto o espaço do primeiro elemento (elemento `0`)
Ou fazer uso do metodo `unshift`

Exemplo 1:

```js
function insertFirstPosition(value){
  for(let i = array.length; i >= 0; i--){
    array[i] = array[i - 1];
  }
  array[0] = value;
}

insertFirstPosition(37);
```

Exemplo 2:

```js
array.unshift(37);
```

***
## Funções

### Arrow functions =>

Elas tem a propria lexidade, logo os `this` dentro delas não referenciam ao mesmo de fora e sim à ela propria.



// MONTAR ARQUIVO DE REGEX E CRUZAR AS INFOS
https://appdividend.com/2020/08/01/javascript-remove-character-from-string-example/
    const regex = new RegExp(`^${rule}$`);
Só lembrar de quando montar esse arquivo sobre regexp falar aqui sobre as diferenças da saida de um new RegExp e só usar a regex dentro de uma função

***
## PADRÕES JAVASCRIPT

Objetos


## SOLUÇÕES

### SOLUÇÃO AO SWITCH...CASE
```js
    badgeProcessoStatusCreator(value) {
      return (
        {
          F: {
            message: 'Aberto',
            style: 'badge-info',
          },
          T: {
            message: 'Fechado',
            style: 'badge-success',
          },
          C: {
            message: 'Cancelado',
            style: 'badge-warning',
          },
        }[value.status] || {
          message: '-',
          style: 'badge-secondary',
        }
      );
    },

    //Como ele retorna um objeto, posso usar o metodo já presumindo ele sendo um objeto
    badgeProcessoStatusCreator(valorPassado)['message']
```


regex + js 

camel case e outros cases

***adquirir conhecimento em regex***
``` js
function camelCase(word) {
    return word.replace(
        /(^|\s+)(\S)(\S*)/g,
        function (match, space, firstLetter, rest) {
            return space + firstLetter.toUpperCase() + rest.toLowerCase();
        }
    )
}

```


array find

https://developer.mozilla.org/pt-BR/docs/Web/JavaScript/Reference/Global_Objects/Array/find

Object assign

```js
const dataObj = { data1: 'Hello world', name: 'Arthur Escalera' }

const dataOriginal = { data1: 'Hello world1' }

Object.assign(dataObj, dataOriginal);
{data1: 'Hello world1', name: 'Arthur Escalera'}
```

array.from()

Muito bom, ele tem um map nele

```js
// Array-like object (arguments) para um Array
function f() {
  return Array.from(arguments);
}

f(1, 2, 3);
// [1, 2, 3]


// Qualquer iterable object ...
// com Set
var s = new Set(["foo", window]);
Array.from(s);
// ["foo", window]


// Map
var m = new Map([[1, 2], [2, 4], [4, 8]]);
Array.from(m);
// [[1, 2], [2, 4], [4, 8]]


// String
Array.from("foo");
// ["f", "o", "o"]


// Usando um arrow function como função map para
// manipular os elementos
Array.from([1, 2, 3], x => x + x);
// [2, 4, 6]


// Gerando uma sequência de números
Array.from({length: 5}, (v, k) => k);
// [0, 1, 2, 3, 4]


const arr1 = []
undefined
arr1.from({length: 5}, (v, k) => k)
VM4035:1 Uncaught TypeError: arr1.from is not a function
    at <anonymous>:1:6
(anonymous) @ VM4035:1
const arr1 = Array.from({length: 5}, (v, k) => k)
undefined
arr1
(5) [0, 1, 2, 3, 4]


reduce
function solution(number){
  const index = number >= 0 ? number : 0;
  const arr = Array.from({length: index}, (v, k) => k)
  const result = arr.reduce((total, item) => {
    if(item%3 === 0 || item%5 === 0){
     return total + item
    }else{
      return total + 0
    }
  }, 0)
  return result;
}
```

Como criar um objeto multilevel, com aninhamento de outros objetos com base de 1 array

```js
const arrayMenus = ['especiais', 'ge', 'jabuticaba'];
const arrayMenus2 = ['contas-pagar', 'solicitacao'];
const menus = {}


function trabalho(array){
  array.reduce((total, menu, index, array) =>  {
    let length = array.length - 1
    console.log(menu, index , length, index === length)
    if (index === 0)
      return total[menu] = { children: {} };
    if (index > 0 && index !== length){
      return total.children[menu] = { children: {} };
    }
    return total.children[menu] = {};
  }, menus)
}

trabalho(arrayMenus)
trabalho(arrayMenus2)


console.log(menus)
```
fonte: https://stackoverflow.com/questions/22562754/create-a-dynamic-nested-object-from-array-of-properties

quando for somente iterar sob o array usar o forEach se for precisar alterar valor a valor do array e vai retornar esse valores novos num array novo numa variavel nova usar o map