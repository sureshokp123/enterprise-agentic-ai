# PostgreSQL Database Standards

## Naming Convention

Tables should use snake_case.

Columns should use meaningful names.

Primary keys should use id.

---

## Indexing

Create indexes for frequently searched columns.

Avoid unnecessary indexes.

---

## Transactions

Use transactions for multiple dependent operations.

Commit only after successful completion.

Rollback on failure.

---

## Constraints

Use:

Primary Key

Foreign Key

Unique

Check Constraints

---

## Backups

Schedule daily backups.

Retain backups for at least 30 days.

---

## Performance

Avoid SELECT *

Retrieve only required columns.

Use EXPLAIN ANALYZE for slow queries.

---

## Security

Least privilege access.

Separate read and write users.

Encrypt backups.

---

## Vector Search

pgvector extension is used for AI embeddings.

Embeddings are stored inside vector columns.

Similarity search uses cosine distance.