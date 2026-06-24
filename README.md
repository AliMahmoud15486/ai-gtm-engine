# AI GTM Engine

An open-source, AI-native go-to-market starter kit for founders and solo operators. Run a real outbound + inbound motion — **list → message → send → measure** — and let an autonomous LinkedIn poster handle your content, all from templates you fill in.

Built and battle-tested in a live GTM program, then genericized for anyone to use.

## What's inside

### 📘 `playbook/` — the GTM operating system (templates)
- **`GTM-Operating-System.md`** — principles, the 7-stage engine, sub-agents, ICP matrix, funnel ledger, cadence, guardrails.
- **`Outbound-Sequence.template.md`** — a 4-touch cold-email sequence (value-led, with placeholders).
- **`Launch-Setup.template.md`** — enrich → send playbook + pre-launch checklist.
- **`Reporting.template.md`** — KPI tree + a fixed report format.
- **`Contact-List.template.md`** — the list shape (keep your filled-in version private).

### 🤖 `linkedin-autoposter/` — autonomous LinkedIn posting
A GitHub Actions cron that posts to your LinkedIn profile on a schedule via the official `w_member_social` API, auto-generating a **branded image** (quote card or chart) per post. Hands-off after a ~30-minute setup. See its [README](linkedin-autoposter/README.md).

## Quick start
1. **Inbound:** copy `linkedin-autoposter/` into its own repo, set your brand in `media_gen.py`, add your LinkedIn token as a secret, drop posts in `queue/`. It posts itself.
2. **Outbound:** fill in the `playbook/` templates for your product, build your list, warm a sending mailbox, then follow `Launch-Setup.template.md`.
3. **Measure:** run the `Reporting.template.md` cadence so every week is real numbers.

## Principles it's built on
Outcomes over technology · defensible claims only · protect your core domain · give value before you ask · one source of truth · compliance by default.

## License
MIT — see [LICENSE](LICENSE). Use it, fork it, sell with it. No warranty.

---
*Tip: pair this with an AI coding agent (like Claude Code) to spin up the sub-agents — list-building, copywriting, content, reporting — described in the playbook.*
