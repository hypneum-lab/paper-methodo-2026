# Freeze, guard, null, amend: what a one-person open lab learned from preregistering computational experiments with AI-agent assistance

Clément Saillant — Hypneum Lab[^1]
Draft skeleton, 2026-10-31. Target: arXiv (cs.LG, stat.ME), then Journal of Trial and Error.

[^1]: The research programme is described internally by the descriptive acronym G.E.N.I.A.L.; this note makes no claim about that framework.

## Abstract (draft, ≈150 words)

Preregistration is cheap to promise and expensive to keep when experiments are run by fast, tireless code agents. We describe an executable chain built out of necessity in a one-person, fully open research programme between April and October 2026: an annotated freeze tag with a SHA-256 manifest and a Software Heritage identifier; launch guards that refuse any registered-budget run without that frozen context; calibrated, paired null distributions computed on saved per-item outcomes; and dated amendments for every deviation. Across seven repositories the chain produced at least twenty freeze tags, twelve amendments, twelve dated corrections to published claims, and, in one twenty-four-hour window, three preregistered verdicts (one negative, one bit-exact replication with one "not computable" stratum, one positive) and one declared deviation after a trivial bug. We report what the chain cost, what it caught, what it missed, and what it cannot guarantee. No scientific claim about the underlying hypotheses is made.

## 1. Introduction
TODO: the setting — one investigator, seven repositories, agents as executors of protocols, not as subjects.
TODO: the problem — researcher degrees of freedom become agent degrees of freedom; iteration is free, reporting is not.
TODO: contribution list (chain, errata register, four case studies, cost table, limits) and the explicit non-claims.

## 2. Related work
TODO: preregistration for experiments *with* AI agents (Vaccaro, 2026) — same threat model, different position of the agent; what our chain adds and what it does not.
TODO: reproduction vs replication (ReScience C criteria), MLRC as an official track, Registered Reports.
TODO: intrinsic identifiers (Software Heritage) vs DOIs (Zenodo, OSF); why both are used.

## 3. The chain
### 3.1 Freeze
TODO: annotated tag, manifest hashed from the tagged commit, SWHID; why git dates are not evidence of time.
TODO: Table 1 — freezes (campaign, tag, commit, manifest SHA-256, SWHID, push time).
### 3.2 Launch guards
TODO: the execution boundary (development ≤ 1 M pair-steps vs registered ≥ 50 M), clean tree, tag-or-descendant rule, GPU wait.
TODO: what the guards do not cover (synchronisation, archive, evaluation path) — one observed failure.
### 3.3 Calibrated and paired nulls
TODO: the max-then-median statistic and why a fixed threshold fails under H0; the sign-flip paired null on saved outcomes (B = 20 000).
TODO: reading rules fixed before data (M5), controls that cannot fail (shrink at T = 0, `n_received: 0`).
### 3.4 Dated amendments
TODO: amendment as the only legal path after a freeze; examples (Bonferroni cycle 3, E1-small tuning, N10-C bis, ActionSense v0.7, NH-81).
TODO: Figure 1 — the chain, with the steps reserved to the investigator (signature, tag, SWH request).

**Figure 1.** TODO caption.
**Table 1.** TODO caption.

## 4. The errata register
TODO: five registers, five formats — a finding in itself; the unit of count (one corrected public claim = one row).
TODO: Table 2 — errata (repository, date, claim, root cause, detector, correction, cost, open).
TODO: three families of root cause (parameter not forwarded, control that cannot fail, estimate presented as measurement) and three detectors (external review, test outside CI, recomputation).
TODO: the invariant — no past artefact edited; old PDFs kept in tags; Zenodo versions superseded, not deleted.

**Table 2.** TODO caption.

