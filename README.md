# Finance Calculator Utility

This utility helps calculate the equivalent interest rate for fixed payment plans and compares it with regular interest charges. It also identifies optimal payoff timing to avoid high-cost fees in later months.

## Features

- Calculate equivalent APR for fixed payment plans
- Compare fixed payment plans with regular interest charges
- Analyze balance reduction schedule over time
- Identify when fixed fees become more expensive than regular APR
- Recommend optimal payoff timing to minimize fees
- Support for configuration files to analyze your own data

## Output Example
---

Finance Calculator Utility - Refactored
==================================================
Running with default examples in Markdown format...

# Fixed Payment Plan Analysis #1
- Purchase Amount: $1196.00
- Number of Payments: 18
- Monthly Payment: $80.73
- Monthly Fee: $14.28
- Total Cost: $1453.14
- Total Fees: $257.04
- Equivalent APR: 25.63%

## Comparison with Regular 27.0% APR
- Regular Interest Paid: $398.80
- Regular Total Cost: $1594.80
- Regular Payments Needed: 24
- Difference (Fixed Plan - Regular): $-141.66
- The fixed payment plan saves $141.66 compared to regular payments.

## Additional Analysis
- Simple interest rate equivalent: 14.33% APR
- Monthly fee as % of purchase: 1.19% per month
- Effective rate based on avg. balance: 28.67% APR (approximate)
- Fee-only equivalent rate (on avg. balance): 28.66% APR

## Balance Schedule and Optimal Payoff Analysis
| Month | Balance | Fixed Fee | Regular Interest* | Difference | Effective Rate | APR Equivalent |
|-------|---------|-----------|------------------|------------|----------------|----------------|
|  1 | $ 1129.55 | $  14.28 | $  25.41 | $ -11.13 |  1.26% monthly | 15.17% |
|  2 | $ 1063.10 | $  14.28 | $  23.92 | $  -9.64 |  1.34% monthly | 16.12% |
|  3 | $  996.65 | $  14.28 | $  22.42 | $  -8.14 |  1.43% monthly | 17.19% |
|  4 | $  930.20 | $  14.28 | $  20.93 | $  -6.65 |  1.54% monthly | 18.42% |
|  5 | $  863.75 | $  14.28 | $  19.43 | $  -5.15 |  1.65% monthly | 19.84% |
|  6 | $  797.30 | $  14.28 | $  17.94 | $  -3.66 |  1.79% monthly | 21.49% |
|  7 | $  730.85 | $  14.28 | $  16.44 | $  -2.16 |  1.95% monthly | 23.45% |
|  8 | $  664.40 | $  14.28 | $  14.95 | $  -0.67 |  2.15% monthly | 25.79% |
| **OPTIMAL PAYOFF POINT: After month 8, pay remaining $664.40**
|  9 | $  597.95 | $  14.28 | $  13.45 | $   0.83 |  2.39% monthly | 28.66% |
| 10 | $  531.50 | $  14.28 | $  11.96 | $   2.32 |  2.69% monthly | 32.24% |
| 11 | $  465.05 | $  14.28 | $  10.46 | $   3.82 |  3.07% monthly | 36.85% |
| 12 | $  398.60 | $  14.28 | $   8.97 | $   5.31 |  3.58% monthly | 42.99% |
| 13 | $  332.15 | $  14.28 | $   7.47 | $   6.81 |  4.30% monthly | 51.59% |
| 14 | $  265.70 | $  14.28 | $   5.98 | $   8.30 |  5.37% monthly | 64.49% |
| 15 | $  199.25 | $  14.28 | $   4.48 | $   9.80 |  7.17% monthly | 86.00% |
| 16 | $  132.80 | $  14.28 | $   2.99 | $  11.29 | 10.75% monthly | 129.04% |
| 17 | $   66.35 | $  14.28 | $   1.49 | $  12.79 | 21.52% monthly | 258.27% |
| 18 | $    0.00 | $  14.28 | $   0.00 | $  14.28 |  0.00% monthly |  0.00% |

*Regular interest calculated at 27.0% APR on remaining balance

