# Launch Setup (template) — enrich → send

> Run this when your sending mailbox is warmed up. Example tools: Apollo (enrichment) + Instantly (sender). Swap in your own.

## Tool split
- **Enrichment tool** (e.g. Apollo) = reveal verified work emails for your list. Costs credits — confirm the count first.
- **Sender/sequencer** (e.g. Instantly) = holds the campaign, sends on a schedule, ramps volume, detects replies, stops on reply.
- **Inbound** = the LinkedIn autoposter in `../linkedin-autoposter/`.

## Build the campaign(s)
Consider one campaign per region/segment so send times land in local business hours and you can compare.

| Step | Day | Content |
|---|---|---|
| 1 | 0 | Touch 1 (custom body per contact) — A/B the subject |
| 2 | +3 | Touch 2 (proof + link) |
| 3 | +3 | Touch 3 (one insight + link) |
| 4 | +4 | Touch 4 (break-up + free value) |

**Settings:** stop-on-reply ON · open tracking ON · plain text · local business hours, weekdays · ramp from ~8–10/day up to ~25–30/day as deliverability stays healthy · include an opt-out line.

**Merge fields:** `firstName`, `company`, plus a per-contact `email_1_body` column holding the custom Touch-1 text; Touches 2–4 use shared templates.

## Pre-launch checklist
- [ ] List finalized
- [ ] Touch-1 copy approved
- [ ] Warmup healthy + DMARC tightened to `p=quarantine`
- [ ] Emails revealed (confirm credit spend first)
- [ ] CSV assembled (merge fields + per-contact Touch-1 body)
- [ ] Campaign(s) built, stop-on-reply ON, ramp set, opt-out line added
- [ ] Booking link live in Touches 2–4
