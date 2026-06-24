# The GTM Operating System (reusable)

A lightweight, AI-native go-to-market engine for founders and solo operators. Point it at any product by filling in the templates in this folder.

## Operating principles
1. **One north-star action per project.** Everything funnels to it (e.g. a booked call, a signup, a demo).
2. **Outcomes over technology.** Say "know which campaign drives revenue," not "attribution engine."
3. **Defensible claims only.** No unsubstantiated stats. Reframe to grounded versions.
4. **Protect the core domain.** High-volume cold outbound never sends from your primary business mailbox/domain.
5. **One source of truth** for leads + pipeline, so every report is real numbers, not vibes.
6. **Small bets, fast read.** Ship a test, get an honest read, double down or kill.
7. **Compliance is a feature.** Respect per-region rules (GDPR/PECR, CAN-SPAM, PDPL, etc.) by default.

## The engine (7 stages)
| Stage | Question it answers | Example tool |
|---|---|---|
| 1. ICP | Who exactly, and what triggers their need? | ICP matrix (below) |
| 2. List | Who specifically, with verified contact data? | Apollo / Clay |
| 3. Message | What outcome do we promise, in their words? | Sequence template |
| 4. Channel | Where do we reach them (email / LinkedIn / content)? | Instantly / LinkedIn |
| 5. Convert | How does interest become the north-star action? | Booking link, call script |
| 6. Measure | What is each stage producing? | Reporting template |
| 7. Learn | What do we change next? | Recurring review |

## Sub-agents you can run (with an AI coding agent)
- **List-Builder** — find + enrich target contacts.
- **Copywriter** — sequence + variant copy, outcome-led.
- **Content-Engine** — inbound calendar, drafts, lead magnets (see `../linkedin-autoposter/`).
- **Enrichment/Research** — account research, trigger-event detection.
- **Reporter** — assembles the recurring report from the ledger.
- **Compliance/Deliverability sentinel** — checks lists + sending health before any send.

## ICP matrix (fill per project)
| Field | Definition | Your value |
|---|---|---|
| Segment | The buying unit | |
| Size band | Employees / revenue | |
| Geography | Primary market(s) | |
| Persona(s) | Who you reach | |
| Trigger | Why now | |
| Core pain | The wound you heal | |
| Disqualifiers | Who to skip | |

## Funnel ledger (the scoreboard)
Outbound: `Targeted → Delivered → Opened → Replied → Positive reply → Action booked → Held → Won`
Inbound: `Impressions → Visits → Lead → Action booked → Held → Won`
North-star KPI: the action booked / period (capped to your capacity). See `Reporting.template.md`.

## Cadence
- **Plan** (start of week): what runs, targets, what you need.
- **Review** (end of week / biweekly): ledger numbers, what's working/dead, next bets.

## Guardrails
- **Deliverability:** dedicated sending domain for volume, warmup 2–3 weeks, SPF/DKIM/DMARC, <40 sends/mailbox/day, clean lists.
- **Compliance:** legitimate-interest basis + clear opt-out; honor suppression lists; use licensed data only.
- **Brand safety:** every claim passes "could we defend this to a skeptical buyer?"