### Months where fee rate exceeds regular 27.0% APR (2.25% monthly):
| Month | Rate | APR | Balance | Fixed Fee | Regular Interest | Difference |
|-------|------|-----|---------|-----------|------------------|------------|
| 9 | 2.39% monthly | 28.66% | $597.95 | $  14.28 | $  13.45 | $   0.83 |
| 10 | 2.69% monthly | 32.24% | $531.50 | $  14.28 | $  11.96 | $   2.32 |
| 11 | 3.07% monthly | 36.85% | $465.05 | $  14.28 | $  10.46 | $   3.82 |
| 12 | 3.58% monthly | 42.99% | $398.60 | $  14.28 | $   8.97 | $   5.31 |
| 13 | 4.30% monthly | 51.59% | $332.15 | $  14.28 | $   7.47 | $   6.81 |
| 14 | 5.37% monthly | 64.49% | $265.70 | $  14.28 | $   5.98 | $   8.30 |
| 15 | 7.17% monthly | 86.00% | $199.25 | $  14.28 | $   4.48 | $   9.80 |
| 16 | 10.75% monthly | 129.04% | $132.80 | $  14.28 | $   2.99 | $  11.29 |
| 17 | 21.52% monthly | 258.27% | $66.35 | $  14.28 | $   1.49 | $  12.79 |

### Optimal Payoff Recommendation:
- Suggested optimal payoff: After month 8, pay remaining $664.40
- At this point, fixed fee would be $14.28, regular interest would be $14.95
- This would avoid 9 months of high-cost fees.

# Fixed Payment Plan Analysis #2
- Purchase Amount: $2365.20
- Number of Payments: 24
- Monthly Payment: $129.14
- Monthly Fee: $30.59
- Total Cost: $3099.36
- Total Fees: $734.16
- Equivalent APR: 27.43%

## Comparison with Regular 27.0% APR
- Regular Interest Paid: $1084.05
- Regular Total Cost: $3449.25
- Regular Payments Needed: 35
- Difference (Fixed Plan - Regular): $-349.89
- The fixed payment plan saves $349.89 compared to regular payments.

## Additional Analysis
- Simple interest rate equivalent: 15.52% APR
- Monthly fee as % of purchase: 1.29% per month
- Effective rate based on avg. balance: 31.04% APR (approximate)
- Fee-only equivalent rate (on avg. balance): 31.04% APR

## Balance Schedule and Optimal Payoff Analysis
| Month | Balance | Fixed Fee | Regular Interest* | Difference | Effective Rate | APR Equivalent |
|-------|---------|-----------|------------------|------------|----------------|----------------|
|  1 | $ 2266.65 | $  30.59 | $  51.00 | $ -20.41 |  1.35% monthly | 16.19% |
|  2 | $ 2168.10 | $  30.59 | $  48.78 | $ -18.19 |  1.41% monthly | 16.93% |
|  3 | $ 2069.55 | $  30.59 | $  46.56 | $ -15.97 |  1.48% monthly | 17.74% |
|  4 | $ 1971.00 | $  30.59 | $  44.35 | $ -13.76 |  1.55% monthly | 18.62% |
|  5 | $ 1872.45 | $  30.59 | $  42.13 | $ -11.54 |  1.63% monthly | 19.60% |
|  6 | $ 1773.90 | $  30.59 | $  39.91 | $  -9.32 |  1.72% monthly | 20.69% |
|  7 | $ 1675.35 | $  30.59 | $  37.70 | $  -7.11 |  1.83% monthly | 21.91% |
|  8 | $ 1576.80 | $  30.59 | $  35.48 | $  -4.89 |  1.94% monthly | 23.28% |
|  9 | $ 1478.25 | $  30.59 | $  33.26 | $  -2.67 |  2.07% monthly | 24.83% |
| 10 | $ 1379.70 | $  30.59 | $  31.04 | $  -0.45 |  2.22% monthly | 26.61% |
| **OPTIMAL PAYOFF POINT: After month 10, pay remaining $1379.70**
| 11 | $ 1281.15 | $  30.59 | $  28.83 | $   1.76 |  2.39% monthly | 28.65% |
| 12 | $ 1182.60 | $  30.59 | $  26.61 | $   3.98 |  2.59% monthly | 31.04% |
| 13 | $ 1084.05 | $  30.59 | $  24.39 | $   6.20 |  2.82% monthly | 33.86% |
| 14 | $  985.50 | $  30.59 | $  22.17 | $   8.42 |  3.10% monthly | 37.25% |
| 15 | $  886.95 | $  30.59 | $  19.96 | $  10.63 |  3.45% monthly | 41.39% |
| 16 | $  788.40 | $  30.59 | $  17.74 | $  12.85 |  3.88% monthly | 46.56% |
| 17 | $  689.85 | $  30.59 | $  15.52 | $  15.07 |  4.43% monthly | 53.21% |
| 18 | $  591.30 | $  30.59 | $  13.30 | $  17.29 |  5.17% monthly | 62.08% |
| 19 | $  492.75 | $  30.59 | $  11.09 | $  19.50 |  6.21% monthly | 74.50% |
| 20 | $  394.20 | $  30.59 | $   8.87 | $  21.72 |  7.76% monthly | 93.12% |
| 21 | $  295.65 | $  30.59 | $   6.65 | $  23.94 | 10.35% monthly | 124.16% |
| 22 | $  197.10 | $  30.59 | $   4.43 | $  26.16 | 15.52% monthly | 186.24% |
| 23 | $   98.55 | $  30.59 | $   2.22 | $  28.37 | 31.04% monthly | 372.48% |
| 24 | $    0.00 | $  30.59 | $   0.00 | $  30.59 |  0.00% monthly |  0.00% |

