---
title: "Resume: Localization Vendor Comparison"
date: 2026-10-09
status: hand-over
tags: [drafts, hand-over, localization, vendors]
---
# Resume: Localization Vendor Comparison

The 2026-10-09 session started comparing the three localization quotes for Spanish and German and stopped before a recommendation. The quotes cover price and scope, but none says how the vendor works with plain-text script files or checks text length on the letter reader, and both matter more than the price gap.

Delete this note when the vendor task in [[prototype/implementation-plan]] closes.

## Done So Far

| Vendor | Rate | Per language at 86,000 words | Spanish and German | Includes |
|---|---|---|---|---|
| A | $0.11 | $9,460 | $18,920 | Translation only |
| B | $0.13 | $11,180 | $22,360 | Translation and one review pass |
| C | $0.16 | $13,760 | $27,520 | Translation, review, and in-game text check |

- **Costs.** The per-word rates and the 86,000-word count come from [[research/localization/localization-cost-estimate]] [emerging] and [[research/narrative/script-word-count]] [emerging].
- **Overlap with a planned task.** Vendor C's in-game check covers part of the ledger task to audit Spanish and German letters at 800p. Vendor A or B would leave that audit to the team.
- **Grant figure.** The Northern Arts Fund application asks for the localization cost and is due 2026-11-30 ([[strategy/funding]]). Until a vendor is chosen, the draft application uses the full range of $18,920 to $27,520.

## Open Questions

- **Script files.** Will each vendor translate inside the team's plain-text script files, or does the text need exporting to another format? Clause S3 of [[architecture/CONSTITUTION]] keeps all text in those files.
- **Line length.** Who checks that translated letters still fit the letter reader at handheld size? Clause P2 requires it in every launch language ([[architecture/ui/letter-reader]]).
- **Patches.** What does each vendor charge for text added after launch, and is there a minimum fee?

## Next Steps

1. Run [[prompts/localization-vendor-research-brief]] and pass the report through the [[vault-guide/ingestion-gate]].
2. Draft the three open questions as an email for Ines to send. Vendor contact is hers, and choosing a vendor spends money, so it needs her yes.
3. Add the answers as columns to the table above, then write the comparison for Ines with a recommendation and its main risk.
4. If vendor A or B wins, keep the ledger's 800p audit of Spanish and German letters. If vendor C wins, rescope that task to spot-checking the vendor's results.

## Load Before Resuming

[[research/localization/localization-cost-estimate]], [[decisions/product/PDR-P014-launch-languages|PDR-P014]], [[decisions/rejected/PDR-P013-full-voice-acting|PDR-P013]], [[strategy/funding]], and [[architecture/CONSTITUTION]] clauses P2 and S3.
