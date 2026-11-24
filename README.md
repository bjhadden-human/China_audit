# C — China supremacy-loss audit

The frozen China calculation is reproducible: 61.383367% eventual loss with continuous Mozambique, or 63.254945% with split-2004. “Approximately 60:40” is coarse rounding, not a third estimate, an average of scenarios, or an additional synthesis. No weights were supplied for combining branches.

This repository publishes one self-contained HTML audit report in two forms:

1. **For people:** the original interactive report at [`public/index.html`](public/index.html), served unchanged as the website.
2. **For AI assistants and search:** the same content split into Markdown, CSV and code files that are small enough to read directly.

## Where to start

- [`public/llms.txt`](public/llms.txt): machine-readable index (also at `/llms.txt` on the website).
- [`public/report.md`](public/report.md): the full report text as one Markdown file.
- [`public/report/`](public/report): the report split into one file per section.

## Report sections

1. [1. Answer and audit conclusion](public/report/01-conclusion.md)
2. [2. Scope, retained inputs and version history](public/report/02-provenance.md)
3. [3. Operational rules and documentary adjudication](public/report/03-rules.md)
4. [4. Historical survival model and estimation](public/report/04-likelihood.md)
5. [5. Frozen China bridge, arithmetic and thresholds](public/report/05-bridge.md)
6. [6. China evidence: support, counterevidence and dependence](public/report/06-evidence.md)
7. [7. Bootstrap, profiles and coding sensitivity](public/report/07-uncertainty.md)
8. [8. Alternative hazard families and old-age diagnostics](public/report/08-families.md)
9. [9. Influence and infinite-tail non-identification](public/report/09-tails.md)
10. [10. Reproduction, embedded data and extraction](public/report/10-repro.md)
11. [11. Justified boundaries and final assessment](public/report/11-limits.md)
12. [12. Source register and evidence locators](public/report/12-sources.md)
13. [13. Original source attachments and validation manifest](public/report/13-attachments.md)

## Data tables

| Table | Rows | CSV size |
|---|---:|---:|
| [`primary_fits`](public/data/primary_fits.csv) | 24 | 4 KB |
| [`bootstrap_summary`](public/data/bootstrap_summary.csv) | 12 | 2 KB |
| [`bootstrap_replicates`](public/data/bootstrap_replicates.csv) | 24,000 | 2,780 KB |
| [`joint_coding_summary`](public/data/joint_coding_summary.csv) | 6 | 1 KB |
| [`joint_coding_results`](public/data/joint_coding_results.csv) | 5,832 | 782 KB |
| [`alternative_families`](public/data/alternative_families.csv) | 72 | 12 KB |
| [`likelihood_profiles`](public/data/likelihood_profiles.csv) | 18 | 2 KB |
| [`one_change_sensitivity`](public/data/one_change_sensitivity.csv) | 360 | 39 KB |
| [`age60_diagnostic`](public/data/age60_diagnostic.csv) | 3 | 0 KB |
| [`age60_records`](public/data/age60_records.csv) | 18 | 2 KB |
| [`selected_record_influence`](public/data/selected_record_influence.csv) | 36 | 4 KB |
| [`identical_fit_tail_constructions`](public/data/identical_fit_tail_constructions.csv) | 24 | 3 KB |
| [`china_bridge`](public/data/china_bridge.csv) | 54 | 11 KB |
| [`bridge_thresholds`](public/data/bridge_thresholds.csv) | 6 | 1 KB |
| [`strict_rule_stress_test`](public/data/strict_rule_stress_test.csv) | 24 | 2 KB |
| [`likelihood_quadrature_checks`](public/data/likelihood_quadrature_checks.csv) | 18 | 1 KB |
| [`documentary_adjudications`](public/data/documentary_adjudications.csv) | 15 | 5 KB |
| [`source_register`](public/data/source_register.csv) | 32 | 12 KB |
| [`records_ARPD_benchmark`](public/data/records_ARPD_benchmark.csv) | 277 | 77 KB |
| [`records_Earlier_Vietnam_correction`](public/data/records_Earlier_Vietnam_correction.csv) | 276 | 77 KB |
| [`records_Frozen_continuous`](public/data/records_Frozen_continuous.csv) | 269 | 75 KB |
| [`records_Frozen_2004`](public/data/records_Frozen_2004.csv) | 270 | 75 KB |
| [`records_Frozen_2009`](public/data/records_Frozen_2009.csv) | 270 | 75 KB |
| [`records_Corrected_continuous`](public/data/records_Corrected_continuous.csv) | 267 | 75 KB |
| [`records_Corrected_2004`](public/data/records_Corrected_2004.csv) | 268 | 75 KB |
| [`records_Corrected_2009`](public/data/records_Corrected_2009.csv) | 268 | 75 KB |
| [`original_source_rows`](public/data/original_source_rows.csv) | 479 | 62 KB |

## Code and sources

- [`public/code/reproduce.py`](public/code/reproduce.py): Python reproduction of the estimates, embedded in the original report.
- [`public/code/frozen_bridge_specification.md`](public/code/frozen_bridge_specification.md): specification of the frozen China bridge.
- [`public/source/`](public/source): the original ARPD spreadsheet and codebook PDF (verified against the SHA-256 hashes in [`public/manifest.json`](public/manifest.json)), plus a page-by-page text version of the codebook.

## Regenerating

Everything except `public/index.html` is generated from it:

```bash
python3 scripts/build_ai_docs.py
```

## Source dataset

The Autocratic Ruling Parties Dataset (ARPD) is by Michael K. Miller. See the codebook for citation guidance: Miller, "The Autocratic Ruling Parties Dataset: Origins, Durability, and Death," *Journal of Conflict Resolution*.
