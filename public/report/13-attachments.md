## 13. Original source attachments and validation manifest

### [file:2349] ARPD-Codebook.pdf

User-provided original; extractable from embedded data.

### [file:2350] AutocraticRulingPartiesDataset.xlsx

User-provided original; extractable from embedded data.

```text
{
  "deliverable": "C",
  "title": "China supremacy-loss calculation: reconstruction, corrections, evidence and reproducibility audit",
  "version": "1.0",
  "assessment_date": "2026-11-24",
  "historical_cutoff": "End 2015; censoring coordinate 2016",
  "source_codebook": "Michael K. Miller, October 2019 Version 1.0",
  "environment": {
    "python": "3.12.14",
    "numpy": "1.26.4",
    "pandas": "2.2.3",
    "scipy": "1.13.1"
  },
  "bootstrap": {
    "root_seed": 20261124,
    "streams_per_version": 6,
    "stream_order": [
      "continuous All",
      "continuous Revolutionary",
      "continuous Marxist Revolutionary",
      "split2004 All",
      "split2004 Revolutionary",
      "split2004 Marxist Revolutionary"
    ],
    "replicates_per_cell": 2000,
    "versions": 2,
    "attempts": 24000,
    "successes": 24000,
    "unit": "normalized country name, not ccode"
  },
  "joint": {
    "combinations_per_version": 972,
    "versions": 2,
    "fit_rows": 5832
  },
  "table_row_counts": {
    "primary_fits": 24,
    "bootstrap_summary": 12,
    "bootstrap_replicates": 24000,
    "joint_coding_summary": 6,
    "joint_coding_results": 5832,
    "alternative_families": 72,
    "likelihood_profiles": 18,
    "one_change_sensitivity": 360,
    "age60_diagnostic": 3,
    "age60_records": 18,
    "selected_record_influence": 36,
    "identical_fit_tail_constructions": 24,
    "china_bridge": 54,
    "bridge_thresholds": 6,
    "strict_rule_stress_test": 24,
    "likelihood_quadrature_checks": 18,
    "documentary_adjudications": 15,
    "source_register": 32,
    "records_ARPD_benchmark": 277,
    "records_Earlier_Vietnam_correction": 276,
    "records_Frozen_continuous": 269,
    "records_Frozen_2004": 270,
    "records_Frozen_2009": 270,
    "records_Corrected_continuous": 267,
    "records_Corrected_2004": 268,
    "records_Corrected_2009": 268,
    "original_source_rows": 479
  },
  "source_hashes": {
    "AutocraticRulingPartiesDataset.xlsx": "950233bab0a86d919944fe7198c650f842c20d5048083a8a1e2216f93344a18e",
    "ARPD-Codebook.pdf": "5259135ed641c6529bc5df1017ba9bbe6bdc25947a40915c9d403d7d5d33b4f0"
  },
  "reproduction_sha256": "77c8af649046a4781d0d07edcc752dec59405037ac1987d87ae2b1247ce18a77",
  "frozen_bridge_comparison": {
    "max_abs_eventual": 0.0,
    "max_abs_horizon": 0.0
  },
  "quadrature_max_abs_NLL_difference": 2.2737367544323206e-13,
  "tail_max_abs_NLL_difference": 2.2737367544323206e-13,
  "tail_max_abs_target_error": 1.0697220886868308e-11,
  "provenance": "Source spreadsheet and codebook embedded as exact supplied binaries. Numerical outputs regenerated. Python is a functionally faithful transcription with explicit corrected extension, not byte-identical recovered original script. Sources distinguish named China evidence from newly recovered historical corroboration. Hosted archive not ingested."
}
```
