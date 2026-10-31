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

Clone o repositório na sua pasta pessoal de skills. Assim ela fica disponível em todos os projetos.

macOS ou Linux:

```bash
git clone https://github.com/Oeditorpod/fichamento-academico.git ~/.claude/skills/fichamento-academico
```

Windows (PowerShell):

```powershell
git clone https://github.com/Oeditorpod/fichamento-academico.git "$env:USERPROFILE\.claude\skills\fichamento-academico"
```

Para usar só em um projeto, clone em `.claude/skills/fichamento-academico` dentro da pasta do projeto.

Também é possível instalar pelo catálogo aberto de skills:

```bash
npx skills add Oeditorpod/fichamento-academico
```

## Como usar

Abra o Claude Code na pasta onde estão seus artigos e peça em linguagem natural:

- "Ficha o artigo `artigos/silva_2024.pdf`"
- "Tira as citações com página desse PDF para a minha introdução"
- "Ficha todos os PDFs da pasta `artigos`"

Ou chame a skill diretamente:

```text
/fichamento-academico artigos/silva_2024.pdf
```

Na primeira vez em cada conversa, a skill pergunta o tema da sua pesquisa para direcionar o parecer. Se você já informar o tema junto com o pedido, ela começa direto.

Os fichamentos são salvos como `fichamento_<autor>_<ano>.md`, ou dentro de uma pasta `fichamentos/` se ela existir.

## Estrutura do repositório

```text
fichamento-academico/
├── SKILL.md                         instruções que o Claude segue
├── references/
│   ├── template.md                  modelo de saída do fichamento
│   └── formatos-referencia.md       regras ABNT e APA para cada tipo de obra
└── scripts/
    └── extract_pages.py             extração de texto do PDF por página
```

O script também funciona sozinho:

```bash
python extract_pages.py artigo.pdf > artigo.txt
```

## Limitações

- A detecção da numeração impressa depende do layout do PDF. Quando falha, a skill cita pelo índice físico e avisa no frontmatter.
- Texto em duas colunas pode sair com a ordem das linhas alterada. A skill é instruída a conferir no PDF os trechos duvidosos.
- O parecer crítico é uma leitura assistida, não substitui a sua avaliação do artigo.

## Contribuições

Sugestões e correções são bem-vindas por issue ou pull request, principalmente sobre regras ABNT e APA e sobre PDFs em que a detecção de páginas falha.

## Licença

[MIT](LICENSE)
