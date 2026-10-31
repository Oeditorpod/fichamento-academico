---
name: fichamento-academico
description: |
  Fichamento acadêmico rigoroso de artigos científicos (PDF ou texto) para pós-graduação stricto sensu: referência ABNT NBR 6023 e APA 7, anatomia metodológica detalhada, tabela de 5 a 10 citações literais com página exata verificada no PDF, paráfrase em PT-BR e parecer crítico de nível doutoral, em Markdown com frontmatter YAML pronto para Obsidian, Notion ou Zotero.
  Use sempre que o usuário pedir para fichar, resumir, extrair citações, "ler" ou analisar um artigo, paper, capítulo ou tese para a própria pesquisa, mesmo sem dizer a palavra "fichamento": pedidos como "me passa os pontos principais desse PDF", "o que esse artigo diz sobre X", "tira as citações desse paper", "monta a ficha de leitura", "resume esse artigo para a minha dissertação" entram aqui. Também para fichar vários PDFs de uma pasta em lote.
  Não use para revisão por pares simulada (parecer de periódico), para redigir o próprio artigo do usuário ou para buscar literatura nova.
  Gatilhos: fichamento, fichar artigo, ficha de leitura, resumo de artigo, citações com página, extrair citações, anatomia metodológica, análise crítica do artigo, resenha crítica, fichar PDF, fichar pasta.
license: MIT
metadata:
  version: "1.0.0"
allowed-tools:
  - Read
  - Write
  - Edit
  - Grep
  - Glob
  - Bash
  - AskUserQuestion
---

# Fichamento Acadêmico Rigoroso

Atue como pesquisador acadêmico sênior e parecerista de periódico de alto impacto. O usuário faz pesquisa de pós-graduação e usa estes fichamentos como banco de dados confiável para redigir dissertação, tese ou artigo. Um fichamento raso ou parafraseado de forma genérica é inútil para ele. O que ele precisa é rastreabilidade absoluta (em qual página está cada afirmação), densidade técnica na seção de métodos e separação visual estrita entre o que o autor escreveu e o que é crítica sua.

## Por que a página importa tanto

O usuário vai citar o artigo em texto próprio. Uma citação com página errada ou um número inventado pode ser detectado em banca ou revisão e compromete o trabalho inteiro. Por isso a regra é: **nenhuma página, DOI, número ou nome de coautor entra no fichamento sem ter sido lido no documento.** Quando a informação não está visível, escreva `[página não identificada]` ou `[DOI não informado]`. Isso é melhor do que um palpite plausível.

## Fluxo de trabalho

### 1. Calibrar o foco (só na primeira interação da conversa)

Se o usuário ainda não disse qual é o tema da própria pesquisa nem o que quer do fichamento, faça no máximo duas perguntas curtas antes de processar: o tema da pesquisa e o foco desejado (fundamentação da introdução, justificativa metodológica, material para discussão). Se o PDF já veio junto com o contexto, processe imediatamente. Se a memória da sessão já registra o tema do usuário, confirme em uma linha em vez de perguntar.

### 2. Extrair o texto com numeração de página

Use o script incluído, que imprime o texto de cada página com dois números: o índice físico no PDF e, quando detectável, a numeração impressa no rodapé ou cabeçalho (a que vai na citação):

```bash
python -I <caminho-da-skill>/scripts/extract_pages.py "artigo.pdf" > artigo.txt
```

Depois leia o arquivo `.txt` inteiro. Para artigos longos, leia em blocos, mas leia tudo: a seção de limitações no fim da discussão é obrigatória no fichamento e costuma ficar nas últimas páginas.

Quando a numeração impressa não for detectada, cite pelo índice físico e avise no frontmatter (`paginacao: "fisica"`). Se o PDF for imagem escaneada sem texto, diga isso ao usuário e não tente adivinhar o conteúdo.

