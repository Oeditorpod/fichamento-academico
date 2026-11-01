# Fichamento Acadêmico Rigoroso

Plugin para o [Claude Code](https://claude.com/claude-code) que transforma as referências de uma pesquisa (artigos, teses, leis, relatórios, notícias, livros) em fichamentos de nível de pós-graduação, com a página ou o artigo de lei de cada afirmação.

Feito para quem escreve dissertação, tese ou artigo e usa os fichamentos como banco de dados confiável na hora de redigir.

## As skills

| Skill | Para quê |
| --- | --- |
| `fichamento` | Porta de entrada. Recebe arquivos ou uma pasta, identifica o tipo de cada documento, mostra a tabela arquivo, tipo e skill, procura fichamentos já existentes, encaminha cada arquivo e gera o índice com pendências. |
| `fichar-artigo` | Artigo, tese, dissertação, preprint: anatomia metodológica com página. |
| `fichar-norma` | Lei, decreto, instrução normativa, regulamento da UE, projeto de lei: objeto, definições, obrigações, prazos, sanções e órgão executor, citados por artigo. |
| `fichar-relatorio` | Relatório, nota técnica, notícia, página web, infográfico: quem produziu, de onde vem cada número, confiabilidade. |
| `fichar-livro` | Livro e capítulo, organizado por capítulo, com os conceitos do autor. |
| `conferir-citacoes` | Confere as citações de fichamentos prontos contra o original e propõe correções. |

Na maior parte do tempo basta pedir em linguagem natural; a skill `fichamento` escolhe as outras.

## O que cada fichamento traz

1. Frontmatter YAML (Obsidian, Notion, Zotero), com tipo, paginação e status da leitura.
2. Referência em ABNT NBR 6023:2018 e APA 7.
3. **Status da leitura**: lido por inteiro, parcial (com o motivo), por capítulos, via OCR ou não lido.
4. Conteúdo do documento, com página ou artigo em cada afirmação. O que muda por tipo está na tabela acima.
5. **Conceitos, dados e definições**: os números e termos que se procura na hora de escrever.
6. **Citações** em tabela: página, trecho literal no idioma original, tradução ou paráfrase, onde usar; abaixo, cada uma pronta para colar no texto em ABNT.
7. **Como citar no texto**: uma frase-modelo neutra e, se você informou o tema da pesquisa, frases voltadas a ele.
8. **Parecer crítico**, separado do relato.

## Por que confiar nas páginas

- O texto é extraído página a página. Livros escaneados com duas páginas por folha são divididos e numerados; texto em duas colunas é posto na ordem de leitura; a numeração impressa é lida, inclusive quando anexos recomeçam do 1.
- Quando a numeração não pode ser confirmada, o fichamento avisa com o nome do arquivo, a pasta e a estimativa, e o índice lista a pendência.
- Antes de entregar, cada citação é procurada no texto do documento. O script diz se a página (ou o artigo de lei) bate.
- Nada de página, DOI, número ou autor que não tenha sido lido no documento. Na falta, o fichamento escreve `[página não identificada]`.

Mesmo assim, confira no original as citações que forem para um texto de banca ou periódico.

## Requisitos

- Claude Code (aplicativo desktop, terminal ou extensão de IDE).
- Python 3.9 ou mais recente.
- Pacotes Python:

| Pacote | Para quê | Obrigatório |
| --- | --- | --- |
| `pymupdf` | PDF: texto, páginas duplas, imagens de conferência | sim |
| `pdfplumber` | tabelas de PDF | não |
| `openpyxl` | tabelas exportadas para planilha | não |
| `python-docx` | DOCX | não |
| `ebooklib` e `beautifulsoup4` | EPUB e HTML | não |
| `ocrmypdf` | PDF escaneado (OCR) | não |

```bash
pip install pymupdf pdfplumber openpyxl python-docx ebooklib beautifulsoup4
```

- Para PDF escaneado sem texto, além do `ocrmypdf`: [Tesseract](https://github.com/tesseract-ocr/tesseract) com o pacote de português e [Ghostscript](https://ghostscript.com/). Sem eles, esses arquivos saem marcados como "não lido", com o motivo.

Para ver o que já está instalado (o script só verifica, não instala nada):

```bash
python shared/scripts/verificar_requisitos.py
```

Não use `python -I` nesse comando: o modo isolado esconde pacotes instalados na pasta do usuário.

## Instalação

Dentro de uma sessão do Claude Code, rode uma vez:

```text
/plugin marketplace add Oeditorpod/fichamento-academico
```

```text
/plugin install fichamento-academico@fichamento-academico
```

Pelo terminal, sem abrir uma sessão:

```bash
claude plugin marketplace add Oeditorpod/fichamento-academico
claude plugin install fichamento-academico@fichamento-academico
```

Se o seu computador não tem chave SSH cadastrada no GitHub e a instalação falhar, defina a variável `CLAUDE_CODE_PLUGIN_PREFER_HTTPS=1` e tente de novo.

## Atualizações automáticas

O Claude Code deixa a atualização automática desligada para marketplaces de terceiros. Para ligar:

1. Rode `/plugin` numa sessão do Claude Code.
2. Abra a aba **Marketplaces** e selecione `fichamento-academico`.
3. Escolha **Enable auto-update**.

Para atualizar à mão:

```text
/plugin marketplace update fichamento-academico
```

Você só recebe uma atualização quando a versão muda. A lista de mudanças está em [CHANGELOG.md](CHANGELOG.md) e o porquê de cada versão, no fim desta página.

## Como usar

Abra o Claude Code na pasta da pesquisa e peça:

- "Ficha todos os arquivos da pasta `referencias`"
- "Ficha `artigos/silva_2024.pdf` e `leis/Lei_12651.pdf`"
- "Tira as citações com página desse livro, só os capítulos 2 e 3"
- "Confere as citações dos fichamentos da pasta `fichamentos`"

Ou chame direto:

```text
/fichamento-academico:fichamento referencias/
```

Em lote, antes de começar, a skill mostra uma tabela com cada arquivo, o tipo identificado, a skill que vai usar e se já existe fichamento dele. Você confirma ou corrige. Arquivos com fichamento existente são **completados** em arquivo novo, com registro do que mudou; o original não é sobrescrito. Também dá para escolher refazer ou pular.

Ao final, `_indice.md` lista todos os fichamentos com o status de leitura, as pendências (paginação a conferir, referências a decidir, leitura parcial) e os arquivos que ficaram de fora e por quê.

A skill lê exatamente o que você pedir: a pasta inteira, com subpastas, ou só os arquivos nomeados.

## Estrutura do repositório

```text
fichamento-academico/
├── .claude-plugin/
│   ├── marketplace.json             catálogo lido pelo /plugin
│   └── plugin.json                  nome e versão do plugin
├── skills/
│   ├── fichamento/SKILL.md          porta de entrada, lote e índice
│   ├── fichar-artigo/               SKILL.md e references/template.md
│   ├── fichar-norma/                SKILL.md e references/template.md
│   ├── fichar-relatorio/            SKILL.md e references/template.md
│   ├── fichar-livro/                SKILL.md e references/template.md
│   └── conferir-citacoes/SKILL.md
├── shared/
│   ├── references/
│   │   ├── secoes-comuns.md         status, conceitos, citações, como citar, parecer
│   │   ├── fluxo-comum.md           passos comuns às skills por tipo
│   │   ├── leitura-em-blocos.md     escopo de leitura e documentos longos
│   │   └── formatos-referencia.md   ABNT e APA por tipo de obra
│   └── scripts/
│       ├── extract_pages.py         PDF por página (duplas, colunas, numeração)
│       ├── extract_other.py         DOCX, EPUB, HTML, TXT, imagem, PDF escaneado
│       ├── find_quote_page.py       conferência de citações
│       └── verificar_requisitos.py  o que falta instalar
├── CHANGELOG.md
├── LICENSE
└── README.md
```

Os scripts funcionam sozinhos:

```bash
python shared/scripts/extract_pages.py livro.pdf --saida livro.txt --amostra amostras/
python shared/scripts/find_quote_page.py fichamento.md livro.txt
```

## Limitações

- A numeração impressa depende do layout. Quando não dá para confirmar, a página é estimada e o fichamento avisa.
- Duas colunas são detectadas por página; layouts muito irregulares (caixas, notas laterais) podem sair fora de ordem. A conferência de citações acusa esses casos.
- OCR depende da qualidade do escaneamento; páginas de baixa confiança são indicadas.
- A redação em vigor de uma norma só é afirmada se o documento lido mostrar. Alterações posteriores não são buscadas na internet.
- O parecer crítico é uma leitura assistida, não substitui a sua avaliação.

## Contribuições

Sugestões e correções são bem-vindas por issue ou pull request, principalmente sobre regras ABNT e APA e sobre PDFs em que a detecção de páginas falha.

## Licença

[MIT](LICENSE)

## Histórico de versões

Esta seção explica por que cada versão mudou, para quem chegar agora entender como o plugin chegou ao estado atual. A lista detalhada do que mudou está no [CHANGELOG](CHANGELOG.md).

### 2.0.0 (novembro de 2026): um plugin com uma skill por tipo de documento

**Por que mudou.** A versão 1.0.0 foi usada para refazer os 65 fichamentos das referências de um trabalho de mestrado (artigos, leis, relatórios e livros). A comparação com os fichamentos feitos antes, à mão e com orientação passo a passo, mostrou que os da skill saíam menos completos: cerca de metade do texto, menos referências de página e sem as seções que o autor mais usava na hora de escrever. Ficaram claros seis problemas:

1. **Um modelo só para tudo.** O modelo era de artigo científico. Em lei, "desenho metodológico" não faz sentido; em relatório, o que importa é quem produziu e de onde vem cada número; em livro, o capítulo. Daí a divisão em skills por tipo, com uma porta de entrada que escolhe sozinha.
2. **Faltavam seções úteis na redação.** "Conceitos, dados e definições" e "Como citar no texto" existiam nos fichamentos manuais e não no modelo. Voltaram, e a tabela de citações ganhou a linha pronta para o texto. Quando o tema da pesquisa não é informado, as frases saem neutras, sem parar o trabalho para perguntar.
3. **Documentos longos.** Ler tudo de uma vez fazia escapar detalhes em relatórios e normas grandes. Agora a leitura é em blocos de cerca de 40 páginas, cada um com ficha parcial, consolidadas no fim. Artigos, normas e relatórios são sempre lidos inteiros; livros, por capítulo.
4. **Páginas erradas.** O script antigo errava em livros escaneados com duas páginas por folha, em texto de duas colunas e em anexos que recomeçam a numeração. Foi reescrito e testado nesses casos. Quando a numeração não pode ser confirmada, o fichamento avisa com o arquivo, a pasta e a estimativa, em vez de errar calado.
5. **Não ficava claro o que não foi lido.** Cada fichamento passou a ter status de leitura com o motivo, o índice lista pendências e arquivos de fora, e um script diz o que falta instalar para cada formato (DOCX, EPUB, HTML, PDF escaneado).
6. **Retrabalho.** Rodar de novo numa pasta com fichamentos prontos criava duplicatas ou corria o risco de apagar trabalho anterior. Agora a skill procura fichamentos existentes e, por padrão, os completa em arquivo novo, com registro do que mudou.

Também entrou a conferência automática de citações: cada trecho literal é procurado no texto do documento, por página ou por artigo de lei.

### 1.0.0 (outubro de 2026): primeira versão

Uma skill única, `fichamento-academico`, pensada para artigos científicos em PDF: referência ABNT e APA, anatomia metodológica, tabela de 5 a 10 citações literais com página e parecer crítico separado do relato. Já trazia a regra central, que continua valendo: nenhuma página, DOI ou número entra no fichamento sem ter sido lido no documento.
