# Modelo de saída do fichamento

Use exatamente esta estrutura. Troque o conteúdo entre colchetes; mantenha os cabeçalhos.

````markdown
---
titulo: "[título completo original]"
autores: ["Sobrenome, N. N.", "Sobrenome, N. N."]
ano: [AAAA]
periodico: "[nome do periódico, volume(número)]"
doi: "[10.xxxx/xxxxx ou 'não informado']"
idioma: "[en | pt | es ...]"
paginacao: "[impressa | fisica]"
tema_pesquisa_usuario: "[tema informado na calibragem]"
tags: [fichamento, [tema1], [tema2], [metodo]]
data_fichamento: [AAAA-MM-DD]
---

### 1. Referência Bibliográfica

- **ABNT (NBR 6023:2018):** SOBRENOME, N.; SOBRENOME, N. Título do artigo. **Nome do Periódico**, v. X, n. Y, p. A-B, AAAA. DOI: 10.xxxx/xxxxx.
- **APA 7:** Sobrenome, N., & Sobrenome, N. (AAAA). Título do artigo. *Nome do Periódico*, X(Y), A-B. https://doi.org/10.xxxx/xxxxx

### 2. Fichamento de Conteúdo e Anatomia Metodológica

> Relato fiel do artigo. Toda afirmação traz a página entre parênteses.

- **Problema de pesquisa / pergunta central:** [...] (p. X).
- **Objetivo geral e específicos:** [...] (p. X).
- **Arcabouço teórico:** [conceitos e autores nomeados] (p. X).
- **Recorte espacial e temporal:** [...] (p. X).
- **Desenho metodológico:**
  - *Tipo de estudo:* [...] (p. X).
  - *Amostragem / n:* [...] (p. X).
  - *Variáveis / instrumentos / equipamentos / reagentes:* [...] (p. X).
  - *Análise:* [testes, modelos, softwares, versões, nível de significância] (p. X).
- **Principais resultados:**
  - [resultado com número exato, unidade e métrica] (p. X).
  - [...]
- **Conclusões dos autores:** [...] (p. X).
- **Limitações declaradas pelos autores:** [...] (p. X).

### 3. Fichamento de Citações Diretas e Paráfrases

| Página | Citação Literal (Original) | Paráfrase em PT-BR (citação indireta) | Aplicação Sugerida |
| --- | --- | --- | --- |
| **p. X** | "[transcrição ipsis litteris]" | [paráfrase com (Autor, ano)] | **[Seção]:** [para que serve] |

### 4. Fichamento Crítico e Parecer Metodológico

> **Voz do parecerista.** O que segue é análise crítica, não relato do artigo.

- **Rigor e contribuição:** [...]
- **Fragilidades metodológicas e vieses:** [...] (referir a página do trecho criticado).
- **Premissas questionáveis:** [...]
- **Lacunas de pesquisa (research gaps):** [...]
- **Conexão com a pesquisa do usuário:** [em qual seção do trabalho dele este artigo entra, o que sustenta e o que não cobre].
````

## Notas de uso

- Citação literal sempre no idioma original; a tradução vai só na coluna de paráfrase.
- Números: mantenha a casa decimal e o separador do original dentro da citação literal; na paráfrase use vírgula decimal (padrão PT-BR).
- Quando a página não for identificável: `[página não identificada]`, nunca um número estimado.
- Se o usuário pedir formato diferente (só a tabela de citações, ou só o parecer), entregue a parte pedida sem perder a rastreabilidade de página.
