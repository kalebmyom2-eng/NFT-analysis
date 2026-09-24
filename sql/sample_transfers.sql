-- SQLite: deterministic local sample, not a random market sample.
SELECT *
FROM transfers
WHERE transaction_value > 0
ORDER BY rowid
LIMIT 100000;