*Regular interest calculated at 27.0% APR on remaining balance

### Months where fee rate exceeds regular 27.0% APR (2.25% monthly):
| Month | Rate | APR | Balance | Fixed Fee | Regular Interest | Difference |
|-------|------|-----|---------|-----------|------------------|------------|
| 11 | 2.39% monthly | 28.65% | $1281.15 | $  30.59 | $  28.83 | $   1.76 |
| 12 | 2.59% monthly | 31.04% | $1182.60 | $  30.59 | $  26.61 | $   3.98 |
| 13 | 2.82% monthly | 33.86% | $1084.05 | $  30.59 | $  24.39 | $   6.20 |
| 14 | 3.10% monthly | 37.25% | $985.50 | $  30.59 | $  22.17 | $   8.42 |
| 15 | 3.45% monthly | 41.39% | $886.95 | $  30.59 | $  19.96 | $  10.63 |
| 16 | 3.88% monthly | 46.56% | $788.40 | $  30.59 | $  17.74 | $  12.85 |
| 17 | 4.43% monthly | 53.21% | $689.85 | $  30.59 | $  15.52 | $  15.07 |
| 18 | 5.17% monthly | 62.08% | $591.30 | $  30.59 | $  13.30 | $  17.29 |
| 19 | 6.21% monthly | 74.50% | $492.75 | $  30.59 | $  11.09 | $  19.50 |
| 20 | 7.76% monthly | 93.12% | $394.20 | $  30.59 | $   8.87 | $  21.72 |
| 21 | 10.35% monthly | 124.16% | $295.65 | $  30.59 | $   6.65 | $  23.94 |
| 22 | 15.52% monthly | 186.24% | $197.10 | $  30.59 | $   4.43 | $  26.16 |
| 23 | 31.04% monthly | 372.48% | $98.55 | $  30.59 | $   2.22 | $  28.37 |

### Optimal Payoff Recommendation:
- Suggested optimal payoff: After month 10, pay remaining $1379.70
- At this point, fixed fee would be $30.59, regular interest would be $31.04
- This would avoid 13 months of high-cost fees.

# Fixed Payment Plan Analysis #3
- Purchase Amount: $200.00
- Number of Payments: 18
- Monthly Payment: $13.51
- Monthly Fee: $2.39
- Total Cost: $243.18
- Total Fees: $43.02
- Equivalent APR: 25.73%

## Comparison with Regular 27.0% APR
- Regular Interest Paid: $66.88
- Regular Total Cost: $266.88
- Regular Payments Needed: 24
- Difference (Fixed Plan - Regular): $-23.70
- The fixed payment plan saves $23.70 compared to regular payments.

## Additional Analysis
- Simple interest rate equivalent: 14.39% APR
- Monthly fee as % of purchase: 1.20% per month
- Effective rate based on avg. balance: 28.79% APR (approximate)
- Fee-only equivalent rate (on avg. balance): 28.68% APR

