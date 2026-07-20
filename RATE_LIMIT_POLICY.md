# Rate Limit Policy

- Respect all Reddit-provided rate-limit headers and documented limits.
- Use adaptive polling rather than a fixed aggressive schedule.
- Prioritize new submissions, new comments, and a small set of active threads.
- Deduplicate IDs before requesting additional detail.
- Back off automatically on warnings, 429 responses, elevated latency, or platform degradation.
- Reserve request capacity for reconciliation and deletion compliance.
- Stop collection when limits or approval status cannot be confirmed.
