# Histórico de versões

O porquê de cada versão está no [README](README.md#histórico-de-versões). Aqui fica a lista do que mudou.

## 2.0.1 (2026-11-02)

- Exemplos das regras e modelos trocados por exemplos neutros, sem ligação com um tema de pesquisa específico.

## 2.0.0 (2026-11-01)

Mudanças que quebram o uso anterior:

- A skill `fichamento-academico` deixou de existir. O plugin agora tem seis skills: `fichamento` (porta de entrada), `fichar-artigo`, `fichar-norma`, `fichar-relatorio`, `fichar-livro` e `conferir-citacoes`. Quem chamava `/fichamento-academico:fichamento-academico` passa a chamar `/fichamento-academico:fichamento`.
- Scripts e regras comuns foram para `shared/`.

Novidades:

- Escolha automática da skill por pasta, nome, primeira página e formato, com tabela de confirmação antes do lote.
- Modelos próprios para lei e norma (citação por artigo, redação em vigor), relatório, notícia e infográfico (proveniência dos dados, interesse do produtor) e livro (por capítulo).
- Voltaram as seções "Conceitos, dados e definições" e "Como citar no texto". Citações em tabela com tradução ou paráfrase e linha "pronta para o texto".
- Status de leitura explícito em cada fichamento (integral, parcial, por capítulos, via OCR, não lido) e índice com pendências e arquivos não fichados.
- Fichamento existente: completar (padrão), refazer ou pular; nunca sobrescreve; registro de mudanças no fim.
- Leitura em blocos de cerca de 40 páginas para documentos longos, com fichas parciais consolidadas no fim.
- `extract_pages.py` reescrito: páginas duplas (livros escaneados), duas colunas, numeração impressa com várias sequências (anexos renumerados), aviso quando a numeração precisa ser conferida, imagem de amostra.
- `extract_other.py`: DOCX, EPUB, HTML, TXT e MD, imagens e PDF escaneado via OCR.
- `find_quote_page.py`: confere cada citação no texto extraído, por página ou por artigo de lei.
- `verificar_requisitos.py`: diz o que falta instalar para cada formato, sem instalar nada.
- Referências ABNT e APA para normas estaduais e da União Europeia, páginas web, notícias e EPUB.

## 1.0.0 (2026-10-31)

- Primeira versão distribuída como plugin do Claude Code, com suporte a atualização automática.
- Fichamento com referência ABNT e APA, anatomia metodológica, tabela de citações literais com página e parecer crítico.
- Script de extração de PDF por página, com detecção da numeração impressa e remoção de hífen suave.
