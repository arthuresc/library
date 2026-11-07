// .foam/templates/aulas.js — v2 alinhado ao Zettelkasten / Second Brain do vault
async function createNote({ trigger, foam, resolver }) {
  const title = (await resolver.resolveFromName('FOAM_TITLE')) || 'nota';
  const today = dayjs();
  const isoDate = today.format('YYYY-MM-DD');
  const displayDate = today.format('DD-MM-YYYY');

  // Detect meeting type from title
  const isProjeto = title.toLowerCase().includes('projeto');
  const isAula = title.toLowerCase().includes('aula');

  const regex = /\s*(?:aula|aulas|projeto|projetos)\s*/gi;
  const titleTratado = title.toLowerCase().replace(regex, "");

  const nomeMateria = {
    pesquisa: "EAD - Pesquisa, tecnologia e Sociedade", // EAD - online
    algoritmos: "Algoritmos e Programação para IA", // Segunda-feira
    intro: "Introdução à Computação", // Terça-feira 1/2
    pi: "PI", // Terça-feira 2/2
    matematica: "Bases Matematicas para IA", // Quarta-feira
    banco: "Banco de Dados para IA", // Quinta-feira
    ia: "Introdução à Inteligência Artificial", // Sexta-feira
  }[titleTratado] || "nota"; // Default

  const slug = (s) =>
    s
      .normalize("NFKD")
      .replace(/[\u0300-\u036f]/g, "")
      .toLowerCase()
      .replace(/[^a-z0-9]+/g, "-")
      .replace(/^-|-$/g, "");

  const type = isProjeto ? "projeto" : isAula ? "aula" : "nota";
  const fileName = `${title} - ${displayDate}`;

  const frontmatter = `---
title: "${title.replace(/"/g, "'")}"
type: ${type}
tags: [${type}, disciplina/${slug(nomeMateria)}]
status: registrado
date: ${isoDate}
---`;

  let template = ``;
  if (isProjeto) {
    template += `
${frontmatter}
# Projeto de ${title}

## Objetivo (Bloom: criar)
- ...

## O que precisa ser feito:
- [ ] ... @next

## Infos, links e fontes:
- ...

## Promover pra evergreen (Second Brain: Distill)
- [ ] Destilei o aprendido em evergreen em notes/ e adicionei no [[000-index]]

## Relacionadas (Zettelkasten)
- [[000-index]]
- [[todo]]

## Notas e Rascunhos:
...
`;
  } else if (isAula) {
    template += `
${frontmatter}
# Aula de ${title}

## Principal
- ...

## O que entendi:
- ...

## O que não entendi:
- ...

## Exemplo/prática (Feynman — explique como se fosse ensinar)
- ...

## Próxima ação (GTD)
- [ ] ... @next

## Glossário:
- ...

## Promover pra evergreen (Second Brain: Distill)
- [ ] Transformei o que entendi em evergreen e adicionei no [[000-index]]

## Relacionadas (Zettelkasten)
- [[000-index]]

## Notas e Rascunhos:
...
`;
  } else {
    template += `
${frontmatter}
# Anotação: ${title} - Data: ${displayDate}

## Anotações e Afazeres :
- ...

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
