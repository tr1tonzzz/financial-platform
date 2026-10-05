"""Small DHG development probe; not a general financial statement parser.

prepare: record PDF text and render two pages using a supplied pdftoppm binary.
check: extract selected OCR rows, then compare with the existing manual reference.
Run crawler and probe_ocr.cjs separately; see the Markdown experiment appendix.
"""
import argparse
import hashlib
import importlib.metadata
import json
from pathlib import Path
import platform
import re
import subprocess
import unicodedata

from pypdf import PdfReader


def write(path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2), encoding="utf-8")


def fold(text):
    return "".join(c for c in unicodedata.normalize("NFD", text.lower())
                   if unicodedata.category(c) != "Mn").replace("đ", "d")


def row_values(text, label):
    lines = text.splitlines()
    found = [i for i, line in enumerate(lines) if label in fold(line)]
    if len(found) != 1:
        return {"status": "missing_or_ambiguous", "values": []}
    index = found[0]
    # This sample has two columns and dot-grouped VND amounts. A wrapped
    # LNST label may put both amounts on the following line.
    raw = lines[index]
    tokens = re.findall(r"\(?\d{1,3}(?:\.\d{3}){2,}\)?", raw)
    if not tokens and index + 1 < len(lines):
        raw += "\n" + lines[index + 1]
        tokens = re.findall(r"\(?\d{1,3}(?:\.\d{3}){2,}\)?", raw)
    values = [int(t.strip("()").replace(".", "")) * (-1 if t.startswith("(") else 1)
              for t in tokens]
    return {"status": "candidate" if len(values) == 2 else "needs_review",
            "raw_row": raw, "values": values}


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("mode", choices=["prepare", "check"])
    ap.add_argument("root", type=Path)
    ap.add_argument("--pdftoppm", type=Path)
    args = ap.parse_args()
    root = args.root.resolve()
    if args.mode == "prepare":
        run = json.loads((root / "latest.json").read_text(encoding="utf-8"))
        chosen = next(d for d in run["downloads"] if d["period_candidate"] == "FY-2025")
        pdf = root / chosen["saved_path"]
        reader = PdfReader(pdf)
        texts = [p.extract_text() or "" for p in reader.pages[:12]]
        write(root / "pdf-probe.json", {
            "source_url": chosen["url"], "sha256": hashlib.sha256(pdf.read_bytes()).hexdigest(),
            "pdf_pages": len(reader.pages), "sampled_page_text_chars": [len(t) for t in texts],
            "python": platform.python_version(),
            "versions": {k: importlib.metadata.version(k) for k in ["pypdf", "lxml"]},
            "dpi": 220, "ocr_pages": [10, 11],
        })
        if not args.pdftoppm:
            ap.error("prepare requires --pdftoppm")
        (root / "ocr").mkdir(exist_ok=True)
        subprocess.run([str(args.pdftoppm), "-f", "10", "-l", "11", "-r", "220",
                        "-png", str(pdf), str(root / "ocr/dhg-fy2025")], check=True)
        write(root / "page-jobs.json", [
            {"id": f"dhg-fy2025-p{p}", "image": str(root / f"ocr/dhg-fy2025-{p}.png"),
             "pdf_page": p, "render_dpi": 220} for p in [10, 11]])
        print("Prepared two OCR pages and PDF text evidence.")
        return

    rows = {}
    for name, page, label in [("net_income", 10, "loi nhuan sau thue"),
                              ("reported_cfo", 11, "luu chuyen tien thuan tu hoat dong kinh doanh"),
                              ("fx_adjustment", 11, "chenh lech ty gia hoi doai do danh gia lai")]:
        text = (root / f"ocr/dhg-fy2025-p{page}-ocr.txt").read_text(encoding="utf-8")
        rows[name] = {"pdf_page": page, **row_values(text, label)}
    # Extraction above never sees the reference. Use the reference only to
    # score the six selected cells in this development sample.
    reference = json.loads(Path("docs/research-profit-cash-dividend/evidence/case-dhg-2025.json")
                           .read_text(encoding="utf-8"))
    expected = {"net_income": reference["net_income"], "reported_cfo": reference["reported_cfo"],
                "fx_adjustment": next(r for r in reference["bridge_leaves"] if r["line"] == "04")}
    cells = []
    for name, row in rows.items():
        for i, year in enumerate(["2025", "2024"]):
            actual = row["values"][i] if len(row["values"]) == 2 else None
            target = expected[name][year]
            cells.append({"field": name, "year": year, "expected": target, "actual": actual,
                          "status": "missing" if actual is None else "correct" if actual == target else "wrong"})
    result = {"warning": "Development sample, same-agent manual reference; not independent accuracy. Year/unit/scope mapping reviewed manually.",
              "rows": rows, "cells": cells,
              "counts": {s: sum(c["status"] == s for c in cells) for s in ["correct", "wrong", "missing"]}}
    if all(c["status"] == "correct" for c in cells if c["field"] != "fx_adjustment"):
        ni, cfo = rows["net_income"]["values"], rows["reported_cfo"]["values"]
        result["core_metrics_from_ocr"] = {"net_income_growth_percent": (ni[0]/ni[1]-1)*100,
            "cfo_growth_percent": (cfo[0]/cfo[1]-1)*100,
            "cfo_to_net_income_2025": cfo[0]/ni[0], "cfo_to_net_income_2024": cfo[1]/ni[1]}
    write(root / "comparison.json", result)
    print(json.dumps(result["counts"]))


if __name__ == "__main__":
    main()
