"""Reproduce selected source arithmetic and check this research pack's links.

Uses only Python's standard library. This is a document/evidence check, not
an application acceptance test or an independent audit of the source PDF.
"""
from collections import defaultdict
from decimal import Decimal
import hashlib
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]
PACK = ROOT / "docs/research-profit-cash-dividend"
case = json.loads((PACK / "evidence/case-dhg-2025.json").read_text(encoding="utf-8"))
checks = []


def check(name, actual, expected):
    checks.append({"name": name, "actual": actual, "expected": expected,
                   "pass": actual == expected})


groups = {}
for year in ("2024", "2025"):
    grouped = defaultdict(int)
    for row in case["bridge_leaves"]:
        grouped[row["group"]] += row[year]
    groups[year] = dict(grouped)
    check(f"{year}: leaf sum equals CFO", sum(grouped.values()), case["reported_cfo"][year])
    check(f"{year}: start and adjustments equal line08",
          grouped["start"] + grouped["adjustments"],
          case["reported_pre_working_capital_subtotal"][year])
check("unique leaf codes", len({r["line"] for r in case["bridge_leaves"]}),
      len(case["bridge_leaves"]))
delta_groups = {g: groups["2025"][g] - groups["2024"][g] for g in groups["2025"]}
check("delta group sum equals delta CFO", sum(delta_groups.values()),
      case["reported_cfo"]["2025"] - case["reported_cfo"]["2024"])
cf = case["cash_flow_totals_2025"]
check("cash flow totals", case["reported_cfo"]["2025"] + cf["cfi"] + cf["cff"], cf["net_cash_flow"])
check("cash rollforward", cf["opening_cash"] + cf["net_cash_flow"] + cf["fx_effect"], cf["closing_cash"])
raw_path = ROOT / case["source_local_path"]
raw_status = "not_available_in_checkout"
if raw_path.exists():
    digest = hashlib.sha256(raw_path.read_bytes()).hexdigest()
    check("source PDF hash", digest, case["expected_sha256"])
    raw_status = "hash_checked; visual review recorded separately"

broken_links = []
md_files = sorted(PACK.glob("*.md"))
for path in md_files:
    text = path.read_text(encoding="utf-8")
    check(f"{path.name}: balanced fences", text.count("```") % 2, 0)
    for target in re.findall(r"\]\(([^)]+)\)", text):
        if target.startswith(("http:", "https:", "#")):
            continue
        target = target.split("#", 1)[0]
        # The result file is written by this script after all checks complete.
        resolved = (path.parent / target).resolve()
        if resolved == (PACK / "evidence/verification.json").resolve():
            continue
        if not resolved.exists():
            broken_links.append({"file": path.name, "target": target})
check("local markdown link targets exist", len(broken_links), 0)


def quotient(a, b):
    return str(Decimal(a) / Decimal(b))


results = {
    "scope": "Selected source arithmetic, existing raw hash, Markdown link/fence checks only",
    "case_id": case["case_id"],
    "raw_status": raw_status,
    "all_checks_pass": all(c["pass"] for c in checks),
    "checks": checks,
    "broken_links": broken_links,
    "group_sums_vnd": groups,
    "group_deltas_vnd": delta_groups,
    "net_income_growth": quotient(case["net_income"]["2025"] - case["net_income"]["2024"], case["net_income"]["2024"]),
    "cfo_growth": quotient(case["reported_cfo"]["2025"] - case["reported_cfo"]["2024"], case["reported_cfo"]["2024"]),
    "cfo_over_net_income": {y: quotient(case["reported_cfo"][y], case["net_income"][y]) for y in ("2024", "2025")},
    "cfo_over_owner_distributions_paid_2025": quotient(case["reported_cfo"]["2025"], abs(case["owner_distributions_paid_signed"]["2025"])),
    "not_verified": ["Mermaid visual rendering", "application implementation", "independent extraction accuracy", "annual dividend completeness"]
}
(PACK / "evidence/verification.json").write_text(json.dumps(results, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps(results, ensure_ascii=False, indent=2))
raise SystemExit(0 if results["all_checks_pass"] else 1)
