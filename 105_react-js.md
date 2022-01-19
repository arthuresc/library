# React Js

## Criando/Iniciando um projeto com react - create react app

Ele é um modulo de npm, basicamente 

- <ReactFragment> <ReactFragment/> serve para substituir o uso de tags excessivamente  (ou <> </>)

## Hooks

### useState
Tem como função setar o valor e metodos que são reativos, pra isso ele usa um hook que retorna uma função e um valor referente à aquele valor reativo

Seu uso mais comum é por destruturação já que quando se usa o setState/useState o retorno é um array com o valor e o método de alteração desse valor.

```javascript
  const App = () => {
    const ativoHook = React.useState('valorOriginal');
    const ativoValor = ativoHook[0]
    const setAtivoValor = ativoHook[1]
  }
```

é a mesma coisa que:

```javascript
  const App = () => {
    const [ativoValor, setAtivoValor] = React.useState('valorOriginal');
  }
```

Para essas alterações reativas a melhor maneira é por uma função de `callback` pois você tem como acessar o valor anterior pelos parametros

```javascript
  const App = () => {
    const [ativoValor, setAtivoValor] = React.useState('valorOriginal');
    handleAtivoValor() {
      setAtivoValor((anterior) => {
        !anterior
      })
    };
  };
```

### useRef 
Faz referência à tag dentro do `jsx` com o atributo `ref`
