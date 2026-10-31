# 4. Errata: what the chain corrected, and what found it

An erratum here is one corrected claim: a sentence, a number or a
verdict that a committed document stated and that a later committed
document withdrew or qualified. The unit is the claim, not the file.
One erratum file in kiki-flow-research (`ERRATUM.md`, 943 lines, first
commit `01cefe4` on 2026-10-24, last `cd61610` on 2026-10-29) carries
eleven of the rows below; one architecture decision record in
bouba_sens carries one. Counting files would make the first repository
look better than the second. Counting claims does not.

Table 2 lists every corrected claim found in the five repositories plus
baby-brain on 2026-10-31. Each row points to the commit or tag that
carries the correction. "Detected by" names the mechanism, not the
person: *agent review* is a code agent reading code in a review pass,
*external review* is the Codex cross-review of 2026-10-25 (section 0),
*null* is a calibrated or paired null, *replication* is a rerun or
recount, *audit* is a documentation pass by the PI. "Cost" is the
compute or the PI's time spent on the correction when a document
records it; "n/r" means not recorded. "Open" means the correction is
not finished on 2026-10-31.

*Table 2. Corrected claims, one per line, 2026-04 to 2026-10-31.*

| # | Repository | Date | Corrected claim | Root cause | Detected by | Correction (commit / tag) | Cost | Open |
|---|---|---|---|---|---|---|---|---|
| 1 | kiki-flow-research | 2026-06-04 | `prox_w2` used the reference measure passed to it (D1) | parameter accepted and ignored since 2026-04-17 | agent review | `ffee5d9`; `ERRATUM.md` §1 | n/r | no |
| 2 | kiki-flow-research | 2026-10-24 | the MLX port computed the same flow as the numpy path (D2) | port diverged from 2026-04-18 without a parity test | agent review | PR #16; `ERRATUM.md` §1 | n/r | no |
| 3 | kiki-flow-research | 2026-10-24 | the entropic parameter ε was varied in the reported sweeps | ε accepted by the CLI and never forwarded | agent review, confirmed by external review 2026-10-25 | `ERRATUM.md` §9 (fix 2026-10-24) | n/r | no |
| 4 | kiki-flow-research | 2026-10-25 | `max_iter` bounded the inner solver in the reported runs | parameter ignored | agent review | `ERRATUM.md` §10 | n/r | no |
| 5 | kiki-flow-research | 2026-10-24 | Figure 1 showed a trajectory | one point repeated; plot of a constant | audit | `ERRATUM.md` §5 | n/r | no |
| 6 | kiki-flow-research | 2026-10-24 | entropies reported in bits | computed in nats, labelled bits | audit | `ERRATUM.md` §5 | n/r | no |
| 7 | kiki-flow-research | 2026-10-24 | README status reflected the JKO results | JKO results never fed back; stale status and provenance timestamps | audit | `ERRATUM.md` §5 | n/r | no |
| 8 | kiki-flow-research | 2026-10-24 | the Zenodo record 19666756 was the lab's archived release | wrong record exposed publicly | audit | `ERRATUM.md` §6; records 23619954 and 23636477 | n/r | no |
| 9 | kiki-flow-research | 2026-10-27 | the "rigorous path" was a JKO step | identification error between a proximal step and a JKO step | agent review | `ERRATUM.md` §12 | n/r | no |
| 10 | kiki-flow-research | 2026-10-27 | the strong-Turing claim (dissipative slow step) held for γ ≥ 10 | the slow step is not dissipative at γ ≥ 10; claim withdrawn | replication under tag `prereg-turing-strong-20261026` | `ERRATUM.md` §14; `docs/prereg/2026-10-26-turing-strong-excess.md` | one registered run | no |
| 11 | kiki-flow-research | 2026-10-29 | PR #50 closed the implicit-default issue | insufficient fix; status PROPOSED | agent review | `ERRATUM.md` §15–16 | n/r | **yes** |
| 12 | micro-kiki | 2026-10-25 | 0.032 mJ per token and 91.6× energy ratio were measured on the target | analytical estimate presented as a measurement | external review | `docs/ERRATA.md` E-01; measurement is NH-81 (issue #14) | six freeze tags, NH-81 campaign | **yes** (NH-81 running) |
| 13 | micro-kiki | 2026-10-25 | C5 accuracy bound 0.911 (MK-23 "confirmed") | summed marginal MI (150.74 bits) used as joint MI | external review | `docs/ERRATA.md` E-02; MK-23 requalified refuted; `estimate_mi_bits` rewritten with a Ross k-NN joint estimator and H(Y) cap | n/r | **yes** (recompute `results/c5-info-bound.json`) |
| 14 | micro-kiki | 2026-10-25 | router accuracy 70.7 % / 89.5 % | not reproducible from the repository; printed merge map did not match the code | replication | `docs/ERRATA.md` E-03; values 46.4 % / 69.6 % (`10c7b6e`) | n/r | no |
| 15 | bouba_sens | 2026-10-23 | the three SNR cells (`floor`, `minus10`, `plus10`) were distinct severities | SNR floors nearly identical under default settings, at most 0.6 dB apart; ramp 1.98 % | audit | ADR-0020 (`784b4ca`) | n/r | no |
| 16 | bouba_sens | 2026-10-26 | the default regime learned the task | default regime at chance (0.25) | null (learning gate) | ADR-0024 (`9a510ae`); straight-through emission added opt-in | n/r | no |
| 17 | bouba_sens | 2026-10-30 | train, lesion and eval rebuilt the same world | world seed differs between the three phases | agent review | ADR-0027 (`1295160`, `02c2407`); `--world-seed-mode cell` opt-in, default unchanged | n/r | no |
| 18 | bouba_sens | 2026-10-25 | B-3 passed at threshold 0.02 | threshold chosen without a null; null expectation 0.10–0.17 | external review, then paired null | `scripts/me6_paired_null.py`; tag `prereg-b3-probe-v2-20261025` | one day of writing, seconds of compute | no |
| 19 | bouba_sens | 2026-10-25 | 25/25 false positives rejected by the C+ control | result inverted in the report | external review | report corrected 2026-10-25 (to verify: commit) | n/r | no |
| 20 | dream-of-kiki | 2026-10-28 | power 0.74 for G4 and G5-bis | value copied after the significance level changed; six locked sentences | audit | `42bc6bb` | n/r | no |
| 21 | nerve-wml | 2026-10-24 | the L1a learnability gate passed | condition 3 never evaluated; 13.1 % above the 10 % bound; the `@slow` test ran outside CI | agent review | `608e6d9`, `a3810cc` | n/r | no |
| 22 | nerve-wml | 2026-10-24 | v1.9.0 archived on Zenodo | no deposit made | audit | same erratum as row 21 | n/r | to verify |
| 23 | nerve-wml | 2026-10-25 | the N-3 ablations ablated consolidation | `n_received` 0 and `apply_consolidation` false: consolidation never applied in the ablated arms | agent review | `17caed5`, Erratum 1 | n/r | no |
| 24 | nerve-wml | 2026-10-25 | direction stability 15/15 (Paper 1) | stale after the v1.7.0 recount | audit (issue #64) | `17caed5`, Erratum 2a; 19/20 | figures still to re-render | **yes** |
| 25 | nerve-wml | 2026-10-25 | N = 2 row: 1 seed, 10.71 % | five-seed rerun existed and was not used | audit | `17caed5`, Erratum 2b; 4/5 seeds | n/r | no |
| 26 | nerve-wml | 2026-10-25 | "all experiments use N = 4" | polymorphism law measured at N ∈ {16, 32, 64} | audit | `17caed5`, Erratum 2c | n/r | no |
| 27 | nerve-wml | 2026-10-25 | transformer pool scale "not measured" | measured (v1.1.4) but the section was not updated; no per-seed JSON archived | audit | `17caed5`, Erratum 2d | re-run of 5 seeds left to the PI | **yes** |
| 28 | nerve-wml | 2026-10-25 | Loihi 2 via `lava-nc` was a deployment path | `lava-nc` archived; nothing ever compiled | audit (GitHub API check) | `17caed5`, Erratum 2e; stub states the archival | n/r | no |
| 29 | baby-brain | 2026-10-25 | gate 1a (learning progress) passed | documentation written ahead of results; refuted on the data | external review | `ba8aa81` | n/r | no |
| 30 | baby-brain | 2026-10-25 | gate 1b passed | same | external review | `ba8aa81` | n/r | no |
| 31 | baby-brain | 2026-10-25 | gate 1c passed | inconclusive on the data | external review | `ba8aa81` | n/r | no |

Thirty-one corrected claims, five repositories plus one, five formats:
a numbered `ERRATUM.md`, a dated-ID `ERRATA.md`, architecture decision
records, OSF erratum notes, and milestone documents with numbered
errata. Twenty-eight of thirty-one are dated between 2026-10-23 and
2026-10-30. That concentration is not a burst of errors; it is the week
the lab started reading.

## 4.1 Cross-reading: who found what

Sorting the "detected by" column gives the distribution a reader would
not guess from the chain alone.

- **Audit by the PI** found the largest share (rows 5–8, 15, 20, 22,
  24–28: thirteen claims). These are stale sentences: a number recounted
  but not propagated, a figure re-rendered but not committed, a
  deployment path that no longer existed. No tool found them; a person
  reading the paper against the repository did.
- **Agent review** found the silent parameters (rows 1–4, 9, 11, 17,
  21, 23: nine claims). Every one of them is a function that accepted
  an argument and did nothing with it, or a condition that was never
  evaluated. These are the errors agents are good at finding and good at
  making.
- **External review** (the Codex cross-review of 2026-10-25) found the
  statistical claims (rows 12, 13, 18, 19, 29–31: seven claims): an
  estimate presented as a measurement, a marginal sum presented as a
  joint quantity, a threshold without a null, an inverted control, three
  gates documented before their data. One reviewer in one day withdrew
  more verdicts than the chain had produced.
- **Nulls and replications** found two (rows 10, 16) and confirmed one
  (row 18). This is the smallest category, and it is the one the chain
  was built to grow.

The reading is uncomfortable and it is the reason this note exists:
the chain of section 3 prevents a class of error (the unregistered run,
the moved threshold, the silently edited protocol) that the table
barely contains, because the chain was in place for the week the table
covers. What the table contains are the errors of the six months
before, found in the week the chain forced a reading. Whether the chain
reduces the next table is the claim this note cannot yet make.

## 4.2 The never-rewrite rule

Every correction in Table 2 is a new committed text that points at the
old one. The old text is not deleted; it receives a status line and a
link. The rule has three consequences that the table shows.

A correction can be wrong. Row 11 is a correction (PR #50) that a later
reading found insufficient; the erratum file records the first
correction, the finding, and the proposed second one, each dated. Had
the first been applied in place, the second would have had nothing to
point at.

A correction can be partial. Row 24 corrected the text and left the
committed figure files with the old title; the erratum says so and
names the command that re-renders them. Row 27 corrected the sentence
and recorded that the per-seed data behind it were never archived. A
rewrite would have hidden both gaps.

A correction has a reader. The micro-kiki E-01 erratum keeps the
analytical script and its artefact "as a record of the estimate, not as
evidence". A reader of the original claim can follow it to the
withdrawal and to the campaign (NH-81) that replaces the estimate with
a measurement, and can see, on 2026-10-31, that the measurement is not
done.

The rule costs disk and attention. The kiki-flow-research erratum file
is longer than most of the papers it corrects. The alternative, a clean
document with no history, is what the lab had on 2026-10-22, and Table 2
is what it cost.
