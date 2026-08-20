async function createNote({ trigger, foam, resolver }) {
  const title = (await resolver.resolveFromName('FOAM_TITLE')) || 'nota';
  const today = dayjs();

  // Detect meeting type from title
  const isProjeto = title.toLowerCase().includes('projeto');
  const isAula = title.toLowerCase().includes('aula');

  const regex = /\s*(?:aula|aulas|projeto|projetos)\s*/gi;
  const titleTratado = title.toLowerCase().replace(regex, "");

  const nomeMateria = {
  pi:"PI",
  algoritmos:"Algoritmos e Programação para IA",
  matematica:"Bases Matematicas para IA",
  ia:"Introdução à Inteligência Artificial",
  pesquisa:"EAD - Pesquisa, tecnologia e Sociedade",
  banco:"Banco de Dados para IA",
  intro:"Introdução à Computação"}[titleTratado] || "nota";

  const tituloNota = title.replace(/\bnota?\b/gi, "");
  

  let template = ``;
  let fileName = `${title} - ${today.format('DD-MM-YYYY')}`

  if (isProjeto) {
    template += 
`
# Projeto de ${title}



## O que precisa ser feito:
- 

## TODOs:
- [ ] ...

## Infos, links e fontes:
- 

## Notas e Rascunhos:
...

`;
  } else if (isAula) {
    template += `

# Aula de ${title}



## O que entendi:
- ...

## O que não entendi:
- ...

## TODOs (tarefas):
- [ ] ...

## Glossário:
- ...

## Notas e Rascunhos:
...


`;
  } else {
    template += 
`# Anotação: ${tituloNota} - Data: ${today.format('DD-MM-YYYY')}



## Anotações e Afazeres :
- 


## TODOs :
- [ ] ...



## Rascunhos :
`;
  }

  return {
    content: template,
    filepath: `/aulas/${nomeMateria}/${fileName}.md`,
  };
}