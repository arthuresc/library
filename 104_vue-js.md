# Vue.js

## TROUBLESHOOTER

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