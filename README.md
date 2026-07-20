# WSBAI Reddit Data Access Review

This public repository contains only the Reddit access-review portion of WSBAI. It intentionally excludes proprietary trading logic, brokerage integrations, market-data credentials, model weights, and private source code.

## Purpose

WSBAI is a private, currently noncommercial, read-only financial research and prospective paper-trading decision-support application for one user. The initial requested scope is limited to public posts and comments in `r/wallstreetbets`.

The Reddit connector is designed to:

- collect only approved public fields;
- preserve point-in-time observations needed for prospective research;
- distinguish explicit recommendations from jokes, questions, quotations, sarcasm, and retrospective claims;
- reconstruct public thread relationships and material rebuttals;
- verify financial claims against public primary sources;
- produce paper-trade candidates requiring explicit human review.

## Current status

The connector is **approval-gated**. It refuses to access Reddit unless explicit Data API approval has been obtained and the local setting `REDDIT_ACCESS_APPROVED=true` is present.

No Reddit credentials are stored in this repository. No live brokerage execution is included.

## Repository contents

- `DATA_FLOW.md` - requested data flow and minimization
- `PRIVACY_AND_DELETION.md` - deletion and retention design
- `SECURITY.md` - credential and access controls
- `RATE_LIMIT_POLICY.md` - adaptive rate-limit behavior
- `DEVVIT_FIT_ANALYSIS.md` - why the proposed external research backend is not a normal Devvit app
- `REQUESTED_DATA_FIELDS.md` - narrow initial field list
- `PAPER_ONLY_PILOT.md` - initial research restrictions
- `src/` - nonfunctional approval-gated connector skeleton
- `tests/` - compliance-gate test

## Explicit non-goals

The pilot will not post, comment, vote, send messages, moderate communities, manipulate engagement, redistribute Reddit content, sell Reddit data, train a general-purpose foundation model, or automatically place brokerage orders.
