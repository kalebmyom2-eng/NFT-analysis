# GitHub preparation notes

## Changes from the original notebook

- Added section introductions, project scope, setup and evaluation limitations.
- Replaced working-directory assumptions with `NFT_DB_PATH` and a read-only SQLite connection.
- Made sample selection explicit with `ORDER BY rowid` and timestamp/event-ID sorting.
- Removed the invalid final Python cell containing a shell export command for another notebook.
- Replaced test-MAE-based final forest selection with training-only cross-validation selection.
- Limited model/search workers to two to avoid exhausting a laptop's CPU resources.
- Routed aggregate reports and local-only prediction/model files to separate directories.
- Added a fresh-kernel runner that exports figures and removes row-level previews from notebook outputs.
- Replaced unsupported narrative claims with model comparisons and explicit limitations.
- Added dataset attribution, dependencies and Git exclusions.

The original files in Downloads were not edited. The separate downloaded Ethereum
NFT reference notebook was used only to identify provenance and is not included.

## Remaining research improvements

This preparation preserves the core exploratory design. Before presenting the
scores as a forecasting benchmark, rebuild history strictly before each block,
count bundles against full transaction membership, split on block/transaction
boundaries, and reserve a fresh holdout period. These are substantive study
design changes rather than repository packaging changes.

## Verification

On September 24, 2026, the prepared notebook ran in a fresh Python 3.13.9 kernel
against the original local database: all 81 code cells executed in order with
no cell errors, and eight figures plus model, prediction and aggregate exports
were generated. Runner exit status was zero. Notebook schema validation passed.
Git ignore checks confirmed exclusion of the database, model, row-level
predictions, environment files and virtual environment. The saved notebook
contains no absolute `/Users/` paths.

The sandbox denied process enumeration during Jupyter kernel shutdown. This
produced a cleanup warning after all cells finished; exported results and the
executed notebook were saved successfully. No claim is made that every
transitive dependency has been locked or that this was tested on another OS.
