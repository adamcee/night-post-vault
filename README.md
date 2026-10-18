---
title: Night Post — Example Vault
---
# Night Post — Example Vault

Night Post is a fictional indie game: an adventure RPG about a courier who delivers letters at night through a forest whose paths shift with the moon. Every quest is a letter, and you can open the sealed ones.

This vault is the project memory of the three-person team making it, six months in. Their AI agents read it at the start of every session and keep it up to date, and the sections below show how each part of the method looks in a real project.

It's an example for the [Agentic Vault](https://github.com/adamcee/agentic-vault), a template for giving AI sessions persistent project memory. Explore it as a website at [adamcee.github.io/night-post-vault](https://adamcee.github.io/night-post-vault/), or clone this repo and open the folder in Obsidian to see it the way the team does.

## Start Here

[AGENTS.md](AGENTS.md) is the first file every AI session reads. It says what the game is, what phase the team is in, which decisions are settled, and what the last session did.

## Picking Up Where the Last Session Left Off

- **The checkpoint.** The top of [AGENTS.md](AGENTS.md) summarizes the last session in two sentences, so a new session starts from there instead of from zero.
- **The session log.** Every session adds one line saying which AI tool did what. [Session history](session-history.md) runs from the first day in April to October.
- **A hand-over note.** The last session ran out of time while comparing translation vendors, so it left a note with what's done and what's next: [resume note](drafts/2026-10-09-resume-localization-vendors.md).

## Two Task Lists

- **The AI's list.** Every action item an AI session finds goes into one ledger, the [implementation plan](prototype/implementation-plan.md).
- **The human's list.** Ines, the project lead, keeps her own short list and copies items over from the ledger at her Friday review. No AI writes to [her list](prototype/human-task-list.md).
- **A decision still being made.** Players at the demo festival kept asking for a map, but a map could undercut the game's shifting paths. The team is deciding whether to add one, and the AI drafts that decision in chat without writing it until Ines approves. It's listed under "Decisions Owed" in the [ledger](prototype/implementation-plan.md), and the original request is in [this idea note](ideas/foldable-map.md).

## Decisions That Changed

Each decision record says what was chosen, what was rejected, and why. When evidence changes a decision, a new record replaces the old one and both stay on file.

- **Combat became conversation.** The team planned turn-based fights, but playtesters said fighting clashed with the cozy tone. Encounters are now resolved by talking: [the old decision](decisions/product/PDR-P003-turn-based-encounters.md) and [its replacement](decisions/product/PDR-P009-parley-encounters.md).
- **Five regions became three.** Publishers and a budget estimate both said five regions was too much for three people, so two regions were cut: [the decision](decisions/product/PDR-P012-three-regions.md).
- **An idea turned down.** Online co-op was considered and rejected, and the record stays so nobody proposes it again without new reasons: [the rejection](decisions/rejected/PDR-P007-co-op-courier-mode.md).

## Following One Finding Through the Vault

When new evidence arrives, the agent checks which decisions it affects. Here is one finding traced end to end.

1. **A playtest finds a problem.** Players on handheld PCs couldn't read the handwritten letters: [playtest 4](research/playtests/pt-04-vertical-slice.md).
2. **An audit measures it.** The team checked the letters against a published readability standard: [the audit](research/accessibility/letter-readability-audit.md).
3. **The decision changes.** Handwriting moved to headers and signatures, with a readable body font and a font toggle: [the new decision](decisions/product/PDR-P011-readable-letters.md). A later playtest confirmed the fix.

## Kinds of Research

Each research doc carries a tag for how solid its evidence is, from `emerging` (one small test) to `established` (a published standard).

- **A playtest.** Notes, player quotes, and numbers from watching people play: [playtest 2](research/playtests/pt-02-greybox-encounters.md).
- **Market data.** What happened when the demo went public at an online festival: [festival results](research/market/demo-festival-results.md).
- **An outside standard.** The one doc that summarizes published rules rather than the team's own tests: [text readability standards](research/accessibility/text-contrast-and-size-standards.md).

## Ideas Before They're Decisions

Raw ideas get a short note until they're promoted to a decision, rejected, or folded into something else.

- **Promoted.** "What if encounters were conversations?" became the parley decision: [the idea](ideas/talk-instead-of-fight.md).
- **Rejected.** A crafting system was turned down because it added busywork: [the idea](ideas/crafting-system.md).
- **Still open.** A small letter-writing minigame is waiting for its turn: [the idea](ideas/letter-writing-minigame.md).

## Checking AI Writing Before It Counts

AI-written material waits in `drafts/` until a person checks it.

- **AI lore that got the facts wrong.** An AI expanded the forest's lore but contradicted settled canon in two places, so it waits for review: [the draft](drafts/ai-lore-hushfolk-expansion.md) versus [the canon](world/factions/the-hushfolk.md).
- **A report that passed.** An AI-written market report was tightened and fact-checked before it entered the vault, and the untouched original is kept beside it: [the clean version](research/market/genre-comparables.md) and [the original](research/market/_source-genre-comparables.md).
- **A draft still waiting.** A marketing plan written for the festival was never tightened in time: [the draft](drafts/ai-report-festival-marketing-plan.md).

## Keeping the Vault Healthy

- **A vault review.** After the festival, an AI session audited the whole vault, fixed small problems on the spot, and listed the rest. It's logged in [the week's log](prototype/implementation-logs/2026-W41.md).
- **Findings go to the ledger.** Problems the review couldn't fix became tasks under "Vault Maintenance" in the [ledger](prototype/implementation-plan.md), not a report that would go stale.
- **Weekly logs.** Each week's file lists what every session changed, such as [the week of playtest 4](prototype/implementation-logs/2026-W33.md).

## The Rest of the Vault

- **The world.** Places, factions, characters, and history, including two regions that were cut: [the world bible](world/README.md).
- **The game design.** How a night of play works, from picking up letters at dusk to returning by dawn: [game design overview](architecture/game-design-overview.md).
- **The plan.** Goals, audience, price, and launch timing: [goals and audience](strategy/goals-and-audience.md).
