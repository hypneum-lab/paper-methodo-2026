# 0. Who did what: the human-agent setup

This note is written by one person with code agents, and the chain it
describes exists because of that setup. The reader needs to know which
parts were done by whom, because the errata of section 4 are sorted by
who found them.

**The principal investigator (PI)** is the only human. He signs every
preregistration, creates every freeze tag, types every launch command
on every host, and types every crontab line himself: the agent harness
refuses to edit a crontab, and the lab's rule is that nothing starts or
stops a computation without the PI's hand. He arbitrates between
conflicting reviews and decides which hypotheses are killed (three were,
on 2026-10-30). Every decision is recorded as a dated line with the
option chosen and the options refused.

**The primary agent** is Claude Code running Claude Fable 5.1
(`claude-fable-5-1`), used in long sessions, one per work stream:
bouba_sens and the ActionSense freeze, kiki-flow-research and the NH
campaigns, and the programme-level sessions of 30–31 October 2026 that
produced the état des lieux and this note. It reads repositories, writes
protocols, amendments, errata and code, runs nothing heavier than a
test suite on the PI's laptop, and delegates bounded tasks (literature
watch, credit programmes, a skeleton for a replication report) to
sub-agents on Claude Opus. Sessions message each other; they do not
share memory beyond a file-based index the PI can read.

**The cross-reviewer** is Codex CLI with OpenAI frontier models
(`gpt-6-astra`, `gpt-6.1-sol`), invoked through a fixed procedure
(`codex-cross-review`) with a written brief and no access to the
primary agent's reasoning. Its review of 2026-10-25 found seven of the
thirty-one corrected claims of Table 2, including the three statistical
ones the primary agent had produced and not caught. The two agents never
edit the same document; one writes, the other reads, the PI decides.

**Division of labour, as practised.** Agents propose; the PI disposes.
A protocol is drafted by the primary agent, read by the PI, frozen by
the PI's tag. A verdict is computed by code the agent wrote, read
against the null by the agent, signed by the PI as a dated comment on
the pull request. An erratum is drafted by whichever agent found the
error and committed under the PI's name after reading. No agent has
credentials to push a tag, launch on a remote host, or send a message
outside the lab.

**What this setup does not control.** The primary agent wrote most of
the code it later reviewed; the silent-parameter errors of section 4
were made and found by the same class of tool. The external reviewer
had one day. The PI read every document but not every line of every
run. The chain of section 3 is the response to those three limits, not
a substitute for them.
