# NFT Price Prediction Project

## Project objective

The objective was to identify blockchain transaction factors associated
with NFT prices and develop a model for predicting NFT transaction value.

## Data source

The analysis used an Ethereum NFT SQLite dataset. The main modelling
data came from the transfers table.

The target variable was transaction_value, converted from wei to ETH.
Because NFT prices were highly skewed and contained extreme values,
price_eth was transformed using log(1 + price_eth).

## Data preparation

The data was checked for missing values, duplicates and outliers.
Timestamps were converted from Unix seconds to UTC datetime values.
Transactions were sorted chronologically.

Historical features use earlier rows in timestamp/event-ID order. Same-block
ordering and transaction grouping remain limitations; see README.md.

## Features

The model included:

- block_number
- collection_activity
- seller_activity
- buyer_activity
- previous_token_log_price
- previous_token_transfers
- days_since_previous_transfer
- token_age_days
- collection_previous_avg_log_price
- seller_previous_avg_log_price
- buyer_previous_avg_log_price

## Models evaluated

The following models were compared:

- Median baseline model
- Multiple linear regression
- Random Forest regression
- Tuned Random Forest regression, where applicable

## Final model

Selected model: Tuned Random Forest

Training MAE on log-price scale: 0.116647
Training R-squared: 0.768893

Testing MAE on log-price scale: 0.107617
Testing R-squared: 0.703683

## Most important predictive factors

- collection_previous_avg_log_price: 0.121423
- collection_activity: 0.013479
- buyer_previous_avg_log_price: 0.009044
- seller_previous_avg_log_price: 0.006297
- previous_token_log_price: 0.004158
- seller_activity: 0.001496
- token_age_days: 0.000167
- days_since_previous_transfer: 0.000034
- previous_token_transfers: 0.000013
- block_number: 0.000000

## Interpretation

Compare the model comparison table in the notebook before drawing conclusions
about relative performance. The final forest is chosen using training-data
cross-validation, not test-set MAE. Importance values describe this fitted model.

The difference between training and testing performance indicates the
extent to which the model generalizes to later transactions.

## Limitations

- Transaction value may represent the value of a complete blockchain
  transaction rather than the exact sale price of one NFT.
- The sample covered a limited portion of the complete database.
- The dataset did not include rarity, artwork characteristics, creator
  reputation, social-media interest or cryptocurrency market conditions.
- Feature importance describes predictive usefulness, not causation.
- Historical features must be calculated using only information
  available before each predicted transaction.

## Conclusion

This is an exploratory prediction prototype. Results describe this limited
sample and evaluation protocol, not a validated NFT valuation system.