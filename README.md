# Freeze, guard, null, amend

Working repository for the Hypneum Lab methods note:

> *Freeze, guard, null, amend: what a one-person open lab learned from
> preregistering computational experiments with AI-agent assistance.*

Target: arXiv (cs.LG, cross-listed stat.ME) before 2026-12-15, then the
Journal of Trial and Error (JOTE) in January 2027.

## Layout

- `docs/plan-2026-10-31.md` — detailed plan validated by the PI on 2026-10-31 (French).
- `paper/manuscript.md` — manuscript skeleton (English); every planned paragraph carries a `TODO:` line.
- `paper/figures/`, `paper/tables/` — to come.

## Scope

The note describes an executable preregistration chain (annotated tag +
SHA-256 manifest + Software Heritage identifier, launch guards, calibrated
paired nulls, dated amendments), its cost, its observed failure modes and
the full set of errata it produced. It makes no scientific claim about the
experiments themselves.

## Case-study rule

All preregistered verdicts rendered between 2026-10-30 00:00 CET and
2026-10-31 12:00 CET, without exception: M5 certify (FAILED), NH-01
(bit-exact replication; "not computable" at m = 0.30), NH-03 deferred
(recency survives) and the Lie/Strang declared deviation.

## Authorship and tooling

Author: Clément Saillant (Hypneum Lab). The note names every agent used in
the programme (models, versions, sessions and their roles); see the
manuscript's human-agent setup section.

## AI assistance (transparency)

This repository is developed by a one-person lab with AI assistants
used as tools, never as authors:

- **Claude Code (Anthropic)** assists with code, documentation,
  operations and literature search in interactive sessions driven by
  the PI.
- **Codex CLI (OpenAI, `gpt-6.1-sol` / `gpt-6-astra`)** runs
  independent review passes before a release, a pre-registration or a
  submission; the briefs, reports and verdict tables are published next
  to the reviewed material whenever a pass is run.

Every scientific claim, verdict and pre-registration decision is taken
by the PI; results are reproduced by the test suite and CI, and review
reports are evidence, not endorsements. No model is listed as a
co-author of a publication or as a co-author of a commit.

## License

Text and figures: CC BY 4.0. Code snippets: MIT.
