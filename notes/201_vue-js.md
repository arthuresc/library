---
title: "Vue.js"
type: evergreen
tags: [evergreen, area/stack]
status: ativo
---
# Vue.js

## TROUBLESHOOTER

### kee-alive

#### quando se torna necessário fazer a destruição do componente em cache que o keep-alive mantém

```js
deactivated() {
  delete this.$vnode.parent.componentInstance.cache.SelecionarProcessosStep;

  this.$vnode.parent.componentInstance.keys = this.$vnode.parent.componentInstance.keys.filter(
    (component) => {
      return component !== 'SelecionarProcessosStep';
    }
  );
  this.$destroy()
}
```

#### Os lifecycle hooks diferentes quando se usa keep-alive
Sã0 criados:
```js
  activated() {},
  deactivated() {},
```
Deixam de existir:
  ~~beforeDestroy() {},~~
  ~~destroyed() {},~~



### v-for
Não fazer mais de um mesmo `v-for` caso precise de uma validação do valor retornado dele, o `jsx` não vai conseguir carregar, faça a validação no retorno (dentro) do `v-for`

### watch property:
- Quando for preciso verificar propriedades de maneira básica (sem precisar de valores novo e velho ou de suas propriedades), o melhor a se fazer é faze-lo em formato de função e não de objeto.


    ✅
    ```
    data(){
      return {
        value: {name: 'Arthur'},
      }
    },
    watch: {
      value() {
        this.doSomething();
      },
    }
    ```

    🚫
    ```
    data(){
      return {
        value: {name: 'Arthur'},
      }
    },
    watch: {
      value: {
        handler() {
          this.doSomething();
        },
        ...
      },
    }
    ```

## $set ou Vue.set

É um metodo para inserir propriedades novas à um objeto reativo do vue.js, já que ele não consegue tornar propriedades comuns como reativas.


Não reativo
```
this.myObject.newProperty = 'hi'
``` 

Reativo
```
this.$set(this.objeto, 'newProperty', newValue);
``` 

### v-model
.lazy
Por padrão, v-model sincroniza o elemento com os dados após cada evento do tipo input (com exceção para o caso de composição IME descrito anteriormente). Mas adicionando o modificador lazy, a sincronização ocorrerá após o evento change:

<!-- sincronizado depois do "change" ao invés de "input" -->
<input v-model.lazy="msg">
.number
Se você quiser que a entrada do usuário seja automaticamente convertida para Number, pode adicionar o modificador number ao v-model do elemento:

<input v-model.number="age" type="number">
Isso é bastante útil, porque mesmo no caso de type="number", o valor retornado pelo HTML é sempre uma String. Se o valor não puder ser convertido através de parseFloat(), o valor original é retornado.

.trim
Se você quiser que a entrada do usuário seja automaticamente isenta de espaços no início e no fim do texto, você pode adicionar o modificador trim ao v-model do elemento:

<input v-model.trim="msg">