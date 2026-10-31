# Fichamento Acadêmico Rigoroso

Skill para o [Claude Code](https://claude.com/claude-code) que transforma um artigo científico em PDF num fichamento de nível de pós-graduação, com rastreabilidade de página em cada afirmação.

Feita para quem escreve dissertação, tese ou artigo e usa fichamentos como banco de dados confiável na hora de redigir.

## O que a skill entrega

Para cada artigo, um arquivo Markdown com frontmatter YAML, pronto para Obsidian, Notion ou Zotero, contendo:

1. **Referência bibliográfica** em ABNT NBR 6023:2018 e APA 7, com DOI.
2. **Fichamento de conteúdo**: problema de pesquisa, objetivos, arcabouço teórico, recorte, desenho metodológico detalhado (amostra, equipamentos, softwares, testes estatísticos) e resultados com os números exatos do artigo.
3. **Tabela de citações diretas**: de 5 a 10 trechos literais no idioma original, com página, paráfrase em português no formato de citação indireta e a seção do trabalho onde cada um pode ser usado.
4. **Parecer crítico**: pontos fortes, fragilidades metodológicas, limitações declaradas pelos autores, lacunas de pesquisa e conexão com o tema do usuário.

O relato do artigo e a crítica ficam visualmente separados.

## Por que confiar nas páginas

A skill não inventa páginas, DOIs, números nem coautores. O script incluído extrai o texto do PDF página a página e tenta detectar a numeração impressa. Quando uma informação não está visível no documento, o fichamento registra `[página não identificada]` ou `[DOI não informado]` em vez de um palpite.

Ainda assim, confira as citações no PDF antes de usá-las num texto que vai para banca ou periódico.

## Requisitos

- Claude Code (aplicativo desktop, terminal ou extensão de IDE).
- Python 3.9 ou mais recente.
- [PyMuPDF](https://pymupdf.readthedocs.io/):

```bash
pip install pymupdf
```

PDFs escaneados sem camada de texto precisam passar por OCR antes.

## Instalação

A skill é distribuída como plugin do Claude Code. Dentro de uma sessão do Claude Code, rode uma vez:

```text
/plugin marketplace add Oeditorpod/fichamento-academico
```

```text
/plugin install fichamento-academico@fichamento-academico
```

Pelo terminal, sem abrir uma sessão, os comandos equivalentes são:

```bash
claude plugin marketplace add Oeditorpod/fichamento-academico
claude plugin install fichamento-academico@fichamento-academico
```

Se o seu computador não tem chave SSH cadastrada no GitHub e a instalação falhar, defina a variável `CLAUDE_CODE_PLUGIN_PREFER_HTTPS=1` e tente de novo.

## Atualizações automáticas

O Claude Code deixa a atualização automática desligada para marketplaces de terceiros. Para receber as novas versões sem precisar fazer nada, ligue uma vez:

1. Rode `/plugin` numa sessão do Claude Code.
2. Abra a aba **Marketplaces** e selecione `fichamento-academico`.
3. Escolha **Enable auto-update**.

Se preferir atualizar manualmente, rode:

```text
/plugin marketplace update fichamento-academico
```

As mudanças são publicadas com número de versão. Você só recebe uma atualização quando a versão muda, e o histórico fica em [CHANGELOG.md](CHANGELOG.md).

### Instalação manual, sem atualizações

Para usar sem o sistema de plugins, copie a pasta `skills/fichamento-academico` deste repositório para `~/.claude/skills/`. Nesse caso as atualizações não chegam sozinhas.

## Como usar

Abra o Claude Code na pasta onde estão seus artigos e peça em linguagem natural:

- "Ficha o artigo `artigos/silva_2024.pdf`"
- "Tira as citações com página desse PDF para a minha introdução"
- "Ficha todos os PDFs da pasta `artigos`"

Ou chame a skill diretamente:

```text
/fichamento-academico:fichamento-academico artigos/silva_2024.pdf
```

Na primeira vez em cada conversa, a skill pergunta o tema da sua pesquisa para direcionar o parecer. Se você já informar o tema junto com o pedido, ela começa direto.

Os fichamentos são salvos como `fichamento_<autor>_<ano>.md`, ou dentro de uma pasta `fichamentos/` se ela existir.

## Estrutura do repositório

```text
fichamento-academico/
├── .claude-plugin/
│   ├── marketplace.json                 catálogo lido pelo /plugin
│   └── plugin.json                      nome e versão do plugin
├── skills/fichamento-academico/
│   ├── SKILL.md                         instruções que o Claude segue
│   ├── references/
│   │   ├── template.md                  modelo de saída do fichamento
│   │   └── formatos-referencia.md       regras ABNT e APA por tipo de obra
│   └── scripts/
│       └── extract_pages.py             extração de texto do PDF por página
├── CHANGELOG.md
├── LICENSE
└── README.md
```

O script também funciona sozinho:

```bash
python skills/fichamento-academico/scripts/extract_pages.py artigo.pdf > artigo.txt
```

## Limitações

- A detecção da numeração impressa depende do layout do PDF. Quando falha, a skill cita pelo índice físico e avisa no frontmatter.
- Texto em duas colunas pode sair com a ordem das linhas alterada. A skill é instruída a conferir no PDF os trechos duvidosos.
- O parecer crítico é uma leitura assistida, não substitui a sua avaliação do artigo.

## Contribuições

Sugestões e correções são bem-vindas por issue ou pull request, principalmente sobre regras ABNT e APA e sobre PDFs em que a detecção de páginas falha.

## Licença

[MIT](LICENSE)
