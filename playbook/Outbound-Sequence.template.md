# Outbound Sequence (template)

> 4 touches over ~10 business days. Low volume, personalized, plain text. Replace every `{{placeholder}}`.

## Principles
- **Plain text only** (no images/banners/tracking pixels) — reads human, lands in inbox.
- **One custom first line per contact** (`{{personal_line}}`) — a real observation about *their* business. Non-negotiable.
- **Reply-CTA on Touch 1** (no link) to protect deliverability; the link appears from Touch 2 on.
- Keep each email **under ~120 words.** Stop the sequence the moment they reply.

**Merge fields:** `{{first_name}}` · `{{company}}` · `{{personal_line}}` · `{{your_proof}}` · `{{booking_link}}`

---

### Touch 1 — Day 0 · Hook (reply-CTA, no link)
**Subject A:** `quick one about {{company}}` · **B:** `{{company}}'s hidden {{problem}}`
> Hi {{first_name}},
>
> {{personal_line}}
>
> {{one-sentence problem your ICP feels}}.
>
> {{one sentence on what you do}} — {{your_proof}}.
>
> Worth a quick look at {{the value for them}}?
>
> — {{your_name}}

### Touch 2 — Day 3 · Proof + offer (introduce link)
**Subject:** `re: {{company}}…`
> Hi {{first_name}}, here's what this looks like in practice.
>
> {{credibility / proof in 1–2 lines}}.
>
> A {{call length}} and I'll {{specific value}} — useful whether or not we work together.
>
> Grab a slot: {{booking_link}}
>
> — {{your_name}}

### Touch 3 — Day 6 · One concrete insight (give value first)
**Subject:** `a quick idea for {{company}}`
> {{first_name}} — one example of what I mean:
>
> {{a genuinely useful, specific insight the reader can act on even if they never reply}}.
>
> {{booking_link}}
>
> — {{your_name}}

### Touch 4 — Day 10 · Break-up + free value
**Subject:** `should I close the loop, {{first_name}}?`
> Hi {{first_name}}, I'll stop here so I'm not crowding your inbox.
>
> If it's ever useful: {{a small free offer that samples your paid work}}.
>
> Either way, wishing you a strong quarter.
>
> — {{your_name}}
> (book anytime: {{booking_link}})

---

## A/B & tracking
- Test the Touch 1 subject; pick the winner by reply rate after ~30 sends.
- Track open / reply / positive-reply / action-booked, segmented by region or segment.
- Replace assumed rates with your real ones after ~2 weeks.
