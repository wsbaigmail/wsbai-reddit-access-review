# Data Flow

1. Reddit OAuth access is enabled only after explicit approval.
2. The connector requests the narrow approved scope for `r/wallstreetbets`.
3. Raw observations are written to a deletable, access-controlled raw store.
4. A normalization process extracts non-sensitive research features and public thread relationships.
5. Claims are checked against public primary sources outside Reddit.
6. Research candidates are sent to paper-trading analysis only.
7. Every recommendation requires human review.
8. Deletion events remove raw content and trigger recomputation of dependent records.

The Reddit raw store is separate from market data, brokerage data, and proprietary scoring code.
