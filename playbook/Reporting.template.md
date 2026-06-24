# Reporting Framework (template)

> A scoreboard so every touchpoint is real numbers. Cadence: weekly pulse and/or biweekly full report.

## KPI tree
**North-Star Metric:** the north-star action booked / period (capped to your capacity).
**Ultimate outcome:** deals/customers won.

### A. Outbound (email)
| Metric | Definition | Typical target |
|---|---|---|
| Deliverability % | delivered ÷ sent (guardrail <5% bounce) | ≥95% |
| Open rate | opened ÷ delivered | 50–60% |
| Reply rate | replies ÷ delivered | 8–12% |
| **Positive-reply rate** ⭐ | interested ÷ delivered | 2–5% |
| Reply→action % | actions ÷ positive replies | 30–40% |

### B. Inbound (LinkedIn / content)
Posts published · impressions · engagement rate (≥3%) · profile views · follower growth · clicks · actions booked.

### C. North-star + conversion
Actions booked ⭐ · show rate (≥70%) · won ⭐ · close rate.

### D. Efficiency / guardrails
Cost per booked action · enrichment credits used · region/segment split · spam-complaint rate (kill switch if rising).

## Report format
```
GTM Report #N · <date range>

⭐ HEADLINE   actions booked X (target Y) · held X · won X

OUTBOUND   sent X · deliv X% · open X% · reply X% · positive X% · booked X   (by segment)
INBOUND    posts X · impressions X · eng X% · followers +X · booked X
WHAT'S WORKING / WHAT'S DEAD   2–4 evidence-based bullets
DECISIONS NEEDED   explicit asks
NEXT PERIOD   what you run, targets
```

## Auto vs manual
- **Automatable** (with an AI agent + APIs): posts published (repo), enrichment credits, actions booked (calendar).
- **Manual paste:** email-tool stats, LinkedIn analytics, won deals.
