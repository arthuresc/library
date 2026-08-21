async function createNote({ trigger, foam, resolver }) {
  const title = (await resolver.resolveFromName('FOAM_TITLE')) || 'nota';
  const today = dayjs();

  // Detect meeting type from title
  const isProjeto = title.toLowerCase().includes('projeto');
  const isAula = title.toLowerCase().includes('aula');

  const regex = /\s*(?:aula|aulas|projeto|projetos)\s*/gi;
  const titleTratado = title.toLowerCase().replace(regex, "");

  console.log("Teste")

  const nomeMateria = {
  pesquisa:"EAD - Pesquisa, tecnologia e Sociedade",  // EAD - online
  algoritmos:"Algoritmos e Programação para IA",      // Segunda-feira
  intro:"Introdução à Computação",                    // Terça-feira 1/2
  pi:"PI",                                            // Terça-feira 2/2
  matematica:"Bases Matematicas para IA",             // Quarta-feira
  banco:"Banco de Dados para IA",                     // Quinta-feira
  ia:"Introdução à Inteligência Artificial"           // Sexta-feira
}[titleTratado] || "nota";                            // Default

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

## Principal
- ...

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