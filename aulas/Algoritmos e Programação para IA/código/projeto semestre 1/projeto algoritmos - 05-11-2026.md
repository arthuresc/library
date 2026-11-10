---
title: "Projeto de projeto algoritmos"
type: aula
tags: [aula, disciplina/algoritmos-e-programacao-para-ia]
status: registrado
date: 2026-11-05
---
# Projeto de projeto algoritmos

## O que precisa ser feito:

- Usaremos o dataset:
  - hwc.csv
    - Não está 100% tratado
    - tem valores que não vamos precisar
    - tem uma excelente documentação
    - existe a versão dele JÁ TRATADA
    - os dados estão simples de serem resolvidos
    - 
    - ~~https://www.kaggle.com/datasets/vrushabhsonawane1/exoplanets-dataset?resource=download~~
  - ~~ou~~
    - ~~https://www.kaggle.com/datasets/walididbennacer/exohabx-habitable-exoplanets-dataset-nasa-hwc (<--- Usando)~~
- ~~Provavelmente usaremos o algoritmo de Machine Learning Gaussian Mixture Models~~
- Usaremos o K-Means com graficos e o K-means mesmo aplicando o ESI (valor gerado pela gente com base na distancia do planeta ao proprio SOL e o valor do RAIO dele) junto da distancia do planeta ao nosso SOL como uma referencia a gente para que possamos medir se é possivel irmos até ele.
- 



## TODOs:

- [ ] ...

## Infos, links e fontes:

- ESI:
# Guia Visual do ESI (Earth Similarity Index) via Média Quadrática

Este guia utiliza diagramas de fluxo para explicar a lógica matemática e o código por trás do Índice de Similaridade com a Terra (ESI).

---

## 1. A Lógica da Fórmula Geral (Lendo o RMS de trás para frente: S ➔ M ➔ R)

Em vez de ler fórmulas com símbolos matemáticos, este diagrama mostra exatamente como os dados fluem através da estrutura **RMS** (Square, Mean, Root) alterada para o ESI.

```mermaid
graph TD
    %% Estilos Globais
    classDef entrada fill:#f9f,stroke:#333,stroke-width:2px;
    classDef processo fill:#bbf,stroke:#333,stroke-width:1px;
    classDef rms fill:#fbb,stroke:#333,stroke-width:2px;
    classDef resultado fill:#bfb,stroke:#333,stroke-width:2px;

    %% Nós do Fluxo
    A[Dados do Planeta] --> B[Calcular Desvio Relativo]
    Ref[Dados de Referência da Terra] --> B
    
    B -->|Fórmula: Planeta - Terra / Planeta + Terra| C(Desvio de cada Propriedade)
    
    %% Bloco RMS ao contrário (S -> M -> R)
    C --> D[1. SQUARE: Elevar cada desvio ao quadrado]
    D --> E[2. MEAN: Somar todos e dividir pela quantidade de propriedades]
    E --> F[3. ROOT: Tirar a Raiz Quadrada de tudo]
    
    %% Conclusão ESI
    F -->|Resultado = Erro Total Acumulado| G[Toque do ESI: Fazer 1 menos o Erro]
    G --> H((ESI Final))

    %% Aplicação de Estilos
    class A,Ref entrada;
    class B,C processo;
    class D,E,F rms;
    class G,H resultado;
```

---

## 2. Exemplo Prático de Fluxo: Calculando Marte

Este mapa mental numérico simula o passo a passo exato do cálculo usando o Raio e o Fluxo Estelar de Marte.

```mermaid
graph LR
    %% Estilos
    classDef dado fill:#fff,stroke:#333,stroke-width:1px;
    classDef calc fill:#ddd,stroke:#333,stroke-width:1px;
    classDef final fill:#bfb,stroke:#333,stroke-width:2px;

    %% Fluxo do Raio
    subgraph Fluxo do Raio
        R1[Raio Marte: 0.53] --> R2["Desvio: (0.53 - 1) / (0.53 + 1) = -0.307"]
        R2 --> R3["SQUARE (Quadrado): 0.094"]
    end

    %% Fluxo da Luz
    subgraph Fluxo da Luz Solar
        S1[Luz Marte: 0.43] --> S2["Desvio: (0.43 - 1) / (0.43 + 1) = -0.399"]
        S2 --> S3["SQUARE (Quadrado): 0.159"]
    end

    %% Integração RMS
    R3 --> M["MEAN (Média dos dois): <br> (0.094 + 0.159) / 2 = 0.1265"]
    S3 --> M
    
    M --> Ro["ROOT (Raiz Quadrada): <br> Raiz de 0.1265 = 0.355"]
    
    %% Resultado
    Ro --> F["ESI Final: <br> 1 - 0.355 = 0.645"]

    class R1,S1 dado;
    class R2,R3,S2,S3,M,Ro calc;
    class F final;
```

