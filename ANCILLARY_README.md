# Ancillary materials

Version: 1.1  
Date: August 4, 2026

These files support the arXiv preprint *Known Good, Known Bad: A Ground-Truth Calibration Protocol for AI Judgment in Science*.

## Contents

- `data/pilot_outcomes.csv`: descriptive outcome matrix for the six pilot conversations.
- `data/pilot_coding_ledger.csv`: response-level primary outcomes, secondary
  markers, evidence locators, coder role, and blinding status.
- `protocol/benchmark_protocol.md`: calibration triad, outcome definitions, codebook, and proposed factorial extension.
- `protocol/case_cards.jsonl`: machine-readable verified-reference and reference-deviant case cards.
- `protocol/essentials_prompt_ladder_protocol.md`: blank documentary-verification instrument.
- `raw_transcripts/`: extracted instructor-generated response records and
  their manifest. Exact prompts are preserved in the protocol and case cards.
- `code/generate_figures.py`: deterministic figure-generation script.

## Evidence scope

The dataset consists exclusively of researcher-authored prompts and public-interface AI outputs. The six conversations provide one run per condition and support trace-level descriptive analysis. The access record identifies the free logged-out ChatGPT web interface and collection period in July 2026; a stable backend identifier and random seed were unavailable.

The extracted response text is preserved verbatim. The case cards, protocol,
outcome matrix, coding ledger, and figures provide the versioned adjudication
record.