## 5. Four case studies from one twenty-four-hour window (30–31 October 2026)
TODO: selection rule stated before writing — every preregistered verdict returned between 2026-10-30 00:00 and 2026-10-31 12:00 CET, no exception.
### 5.1 A negative verdict: M5 certification rule, FAILED (50/60)
TODO: rule fixed before any γ ≤ 30 datum; counts per γ; invariants intact; reading (solver budget, not scheme); secondary rerun.
### 5.2 A bit-exact replication with a "not computable" stratum: NH-01
TODO: 29 640/29 640 cells identical; confirmed at m = 0 and 0.15; ratio denominator ≈ 0 at m = 0.30 → "not computable", never "44×".
### 5.3 A positive verdict: NH-03 deferred, "recency_survives"
TODO: R at d3 = +14.65 [13.77, 15.51] vs +18.55 at d0; 79 % retained; the confound noted at review (recency vs interference).
### 5.4 A declared deviation: Lie/Strang confirmatory run
TODO: 261/576 jobs in `job_error` (PermissionError in `os.nice(0)`); stop, fix, declare, relaunch; what the amendment records.
TODO: Figure 2 — timeline of the window (tags, launches, verdicts, deviation, host).

**Figure 2.** TODO caption.

## 6. Cost
TODO: Table 3 — per campaign: human hours, machine hours, amendments, verdict.
TODO: compute lost to the chain (Lie/Strang, NH-81 refusals) vs compute avoided by it (E1-35B abandoned).

**Table 3.** TODO caption.

## 7. What the chain does not guarantee
TODO: a measurement that does not measure (baseline below chance; grids at chance for six months).
TODO: reading a forbidden field before the tag (blinding breach).
TODO: external replication is still missing; the note is self-description and says so.

## 8. Six transferable rules and artefacts
TODO: tag before run; manifest read from the tag; SWHID; registered budget refused without context; paired null on saved outcomes; amendment before relaunch.
TODO: artefacts announced (guard package), not delivered; paths to the real code.

## Acknowledgements
TODO.

## References (minimal, verified only)
- M. Vaccaro. *Preregistration for Experiments with AI Agents.* arXiv:2606.11217, ICML 2026 (spotlight position paper). — verified 2026-10-31 (abstract page and PDF).
- A. Fachechi, E. Agliari, A. Barra. *Dreaming neural networks: forgetting spurious memories and reinforcing pure ones.* arXiv:1810.12217. — cited in nerve-wml NH-01 preregistration; journal reference à vérifier.
- I. Kanter, H. Sompolinsky (1987), projection rule. — exact citation à vérifier.
- J. P. Simmons, L. D. Nelson, U. Simonsohn (2011), *False-positive psychology.* — standard reference, à vérifier.
- A. Gelman, E. Loken (2013), *The garden of forking paths.* — standard reference, à vérifier.
- ReScience C, submission process and criteria, https://rescience.github.io/write/ — verified 2026-10-31.
- Journal of Trial and Error, general call, https://journal.trialanderror.org/pub/callgeneral — from the 2026-10-30 survey, à revérifier before submission.
- Hypneum Lab artefacts: OSF `10.17605/OSF.IO/Q6JYN` (parent registration, 2026-04-19) and `10.17605/OSF.IO/TPM5S` (amendment, 2026-04-21); Zenodo `10.5281/zenodo.23619954`, `10.5281/zenodo.23636477` (kiki-flow paper drafts, superseded), concept `10.5281/zenodo.19666755`; Software Heritage `swh:1:rev:99a7cf4bb01d31e8e7f6c99c0e6676f41e6e17bb` (N10-C freeze), `swh:1:rev:02c24073d3a04e1db3d3adf2ee77e545c0bdde17` (bouba_sens v0.7), `swh:1:rev:b790db272fede343fa55c996709fe39b31f4f9dd` (Me6).
- MLRC 2026 as an official NeurIPS track, https://blog.neurips.cc/2026/05/04/mlrc-2026-reproducibility-as-an-official-track-at-neurips/ — from the survey, à revérifier.