---

## 3. Arquitetura do Código Genérico (Python / NumPy / Pandas)

Este diagrama representa visualmente o que as funções de código fazem nos bastidores, eliminando a necessidade de ler linhas puras de código para entender a lógica de processamento vetorial.

```mermaid
graph TD
    classDef func fill:#e1f5fe,stroke:#03a9f4,stroke-width:2px;
    classDef etapa fill:#fff,stroke:#777,stroke-width:1px;

    subgraph Entrada de Dados Genérica
        P[Array / Lista de Planetas Avaliados]
        T[Array / Lista com Valores da Terra]
    end

    subgraph Processamento Interno da Função
        E1[Subtrai e divide os arrays para gerar os desvios relativos]
        E2[Eleva toda a matriz de desvios ao quadrado exponencialmente]
        E3[np.mean: Consolida a média dos desvios verticalmente ou por eixo]
        E4[np.sqrt: Reduz a escala tirando a raiz quadrada global]
    end

    subgraph Retorno de Saída
        S1[Subtrai o resultado de 1]
        Out[Métrica ESI Pronta entre 0.0 e 1.0]
    end

    P --> E1
    T --> E1
    E1 --> E2
    E2 --> E3
    E3 --> E4
    E4 --> S1
    S1 --> Out

    class E1,E2,E3,E4 func;
    class P,T,S1,Out etapa;
```



- Fonte:
  - Dados: https://phl.upr.edu/home
  - Calculo matemático usado no ESI: 
    - 
  - Calculo de parsecs em anos luz: anos-luz​=S_DISTANCE×3,26156
    - O S_DISTANCE se trata da distancia do Sol do planeta até o nosso planeta Terra, então se trata de uma aproximação
- Os alunos devem fazer:
  - Apresentar insights iniciais
  - Mostrar estatísticas básicas
  - Identificar valores nulos
  - Apresentar com gráficos
- Insights:
  - Quais são os planetas que seria possivel irmos lá descobrir se HÁ vida ou se é possivel HABITAR vida (semelhante a nossa) lá
    - Primeiro eliminamos os planetas que não tem dados o suficiente (P_RADIUS e P_FLUX)
    - Pra isso calculamos o ESI deles
  - Mas e ai as IA's vão acabar com o planeta? Gastando nossa água, esquentando nosso planeta, acabando com nossos recursos? Então cabe a gente resolver isso, como? Com IA's que desperdiçam menos energia? Com uso mais responsavel das IAs? Com pensamentos mais sustentaveis? NÃO!! NUNCA!! MAS SIM ESCOLHENDO OUTRO PLANETA... Já fud&#øs o nosso, melhor escolher outro mesmo. E foi com essa ideia que pensamos, quais seriam bons planetas para a gente morar quando tudo isso aquifor pras cucuias?
  Nas nossas pesquisas trouxemos o indice ESI (Earth Similarity Index ou Indice de Similaridade com a Terra), usado como um indice superficial pela Universidade de Porto Rico com esse dataset para inicialmente identificar planetas que conseguiriam ter o minimo de similaridade com a Terra, pois é a premissa de mantermos uma vida baseada em carbono (que é a nossa). Depois disso veio a pergunta "Mas da pra chegar com o meu BYD Dolphin Hybrid com 1000km de autonomia?" e para o desespero meu (e do Han Solo e já explico o porquê) não dá. Acontece que estamos muitos anos luz (ly) de distancia, que originalmente estão registrados em parsecs ou pc (viu Han Solo, não é medida de tempo e sim de distancia, mentiroso salafrario). 

## Notas e Rascunhos:

...
