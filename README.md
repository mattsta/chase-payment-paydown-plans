# Finance Calculator Utility

This utility helps calculate the equivalent interest rate for fixed payment plans and compares it with regular interest charges. It also identifies optimal payoff timing to avoid high-cost fees in later months.

## Features

- Calculate equivalent APR for fixed payment plans
- Compare fixed payment plans with regular interest charges
- Analyze balance reduction schedule over time
- Identify when fixed fees become more expensive than regular APR
- Recommend optimal payoff timing to minimize fees
- Support for configuration files to analyze your own data

## Usage

### Basic Usage

```bash
python src/finance_calculator.py
```

This runs the analysis with default examples.

### Using Configuration File

```bash
python src/finance_calculator.py path/to/config.json
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