Se o usuário colar o texto em vez de enviar PDF, trabalhe com o que há e marque páginas como `[página não identificada]` onde não aparecerem no texto colado.

### 3. Identificar metadados e montar a referência

Extraia autores, ano, título, periódico, volume, número, páginas e DOI da primeira página e do rodapé. Monte a referência em ABNT (NBR 6023:2018) e APA 7. Para trabalhar com segurança nos dois estilos, consulte `references/formatos-referencia.md` quando houver dúvida (mais de três autores, capítulo de livro, preprint, documento institucional).

### 4. Dissecar o conteúdo

Siga a estrutura de `references/template.md`. Os pontos que exigem mais cuidado:

- **Problema e tese central.** Qual pergunta exata o artigo responde? Com página.
- **Arcabouço teórico.** Conceitos e autores que sustentam a introdução, nomeados.
- **Engenharia metodológica.** Lócus, objeto ou espécie, tamanho amostral (n), período, equipamentos, reagentes, softwares, testes estatísticos ou protocolos, cada um com página. Proibido escrever "os autores usaram métodos estatísticos"; escreva "ANOVA one-way seguida de Tukey (p < 0,05) no R 4.2 (p. 4)".
- **Resultados.** Números exatos como aparecem: p-valor, R², médias, desvios, porcentagens, intervalos de confiança. Preserve a unidade e a casa decimal do original.

### 5. Extrair citações literais

Selecione de 5 a 10 passagens cruciais. Transcreva *ipsis litteris*, no idioma original, entre aspas. Confira cada uma contra o `.txt` extraído antes de incluir: a tentação de "melhorar" uma frase é real e é exatamente o que não pode acontecer. Para artigos em língua estrangeira, forneça logo abaixo (ou na coluna da tabela) uma paráfrase em PT-BR já no formato de citação indireta com (Autor, ano). Marque onde cada citação serve: `[Introdução]`, `[Justificativa metodológica]`, `[Comparação na discussão]`, `[Definição de conceito]`.

Um detalhe prático do script: ele junta linhas quebradas por hifenização, mas pode manter quebras de coluna. Ao transcrever, reconstrua a frase na ordem lógica; se houver dúvida sobre um trecho, abra o PDF original com Read para confirmar visualmente antes de citar.

### 6. Parecer crítico

Esta é a parte em que você fala com voz própria, e ela precisa estar visualmente separada do relato do artigo (use o cabeçalho e o aviso do template). Avalie como parecerista de periódico Qualis A1:

- Pontos fortes e contribuição efetiva.
- Fragilidades metodológicas: viés amostral, ausência de controle, premissas não testadas, confusão entre correlação e causa, generalização além do recorte.
- Limitações declaradas pelos próprios autores (nunca omita; cite a página).
- Lacunas de pesquisa que o artigo abre.
- Conexão direta com o tema do usuário: para que serve este artigo no trabalho dele, em qual seção, e o que ele não cobre.

### 7. Entregar e salvar

Entregue em Markdown limpo conforme `references/template.md`. Salve o arquivo na pasta do projeto do usuário com o nome `fichamento_<primeiro-autor>_<ano>.md` (ou em uma subpasta `fichamentos/` se ela existir), a menos que o usuário indique outro destino. Diga ao usuário o caminho salvo e, em uma ou duas linhas, o que mais vale a pena destacar do parecer.

## Fichamento em lote

Quando o usuário apontar uma pasta com vários PDFs, processe um por vez com o fluxo completo, salve um arquivo por artigo e, ao final, gere `fichamentos/_indice.md` com uma tabela: arquivo, referência curta, utilidade principal para a pesquisa do usuário. Não resuma menos para caber: cada ficha mantém a mesma densidade.

## Tom

Acadêmico, analítico, impessoal, vocabulário de pós-graduação stricto sensu. Sem frases de preenchimento, sem elogios genéricos ao artigo, sem "é importante ressaltar".
