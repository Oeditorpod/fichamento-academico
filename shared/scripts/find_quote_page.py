"""Confere as citações de um fichamento contra o texto extraído do documento.

Uso:
    python find_quote_page.py fichamento.md texto_extraido.txt [--saida relatorio.md]
    python find_quote_page.py --trecho "texto da citação" texto_extraido.txt

O texto extraído é a saída do extract_pages.py ou do extract_other.py.
O script lê as citações entre aspas da tabela de citações do fichamento
(linhas que começam com "| **p." ou "| **art."), procura cada uma no texto,
ignorando quebras de linha, hifenização e espaços, e diz em que página (ou
seção) ela está.

Resultado por citação:
- OK: achada na página indicada no fichamento.
- PÁGINA DIVERGE: achada, mas em outra página (mostra a certa).
- NÃO ACHADA: não está no texto como foi transcrita (conferir no PDF;
  pode ser erro de transcrição ou de extração).
- PARCIAL: só o início da citação foi achado.
"""
import argparse
import re
import sys
import unicodedata
from pathlib import Path

HDR = re.compile(r"^===== (PÁGINA (\S+)|SEÇÃO: .*|CAPÍTULO .*|TEXTO.*) .*=====$|^===== (.*) =====$", re.M)


def norm(s):
    s = unicodedata.normalize("NFKC", s)
    s = s.replace("­", "")
    s = re.sub(r"-\s*\n\s*", "", s)
    s = s.replace("“", '"').replace("”", '"').replace("’", "'").replace("‘", "'")
    s = s.replace("—", "-").replace("–", "-")
    s = re.sub(r"\s+", " ", s)
    return s.strip().lower()


def build_index(text):
    """Texto normalizado + lista de (posição inicial, rótulo da página)."""
    parts, labels = [], []
    pos = 0
    chunks = re.split(r"^(===== .* =====)$", text, flags=re.M)
    label = "?"
    for c in chunks:
        if c.startswith("===== ") and c.endswith(" ====="):
            m = re.match(r"===== PÁGINA (\S+)", c)
            label = m.group(1) if m else c.strip("= ").split(" | ")[0]
            continue
        n = norm(c)
        if not n:
            continue
        labels.append((pos, label))
        parts.append(n)
        pos += len(n) + 1
    return " ".join(parts), labels


def label_at(labels, idx):
    lab = "?"
    for p, l in labels:
        if p > idx:
            break
        lab = l
    return lab


def find(quote, full, labels):
    q = norm(quote.strip('"“” '))
    q = re.sub(r"\[\s*\.\.\.\s*\]|\[…\]|\.\.\.|…", "\u0000", q)
    pieces = [p.strip() for p in q.split("\u0000") if len(p.strip()) > 8]
    if not pieces:
        return "CURTA", None
    i = full.find(pieces[0])
    if i >= 0:
        ok = all(full.find(p, i) >= 0 for p in pieces[1:])
        return ("ACHADA" if ok else "PARCIAL"), label_at(labels, i)
    head = pieces[0][:60]
    i = full.find(head)
    if i >= 0:
        return "PARCIAL", label_at(labels, i)
    return "NÃO ACHADA", None


def quotes_from_fichamento(md):
    rows = []
    for line in md.splitlines():
        m = re.match(r"^\|\s*\*\*(p\.|art\.)\s*([^*|]+)\*\*\s*\|\s*(.+?)\s*\|", line)
        if not m:
            continue
        cited = m.group(2).strip()
        cell = m.group(3)
        for q in re.findall(r'"([^"]{12,})"', cell) or [cell]:
            rows.append((m.group(1) + " " + cited, q))
    return rows


def same_page(cited, found):
    if found is None:
        return False
    nums = re.findall(r"\d+", cited)
    if not nums:
        return False
    try:
        f = int(re.findall(r"-?\d+", found)[0])
    except (IndexError, ValueError):
        return False
    lo, hi = int(nums[0]), int(nums[-1])
    return lo <= f <= hi or lo - 1 <= f <= hi  # citação que começa no fim da página anterior


def main():
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except AttributeError:
        pass
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("fichamento", nargs="?")
    ap.add_argument("texto")
    ap.add_argument("--trecho")
    ap.add_argument("--saida")
    a = ap.parse_args()
    full, labels = build_index(Path(a.texto).read_text(encoding="utf-8"))

    if a.trecho:
        status, page = find(a.trecho, full, labels)
        print(f"{status}: página {page}" if page else status)
        return

    rows = quotes_from_fichamento(Path(a.fichamento).read_text(encoding="utf-8"))
    out = [f"# Conferência de citações: {Path(a.fichamento).name}", "",
           "| Citada como | Resultado | Página encontrada | Início da citação |", "| --- | --- | --- | --- |"]
    counts = {}
    for cited, q in rows:
        status, page = find(q, full, labels)
        if status == "ACHADA":
            status = "OK" if (cited.startswith("art.") or same_page(cited, page)) else "PÁGINA DIVERGE"
        counts[status] = counts.get(status, 0) + 1
        out.append(f"| {cited} | {status} | {page or '-'} | {q[:60].replace('|', '/')}… |")
    out += ["", "Resumo: " + ", ".join(f"{k}: {v}" for k, v in sorted(counts.items()))]
    text = "\n".join(out)
    if a.saida:
        Path(a.saida).write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
