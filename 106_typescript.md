# Typescript

Apesar de parecido com (e transpilado para) o javascript, o TS (typescript) veio para solucionar os problemas que seu irmão mais velho possui já que é tipado e possui como ser aplicado completamente OOP.

## Operators (Operadores)

## Funções
Para as funções é necessário descrever o tipo 

## Interfaces
Igual ao oq outras linguagens orientadas à objetos já possuem é como se fosse uma prévia de uma classe.
É esperado de retorno da `interface` um objeto.

```typescript
interface LabeledValue {
  label: string;
}

function printLabel(labelledObject: LabelledValue) {
  console.log(labeledObject.label); // O `label` agora oriundo da interface`
}
```