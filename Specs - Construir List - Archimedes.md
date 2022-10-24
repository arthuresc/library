# Feature

## Qual o funcionalidade ou melhoria que essa feature se propõe a realizar ?
Essa issue cria uma listagem de processos que estão aptos para faturamento. O objetivo é conseguir encontrar de forma rápida todos os processos que já podem ser faturados. 

## Descrição da feature
- Será necessário criar uma tela de listagem dos processos com status apto para faturamento **APROVADO**, cujo valor é **3**;
- Deve existir um novo item no menu de acesso para essa listagem;
- O menu deve conter regra de ACL para restringir o acesso;
- Deve existir por registro a opção de visualizar o processo;
- A listagem deve ser com scroll infinito;
- Deve existir a opção de **criar NFSe em lote**, onde o **Ator** pode selecionar um ou mais registros para criar a NFSe;
- O botão com a ação de **criar NFSe em lote** deverá estar desabilitado na entrega dessa issue.
- Deve existir a opção de **faturar em lote**, onde o **Ator** pode selecionar um ou mais registros para emitir a fatura;
- O botão com a ação de **faturar em lote** deverá estar desabilitado na entrega dessa issue.
- Deve existir a opção de **criar processo consolidado**, onde o **Ator** pode selecionar um ou mais registros para criar um processo consolidado;
- O botão com a ação de **criar processo consolidado** deverá estar desabilitado na entrega dessa issue.


## Há dependências de outras issues?
- Não há

### Se sim, quais?
- Não há


## Quais são os endpoints que deverão ser utilizados para essa issue?
- /api/processos?statusFinanceiro={status} 
- /api/processos/{id}

## Existem regras de ACL para essa feature?
- Sim

### Quais?
| Nome | Caminho |
| ------ | ------ |
| Menu de aptos Faturamento | menu_faturamento_aptos |
| Ação de faturar | lista_faturamento_faturar |
| Ação de criar NFSe | lista_faturamento_criar_nfse |
| Ação de criar processo consolidado | lista_faturamento_criar_processo_consolidado |

## Essa issue inclui campos novos na tela?
- As seguintes colunas deve ser exibidas na listagem, seguindo a tabela abaixo.

### Quais?

| Nome | Atributo | Tipo | Tipo input | Obrigatoriedade | Entidade de relacionamento | Atributo de relacionamento | Valor |
|------|----------|------|------------|-----------------|----------------------------|----------------------------|---------|
| Número | numero |string| - | sim | - | - | 2102ER00144 |-|
| Processo Complementar | processoComplementar | string | - | não | - | - | 2102ER00144 | - |
| Cliente | importadorCliente | string | - | sim | Cliente | codigo | 1118 | - |
| Sacado | sacado | string | - | sim | Cliente | codigo | 1118 | - |
| data do fechamento | dataFechamento | Datetime | - | sim | - | - | 10/08/2021 | - |
| 1ª Referência cliente | referenciaCliente1 | string | - | não | - | - | GF-4445 |
| Filial de Faturamento | filialFaturamento | string | - | não | Filial | codigo | 2 |


## Observações
- Listagem deve possuir os mesmos filtros já criados na listagem padrão de processos exceto status financeiro e emissão da fatura e deve ser incluído o filtro por período da data do fechamento;
- Listagem deve possuir as seguintes opções de ordenação: Alterado recentemente e referência do cliente;


## Casos de teste:
Entrar na rota de `/aprovados`:
- [ ] Apresentar listagem de processos com statusFinanceiro = 3
- [ ] As colunas da listagem precisam ter as mesmas citadas acima
- [ ] Os processos listados devem ter um campo para selecionar dando a opção de faturar em lote
- [ ] O número do processo precisar ser um caminho/link para a visualização de processo
- [ ] Listagem de carregamento infinito (que só carrega quando rodamos a listagem até o final)
- [ ] 
