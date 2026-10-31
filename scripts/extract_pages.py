"""Extrai o texto de um PDF página a página, marcando índice físico e página impressa.

Uso:
    python -I extract_pages.py artigo.pdf [> artigo.txt]

Cada página sai precedida de um cabeçalho:
    ===== PÁGINA FÍSICA 3 | IMPRESSA: 214 =====
Quando a numeração impressa não é detectada, aparece "IMPRESSA: ?".
A detecção procura um número isolado nas primeiras e últimas linhas da página
e verifica se a sequência entre páginas é consistente (passo de 1).
"""
import re
import sys
from pathlib import Path

try:
    import pymupdf
except ImportError:  # versões antigas
    import fitz as pymupdf  # type: ignore


def candidate_numbers(lines):
    """Números isolados nas bordas da página (até 3 linhas de cada lado)."""
    edge = lines[:3] + lines[-3:]
    nums = []
    for ln in edge:
        s = ln.strip()
        m = re.fullmatch(r"(?:p\.?\s*|page\s*|página\s*)?(\d{1,4})", s, flags=re.I)
        if m:
            nums.append(int(m.group(1)))
            continue
        # padrões como "214  Nome do periódico" ou "Autor et al.   215"
        m = re.match(r"^(\d{1,4})\s{2,}\S", s) or re.search(r"\S\s{2,}(\d{1,4})$", s)
        if m:
            nums.append(int(m.group(1)))
    return nums


def infer_offset(per_page_candidates):
    """Acha o deslocamento (impressa - física) mais votado entre páginas."""
    votes = {}
    for phys, cands in enumerate(per_page_candidates, start=1):
        for c in cands:
            votes[c - phys] = votes.get(c - phys, 0) + 1
    if not votes:
        return None
    best, count = max(votes.items(), key=lambda kv: kv[1])
    # exige pelo menos duas páginas concordando para evitar falso positivo
    return best if count >= 2 else None


def dehyphenate(text):
    # hífen suave (U+00AD) usado por editoras como Springer nas quebras de linha
    text = re.sub(r"­\s*\n\s*", "", text)
    text = text.replace("­", "")
    return re.sub(r"(\w)-\n(\w)", r"\1\2", text)


def main():
    # Windows usa cp1252 por padrão no stdout; força UTF-8 para preservar acentos
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except AttributeError:
        pass
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    path = Path(sys.argv[1])
    doc = pymupdf.open(path)
    pages = []
    cands = []
    for page in doc:
        text = page.get_text("text")
        lines = [l for l in text.splitlines() if l.strip()]
        pages.append(text)
        cands.append(candidate_numbers(lines))

    offset = infer_offset(cands)
    meta = doc.metadata or {}
    print(f"# ARQUIVO: {path.name}")
    print(f"# PÁGINAS FÍSICAS: {len(pages)}")
    print(f"# TÍTULO (metadado): {meta.get('title') or '?'}")
    print(f"# AUTOR (metadado): {meta.get('author') or '?'}")
    if offset is None:
        print("# NUMERAÇÃO IMPRESSA: não detectada; cite pelo índice físico e registre paginacao: fisica")
    else:
        print(f"# NUMERAÇÃO IMPRESSA: detectada (impressa = física {offset:+d})")
    print()

    for i, text in enumerate(pages, start=1):
        printed = "?" if offset is None else str(i + offset)
        print(f"===== PÁGINA FÍSICA {i} | IMPRESSA: {printed} =====")
        print(dehyphenate(text).rstrip())
        print()

    if sum(len(t.strip()) for t in pages) < 200:
        print("# AVISO: quase nenhum texto extraído. PDF provavelmente escaneado (imagem). Precisa de OCR.")


if __name__ == "__main__":
    main()
