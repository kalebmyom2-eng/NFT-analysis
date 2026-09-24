# Data setup

The database is intentionally excluded from Git. The working source is a local
`nfts.sqlite` file (approximately 6.9 GB) with a `transfers` table.

Place your copy at `data/nfts.sqlite`, or set `NFT_DB_PATH` to its absolute path.
The notebook opens it read-only and does not copy or modify the database.

## Provenance

Dataset: [Ethereum NFTs on Kaggle](https://www.kaggle.com/datasets/simiotic/ethereum-nfts),
by Sophia Arakelyan et al. / Moonstream, 2021. Dataset ID **1643391**, version
**1**, version ID **2698517**. These IDs match the owner's original download URL.
Kaggle metadata lists **Creative Commons Attribution 4.0 International (CC BY 4.0)**.

Citation: Sophia Arakelyan et al., “Ethereum NFTs.” Kaggle, 2021.
DOI: [10.34740/KAGGLE/DSV/2698517](https://doi.org/10.34740/KAGGLE/DSV/2698517).

Sources:
- [Kaggle metadata](https://www.kaggle.com/api/v1/datasets/view/simiotic/ethereum-nfts)
- [Original dataset research](https://github.com/bugout-dev/papers/blob/main/nfts/nfts.md)
- [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)

Download version 1 from Kaggle and extract `nfts.sqlite`. A Kaggle account may be
required. Use the permanent dataset page rather than an expiring signed download
URL. The source covers April 1–September 25, 2021; this project's sampled rows
cover only a portion of that source. The project adds sampling, engineered
features, exploratory plots and predictive modeling. Dataset creators do not
endorse this analysis. The downloaded reference notebook is not bundled.

## Required schema

| Column | Use |
| --- | --- |
| `event_id` | Unique event identifier; deterministic tie-breaker |
| `transaction_hash` | Within-sample transaction grouping |
| `block_number` | Numeric predictor |
| `nft_address`, `token_id` | Collection and token history |
| `from_address`, `to_address` | Observed sender and receiver history |
| `transaction_value` | Transaction value in wei |
| `timestamp` | Unix timestamp in seconds |

The notebook selects the first 100,000 positive-value rows ordered by SQLite
`rowid`, then sorts the sample by timestamp and event ID. Reproduction requires
the same database and row order. This is not a random sample or necessarily the
first 100,000 events chronologically across the full database.

## Local validation fingerprint

The analyzed file is recorded in [source_manifest.json](source_manifest.json),
including its byte size and SHA-256 hash. The 100,000 selected rows span
2021-08-01T00:00:17+00:00 to 2021-08-05T18:57:04+00:00 (UTC),
across 25,373 distinct blocks. The hash fingerprints the local input; it was not
compared with an independently published checksum.
