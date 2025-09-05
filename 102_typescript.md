# Typescript

Apesar de parecido com (e transpilado para) o javascript, o TS (typescript) veio para solucionar os problemas que seu irmão mais velho possui já que é tipado e possui como ser aplicado completamente OOP.

## Operators (Operadores)

## Funções
Para as funções é necessário descrever o tipo 

## Interfaces
- Igual ao oq outras linguagens orientadas à objetos já possuem é como se fosse uma prévia de uma classe.
É esperado de retorno da `interface` um objeto.

```typescript
interface LabeledValue {
  label: string;
}

function printLabel(labelledObject: LabelledValue) {
  console.log(labeledObject.label); // O `label` agora oriundo da interface`
}
```
- `interfaces` e `types` são muitíssimo parecidos
  - `types`: 
    - É possivel configurar `union` como tipo da propriedade do `type`, fazendo assim é possivel, por exemplo, configurar um tipo que a propriedade dele é um objeto com a `interface` x ou pode ser y, usando o tipo `union` para que seja decidido na hora
   
  - `interface`: 
    - É possivel fazer _Declaração de Merge (Declaration Merging)_ é aonde você declara uma `interface` e após isso você declara a mesma interface mas com outras propriedades, o que faz com que ambas se mesclem
  - TEM ERROS ACIMA, PRECISO ESTUDAR E APRENDER MAIS, ARTIGOS ANTES DE 2023 NÃO SÃO TÃO BONS