## Balance Schedule and Optimal Payoff Analysis
| Month | Balance | Fixed Fee | Regular Interest* | Difference | Effective Rate | APR Equivalent |
|-------|---------|-----------|------------------|------------|----------------|----------------|
|  1 | $  188.88 | $   2.39 | $   4.25 | $  -1.86 |  1.27% monthly | 15.18% |
|  2 | $  177.76 | $   2.39 | $   4.00 | $  -1.61 |  1.34% monthly | 16.13% |
|  3 | $  166.64 | $   2.39 | $   3.75 | $  -1.36 |  1.43% monthly | 17.21% |
|  4 | $  155.52 | $   2.39 | $   3.50 | $  -1.11 |  1.54% monthly | 18.44% |
|  5 | $  144.40 | $   2.39 | $   3.25 | $  -0.86 |  1.66% monthly | 19.86% |
|  6 | $  133.28 | $   2.39 | $   3.00 | $  -0.61 |  1.79% monthly | 21.52% |
|  7 | $  122.16 | $   2.39 | $   2.75 | $  -0.36 |  1.96% monthly | 23.48% |
|  8 | $  111.04 | $   2.39 | $   2.50 | $  -0.11 |  2.15% monthly | 25.83% |
| **OPTIMAL PAYOFF POINT: After month 8, pay remaining $111.04**
|  9 | $   99.92 | $   2.39 | $   2.25 | $   0.14 |  2.39% monthly | 28.70% |
| 10 | $   88.80 | $   2.39 | $   2.00 | $   0.39 |  2.69% monthly | 32.30% |
| 11 | $   77.68 | $   2.39 | $   1.75 | $   0.64 |  3.08% monthly | 36.92% |
| 12 | $   66.56 | $   2.39 | $   1.50 | $   0.89 |  3.59% monthly | 43.09% |
| 13 | $   55.44 | $   2.39 | $   1.25 | $   1.14 |  4.31% monthly | 51.73% |
| 14 | $   44.32 | $   2.39 | $   1.00 | $   1.39 |  5.39% monthly | 64.71% |
| 15 | $   33.20 | $   2.39 | $   0.75 | $   1.64 |  7.20% monthly | 86.39% |
| 16 | $   22.08 | $   2.39 | $   0.50 | $   1.89 | 10.82% monthly | 129.89% |
| 17 | $   10.96 | $   2.39 | $   0.25 | $   2.14 | 21.81% monthly | 261.68% |
| 18 | $    0.00 | $   2.39 | $   0.00 | $   2.39 |  0.00% monthly |  0.00% |

*Regular interest calculated at 27.0% APR on remaining balance

### Months where fee rate exceeds regular 27.0% APR (2.25% monthly):
| Month | Rate | APR | Balance | Fixed Fee | Regular Interest | Difference |
|-------|------|-----|---------|-----------|------------------|------------|
| 9 | 2.39% monthly | 28.70% | $99.92 | $   2.39 | $   2.25 | $   0.14 |
| 10 | 2.69% monthly | 32.30% | $88.80 | $   2.39 | $   2.00 | $   0.39 |
| 11 | 3.08% monthly | 36.92% | $77.68 | $   2.39 | $   1.75 | $   0.64 |
| 12 | 3.59% monthly | 43.09% | $66.56 | $   2.39 | $   1.50 | $   0.89 |
| 13 | 4.31% monthly | 51.73% | $55.44 | $   2.39 | $   1.25 | $   1.14 |
| 14 | 5.39% monthly | 64.71% | $44.32 | $   2.39 | $   1.00 | $   1.39 |
| 15 | 7.20% monthly | 86.39% | $33.20 | $   2.39 | $   0.75 | $   1.64 |
| 16 | 10.82% monthly | 129.89% | $22.08 | $   2.39 | $   0.50 | $   1.89 |
| 17 | 21.81% monthly | 261.68% | $10.96 | $   2.39 | $   0.25 | $   2.14 |

### Optimal Payoff Recommendation:
- Suggested optimal payoff: After month 8, pay remaining $111.04
- At this point, fixed fee would be $2.39, regular interest would be $2.50
- This would avoid 9 months of high-cost fees.

---


## Usage

### Basic Usage

```bash
python finance_calculator.py
```

This runs the analysis with default examples.

### Using Configuration File

```bash
python finance_calculator.py path/to/config.json
```

## Configuration File Format

Create a JSON file with the following structure:

```json
{
  "regular_apr": 27.0,
  "payment_plans": [
    {
      "purchase_amount": 1196.0,
      "num_payments": 18,
      "monthly_payment": 80.73,
      "monthly_fee": 14.28
    }
  ]
}
```

### Parameters Explained

- `regular_apr`: The regular annual percentage rate to compare against (default: 27.0)
- `purchase_amount`: Initial purchase amount
- `num_payments`: Number of monthly payments in the fixed plan
- `monthly_payment`: Total monthly payment amount (principal + fee)
- `monthly_fee`: Monthly fee component of the payment

## Output Explanation

The utility provides several key metrics:

1. **Equivalent APR**: The annual percentage rate that would result in the same payment schedule as the fixed payment plan
2. **Balance Schedule**: Shows how the remaining balance decreases over time and the effective monthly rate of fees
3. **Optimal Payoff Timing**: When to payoff the remaining balance to avoid high-cost fees in later months
4. **Cost Comparison**: How the fixed payment plan compares to regular interest charges

## Example Output Interpretation

The utility will show when the fixed monthly fees become more expensive than the regular APR as a percentage of the remaining balance. For example, if the regular APR is 27% (2.25% monthly), the utility will identify months where the effective rate of the fixed fee exceeds 2.25% monthly (27% annually) on the remaining balance.

In later months of the payment plan, as the balance decreases, the fixed fee becomes increasingly expensive as a percentage of the remaining balance, sometimes reaching very high effective rates (100%+ APR).
