# Vue.js

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