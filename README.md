# Known Good, Known Bad: ground-truth calibration protocol

Public record for:

> Olga Lavinda. *Known Good, Known Bad: A Ground-Truth Calibration Protocol for AI Judgment in Science.* arXiv:2611.11673 (2026). https://arxiv.org/abs/2611.11673

The protocol evaluates a language model on a verified reference case and on variants that each carry one planted deviation. Every conversation follows a fixed three-turn sequence: a neutral evaluation, an authority-framed recheck, and a line-by-line audit. Human adjudication scores four behaviors separately: deviation detection, premise accommodation, unsupported doubt, and correctness of the resulting calculation.

The organic-chemistry pilot comprises six conversations and 18 responses collected through the free logged-out ChatGPT web interface in July 2026. Neutral evaluation detected three of five planted deviations. The two initial misses, oxidant stoichiometry and experimental scale, were detected at the authority-framed turn, and all five detections persisted at the audit turn. In the scale case the model recognized the unit problem and then retained its earlier limiting-reagent conclusion, so detection and numerical repair are scored as separate outcomes.

## Contents

- `protocol/benchmark_protocol.md`: calibration triad, outcome definitions, and behavioral codebook.
- `protocol/case_cards.jsonl`: machine-readable verified-reference and reference-deviant case cards.
- `protocol/pilot_prompt_instructions.md`: intended reference and variant substitutions for the pilot.
- `protocol/essentials_prompt_ladder_protocol.md`: blank documentary-verification instrument.
- `raw_transcripts/`: extracted model responses for the six conversations, with a SHA-256 manifest.
- `data/pilot_outcomes.csv`: outcome matrix by condition and turn.
- `data/pilot_coding_ledger.csv`: response-level outcomes, secondary markers, evidence locators, coder role, and blinding status.
- `code/verify_record.py`: checks response-file integrity, turn-level counts, and the reference arithmetic.
- `PROVENANCE_AND_REVIEW_ADDENDUM.md`: corrections to the historical record. Read it with `READ_FIRST.md` before interpreting the earlier files; it takes precedence where descriptions conflict.

## Verify the record

The check uses only the Python standard library:

```bash
python3 code/verify_record.py
```

## Evidence scope

The dataset contains researcher-authored prompts and public-interface model outputs. It contains no student submissions or educational records. Each condition was run once, which supports trace-level descriptive analysis. A stable backend identifier and random seed were unavailable for the public interface. Replicated model evaluation and learner assessment are the planned next validation steps.

See `DATA_USE_NOTICE.md` for license and reuse terms.
