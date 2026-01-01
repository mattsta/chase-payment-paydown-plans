#!/usr/bin/env python3
"""
Finance Calculator Utility

This utility helps calculate the equivalent interest rate for fixed payment plans
and compares it with regular interest charges. Includes support for configuration files.
"""

import json
from dataclasses import dataclass
from pathlib import Path


@dataclass
class PaymentPlan:
    """Represents a fixed payment plan."""

    purchase_amount: float
    num_payments: int
    monthly_payment: float
    monthly_fee: float


@dataclass
class MonthlyScheduleData:
    """Data for each month in the balance schedule."""

    month: int
    balance: float
    principal_payment: float
    fee: float
    effective_monthly_rate: float
    regular_interest_equivalent: float


@dataclass
class AnalysisResult:
    """Results of the fixed payment plan analysis."""

    purchase_amount: float
    num_payments: int
    monthly_payment: float
    monthly_fee: float
    total_cost: float
    total_fees: float
    equivalent_apr: float
    regular_interest_paid: float
    regular_total_cost: float
    regular_payments: int
    difference: float
    balance_schedule: list[MonthlyScheduleData]
    high_cost_months: list[
        tuple[int, float, float]
    ]  # (month, balance, effective_monthly_rate)
    optimal_payoff_month: int | None = None
    remaining_balance_at_optimal: float | None = None


def calculate_equivalent_apr(
    principal: float, monthly_payment: float, num_payments: int
) -> float:
    """
    Calculate the equivalent APR for a fixed payment plan.
    This is the APR that would result in the same total cost as the fixed payment plan.

    Args:
        principal: The initial loan amount
        monthly_payment: The actual monthly payment in the fixed payment plan (including any fees)
        num_payments: Number of monthly payments

    Returns:
        The equivalent APR as a percentage
    """
    # Use binary search to find the monthly interest rate
    # Payment = Principal * (rate * (1 + rate)^n) / ((1 + rate)^n - 1)
    # We need to solve for rate, which requires an iterative approach

    # Set bounds for binary search
    low_rate = (
        0.000001  # Start with a very small positive rate to avoid division by zero
    )
    high_rate = 1.0  # 100% monthly rate as upper bound

    # Perform binary search to find the rate
    for i in range(100):  # Limit iterations
        mid_rate = (low_rate + high_rate) / 2.0

        # Calculate the payment based on this rate using the loan payment formula
        if mid_rate == 0:
            # If rate is 0, payment is just principal divided by number of payments
            calculated_payment = principal / num_payments
        else:
            # Calculate denominator carefully to avoid division by zero
            denominator = (1 + mid_rate) ** num_payments - 1
            if abs(denominator) < 1e-10:  # Avoid division by zero
                # If denominator is too close to zero, adjust the search range
                high_rate = mid_rate
                continue

            calculated_payment = (
                principal * (mid_rate * (1 + mid_rate) ** num_payments) / denominator
            )

        if calculated_payment < monthly_payment:
            low_rate = mid_rate
        else:
            high_rate = mid_rate

    monthly_rate = (low_rate + high_rate) / 2.0
    apr = monthly_rate * 12 * 100  # Convert to annual percentage rate

    return apr


def calculate_regular_interest(
    principal: float, apr: float, monthly_payment: float
) -> tuple[float, int]:
    """
    Calculate how much interest would be paid with regular APR over time.

    Args:
        principal: The initial loan amount
        apr: Annual percentage rate as percentage (e.g., 27 for 27%)
        monthly_payment: Monthly payment amount

    Returns:
        Tuple of (total_interest_paid, number_of_payments)
    """
    monthly_rate = apr / 100 / 12
    balance = principal
    total_paid = 0
    payments = 0

    while balance > 0.01:  # Continue until balance is nearly paid off
        interest = balance * monthly_rate
        principal_payment = monthly_payment - interest

        # Ensure we don't pay more principal than the remaining balance
        if principal_payment > balance:
            principal_payment = balance

        balance -= principal_payment
        total_paid += monthly_payment
        payments += 1

        # Safety check to prevent infinite loop
        if payments > 1000:
            break

    total_interest = total_paid - principal
    return total_interest, payments


def calculate_balance_schedule(
    purchase_amount: float,
    monthly_payment: float,
    monthly_fee: float,
    num_payments: int,
    regular_apr: float = 27.0,
) -> list[MonthlyScheduleData]:
    """
    Calculate the balance reduction schedule for the fixed payment plan.
    Returns a list of MonthlyScheduleData objects.
    """
    balance = purchase_amount
    schedule = []

    # Calculate monthly interest rate for regular APR
    monthly_regular_rate = regular_apr / 100 / 12

    for month in range(1, num_payments + 1):
        # In the fixed payment plan, each payment is split between principal and fee
        principal_payment = monthly_payment - monthly_fee
        balance -= principal_payment

        # If we've paid off the balance early, stop
        if balance <= 0:
            balance = 0
            schedule.append(
                MonthlyScheduleData(
                    month=month,
                    balance=balance,
                    principal_payment=principal_payment + balance,
                    fee=monthly_fee,
                    effective_monthly_rate=0,
                    regular_interest_equivalent=0,
                )
            )
            break

        # Calculate effective monthly rate based on fee vs remaining balance
        effective_monthly_rate = (
            (monthly_fee / balance) * 100 if balance > 0.01 else 0
        )  # Avoid division by very small numbers

        # Calculate what interest would be charged at regular APR on this balance
        regular_interest_equivalent = balance * monthly_regular_rate

        schedule.append(
            MonthlyScheduleData(
                month=month,
                balance=balance,
                principal_payment=principal_payment,
                fee=monthly_fee,
                effective_monthly_rate=effective_monthly_rate,
                regular_interest_equivalent=regular_interest_equivalent,
            )
        )

    return schedule


def analyze_fixed_payment_plan(
    payment_plan: PaymentPlan, regular_apr: float = 27.0
) -> AnalysisResult:
    """
    Analyze a fixed payment plan and compare with regular interest charges.

    Args:
        payment_plan: The fixed payment plan to analyze
        regular_apr: The regular APR to compare against (default 27%)

    Returns:
        AnalysisResult with detailed analysis
    """
    total_cost = payment_plan.monthly_payment * payment_plan.num_payments
    total_fees = payment_plan.monthly_fee * payment_plan.num_payments

    # Calculate equivalent APR for the total payment (including fees)
    # This represents the effective cost of the fixed payment plan
    equivalent_apr = calculate_equivalent_apr(
        payment_plan.purchase_amount,
        payment_plan.monthly_payment,
        payment_plan.num_payments,
    )

    # Calculate what would happen with regular APR
    principal_monthly_payment = payment_plan.monthly_payment - payment_plan.monthly_fee
    regular_interest_paid, regular_payments = calculate_regular_interest(
        payment_plan.purchase_amount, regular_apr, principal_monthly_payment
    )
    regular_total_cost = payment_plan.purchase_amount + regular_interest_paid

    # Calculate difference
    difference = total_cost - regular_total_cost

    # Calculate balance schedule and optimal payoff analysis
    schedule = calculate_balance_schedule(
        payment_plan.purchase_amount,
        payment_plan.monthly_payment,
        payment_plan.monthly_fee,
        payment_plan.num_payments,
        regular_apr,
    )

    # Find when the effective rate exceeds the regular APR
    regular_apr_monthly = regular_apr / 12  # Convert annual to monthly
    high_cost_months = [
        (entry.month, entry.balance, entry.effective_monthly_rate)
        for entry in schedule
        if entry.effective_monthly_rate > regular_apr_monthly
    ]

    # Determine optimal payoff time
    optimal_payoff_month = None
    remaining_balance_at_optimal = None
    if high_cost_months:
        optimal_payoff_month = (
            high_cost_months[0][0] - 1
        )  # Pay off before the first high-cost month
        if optimal_payoff_month > 0:
            matching_entry = next(
                (entry for entry in schedule if entry.month == optimal_payoff_month),
                None,
            )
            remaining_balance_at_optimal = (
                matching_entry.balance if matching_entry else 0
            )

    return AnalysisResult(
        purchase_amount=payment_plan.purchase_amount,
        num_payments=payment_plan.num_payments,
        monthly_payment=payment_plan.monthly_payment,
        monthly_fee=payment_plan.monthly_fee,
        total_cost=total_cost,
        total_fees=total_fees,
        equivalent_apr=equivalent_apr,
        regular_interest_paid=regular_interest_paid,
        regular_total_cost=regular_total_cost,
        regular_payments=regular_payments,
        difference=difference,
        balance_schedule=schedule,
        high_cost_months=high_cost_months,
        optimal_payoff_month=optimal_payoff_month,
        remaining_balance_at_optimal=remaining_balance_at_optimal,
    )


def print_analysis(
    result: AnalysisResult,
    regular_apr: float = 27.0,
    markdown_format: bool = False,
    plan_number: int = 1,
):
    """Print a formatted analysis of the fixed payment plan."""
    if markdown_format:
        print(f"\n# Fixed Payment Plan Analysis #{plan_number}")
        print(f"- Purchase Amount: ${result.purchase_amount:.2f}")
        print(f"- Number of Payments: {result.num_payments}")
        print(f"- Monthly Payment: ${result.monthly_payment:.2f}")
        print(f"- Monthly Fee: ${result.monthly_fee:.2f}")
        print(f"- Total Cost: ${result.total_cost:.2f}")
        print(f"- Total Fees: ${result.total_fees:.2f}")
        print(f"- Equivalent APR: {result.equivalent_apr:.2f}%")
        print(f"\n## Comparison with Regular {regular_apr}% APR")
        print(f"- Regular Interest Paid: ${result.regular_interest_paid:.2f}")
        print(f"- Regular Total Cost: ${result.regular_total_cost:.2f}")
        print(f"- Regular Payments Needed: {result.regular_payments}")
        print(f"- Difference (Fixed Plan - Regular): ${result.difference:.2f}")

        if result.difference > 0:
            print(
                f"- The fixed payment plan costs ${result.difference:.2f} more than regular payments."
            )
        else:
            print(
                f"- The fixed payment plan saves ${abs(result.difference):.2f} compared to regular payments."
            )

        # Additional analysis
        print(f"\n## Additional Analysis")
        simple_interest_rate = (
            (result.total_cost - result.purchase_amount) / result.purchase_amount
        ) / (result.num_payments / 12)
        print(
            f"- Simple interest rate equivalent: {simple_interest_rate * 100:.2f}% APR"
        )
        monthly_fee_percentage = (result.monthly_fee / result.purchase_amount) * 100
        print(
            f"- Monthly fee as % of purchase: {monthly_fee_percentage:.2f}% per month"
        )

        # Effective rate based on average balance (approximate)
        avg_balance = result.purchase_amount / 2  # Rough approximation
        effective_rate_avg_balance = (
            (result.total_cost - result.purchase_amount) / avg_balance
        ) / (result.num_payments / 12)
        print(
            f"- Effective rate based on avg. balance: {effective_rate_avg_balance * 100:.2f}% APR (approximate)"
        )

        # Fee-only equivalent rate - what rate would generate the same fees if applied to declining balance
        total_fees = result.monthly_fee * result.num_payments
        avg_balance_for_fees = (
            result.purchase_amount / 2
        )  # Average balance over the term
        fee_equivalent_rate = (total_fees / avg_balance_for_fees) / (
            result.num_payments / 12
        )
        print(
            f"- Fee-only equivalent rate (on avg. balance): {fee_equivalent_rate * 100:.2f}% APR"
        )

        # Calculate and show the balance schedule and optimal payoff analysis
        print(f"\n## Balance Schedule and Optimal Payoff Analysis")
        schedule = result.balance_schedule

        # Show all months (no elision) in a table format
        print(
            "| Month | Balance | Fixed Fee | Regular Interest* | Difference | Effective Rate | APR Equivalent |"
        )
        print(
            "|-------|---------|-----------|------------------|------------|----------------|----------------|"
        )
        for entry in schedule:
            annualized_rate = (
                entry.effective_monthly_rate * 12
            )  # Convert monthly rate to APR
            difference = entry.fee - entry.regular_interest_equivalent
            print(
                f"| {entry.month:2d} | ${entry.balance:8.2f} | ${entry.fee:7.2f} | ${entry.regular_interest_equivalent:7.2f} | ${difference:7.2f} | {entry.effective_monthly_rate:5.2f}% monthly | {annualized_rate:5.2f}% |"
            )

            # Check if this is the optimal payoff month (the month before fees exceed regular interest)
            is_optimal_payoff_month = (
                result.optimal_payoff_month is not None
                and entry.month == result.optimal_payoff_month
            )
            if is_optimal_payoff_month:
                print(
                    f"| **OPTIMAL PAYOFF POINT: After month {entry.month}, pay remaining ${result.remaining_balance_at_optimal:.2f}** |"
                )

        print(
            f"\n*Regular interest calculated at {regular_apr}% APR on remaining balance"
        )

        # Find when the effective rate exceeds the regular APR
        high_cost_months = result.high_cost_months
        if high_cost_months:
            print(
                f"\n### Months where fee rate exceeds regular {regular_apr}% APR ({regular_apr / 12:.2f}% monthly):"
            )
            print(
                "| Month | Rate | APR | Balance | Fixed Fee | Regular Interest | Difference |"
            )
            print(
                "|-------|------|-----|---------|-----------|------------------|------------|"
            )
            for (
                month,
                balance,
                effective_rate,
            ) in high_cost_months:  # Show all, no limit
                # Find the regular interest for this month from the schedule
                month_entry = next(
                    (entry for entry in schedule if entry.month == month), None
                )
                if month_entry:
                    regular_interest_equivalent = (
                        month_entry.regular_interest_equivalent
                    )
                    difference = (
                        month_entry.fee - regular_interest_equivalent
                    )  # fee - regular_interest
                    annualized_rate = effective_rate * 12  # Convert monthly rate to APR
                    print(
                        f"| {month} | {effective_rate:.2f}% monthly | {annualized_rate:.2f}% | ${balance:.2f} | ${month_entry.fee:7.2f} | ${regular_interest_equivalent:7.2f} | ${difference:7.2f} |"
                    )

            # Suggest optimal payoff time
            if (
                result.optimal_payoff_month is not None
                and result.remaining_balance_at_optimal is not None
            ):
                # Get the regular interest for the optimal payoff month
                optimal_month_entry = (
                    next(
                        (
                            entry
                            for entry in schedule
                            if entry.month == result.optimal_payoff_month
                        ),
                        None,
                    )
                    if result.optimal_payoff_month
                    else None
                )
                if optimal_month_entry:
                    print(f"\n### Optimal Payoff Recommendation:")
                    print(
                        f"- Suggested optimal payoff: After month {result.optimal_payoff_month}, pay remaining ${result.remaining_balance_at_optimal:.2f}"
                    )
                    print(
                        f"- At this point, fixed fee would be ${optimal_month_entry.fee:.2f}, regular interest would be ${optimal_month_entry.regular_interest_equivalent:.2f}"
                    )
                    print(
                        f"- This would avoid {len(high_cost_months)} months of high-cost fees."
                    )
                else:
                    print(f"\n### Optimal Payoff Recommendation:")
                    print(
                        f"- Suggested optimal payoff: After month {result.optimal_payoff_month}, pay remaining ${result.remaining_balance_at_optimal:.2f}"
                    )
                    print(
                        f"- This would avoid {len(high_cost_months)} months of high-cost fees."
                    )
    else:
        print(f"\n--- Fixed Payment Plan Analysis ---")
        print(f"Purchase Amount: ${result.purchase_amount:.2f}")
        print(f"Number of Payments: {result.num_payments}")
        print(f"Monthly Payment: ${result.monthly_payment:.2f}")
        print(f"Monthly Fee: ${result.monthly_fee:.2f}")
        print(f"Total Cost: ${result.total_cost:.2f}")
        print(f"Total Fees: ${result.total_fees:.2f}")
        print(f"Equivalent APR: {result.equivalent_apr:.2f}%")
        print(f"\n--- Comparison with Regular {regular_apr}% APR ---")
        print(f"Regular Interest Paid: ${result.regular_interest_paid:.2f}")
        print(f"Regular Total Cost: ${result.regular_total_cost:.2f}")
        print(f"Regular Payments Needed: {result.regular_payments}")
        print(f"Difference (Fixed Plan - Regular): ${result.difference:.2f}")

        if result.difference > 0:
            print(
                f"The fixed payment plan costs ${result.difference:.2f} more than regular payments."
            )
        else:
            print(
                f"The fixed payment plan saves ${abs(result.difference):.2f} compared to regular payments."
            )

        # Additional analysis
        print(f"\n--- Additional Analysis ---")
        simple_interest_rate = (
            (result.total_cost - result.purchase_amount) / result.purchase_amount
        ) / (result.num_payments / 12)
        print(f"Simple interest rate equivalent: {simple_interest_rate * 100:.2f}% APR")
        monthly_fee_percentage = (result.monthly_fee / result.purchase_amount) * 100
        print(f"Monthly fee as % of purchase: {monthly_fee_percentage:.2f}% per month")

        # Effective rate based on average balance (approximate)
        avg_balance = result.purchase_amount / 2  # Rough approximation
        effective_rate_avg_balance = (
            (result.total_cost - result.purchase_amount) / avg_balance
        ) / (result.num_payments / 12)
        print(
            f"Effective rate based on avg. balance: {effective_rate_avg_balance * 100:.2f}% APR (approximate)"
        )

        # Fee-only equivalent rate - what rate would generate the same fees if applied to declining balance
        total_fees = result.monthly_fee * result.num_payments
        avg_balance_for_fees = (
            result.purchase_amount / 2
        )  # Average balance over the term
        fee_equivalent_rate = (total_fees / avg_balance_for_fees) / (
            result.num_payments / 12
        )
        print(
            f"Fee-only equivalent rate (on avg. balance): {fee_equivalent_rate * 100:.2f}% APR"
        )

        # Calculate and show the balance schedule and optimal payoff analysis
        print(f"\n--- Balance Schedule and Optimal Payoff Analysis ---")
        schedule = result.balance_schedule

        # Show all months (no elision)
        print(
            "Month | Balance  | Fixed Fee | Regular Interest | Difference | Effective Rate"
        )
        print(
            "------|----------|-----------|------------------|------------|---------------"
        )
        for entry in schedule:
            annualized_rate = (
                entry.effective_monthly_rate * 12
            )  # Convert monthly rate to APR
            difference = entry.fee - entry.regular_interest_equivalent
            print(
                f"{entry.month:5d} | ${entry.balance:7.2f} | ${entry.fee:7.2f} | ${entry.regular_interest_equivalent:7.2f} | ${difference:7.2f} | {entry.effective_monthly_rate:5.2f}% monthly ({annualized_rate:5.2f}% APR)"
            )

            # Check if this is the optimal payoff month (the month before fees exceed regular interest)
            is_optimal_payoff_month = (
                result.optimal_payoff_month is not None
                and entry.month == result.optimal_payoff_month
            )
            if is_optimal_payoff_month:
                print(
                    f"      >>> OPTIMAL PAYOFF POINT: After month {entry.month}, pay remaining ${result.remaining_balance_at_optimal:.2f}"
                )

        print(
            f"      *Regular interest calculated at {regular_apr}% APR on remaining balance"
        )

        # Find when the effective rate exceeds the regular APR
        high_cost_months = result.high_cost_months
        if high_cost_months:
            print(
                f"\nMonths where fee rate exceeds regular {regular_apr}% APR ({regular_apr / 12:.2f}% monthly):"
            )
            for (
                month,
                balance,
                effective_rate,
            ) in high_cost_months:  # Show all, no limit
                # Find the regular interest for this month from the schedule
                month_entry = next(
                    (entry for entry in schedule if entry.month == month), None
                )
                if month_entry:
                    difference = (
                        month_entry.fee - month_entry.regular_interest_equivalent
                    )
                    annualized_rate = effective_rate * 12  # Convert monthly rate to APR
                    print(
                        f"  Month {month}: {effective_rate:.2f}% monthly ({annualized_rate:.2f}% APR) on ${balance:.2f} balance"
                    )
                    print(
                        f"    Fixed fee: ${month_entry.fee:.2f}, Regular interest: ${month_entry.regular_interest_equivalent:.2f}, Difference: ${difference:.2f}"
                    )

            # Suggest optimal payoff time
            if (
                result.optimal_payoff_month is not None
                and result.remaining_balance_at_optimal is not None
            ):
                # Get the regular interest for the optimal payoff month
                optimal_month_entry = (
                    next(
                        (
                            entry
                            for entry in schedule
                            if entry.month == result.optimal_payoff_month
                        ),
                        None,
                    )
                    if result.optimal_payoff_month
                    else None
                )
                if optimal_month_entry:
                    print(
                        f"\nSuggested optimal payoff: After month {result.optimal_payoff_month}, pay remaining ${result.remaining_balance_at_optimal:.2f}"
                    )
                    print(
                        f"At this point, fixed fee would be ${optimal_month_entry.fee:.2f}, regular interest would be ${optimal_month_entry.regular_interest_equivalent:.2f}"
                    )
                    print(
                        f"This would avoid {len(high_cost_months)} months of high-cost fees."
                    )
                else:
                    print(
                        f"\nSuggested optimal payoff: After month {result.optimal_payoff_month}, pay remaining ${result.remaining_balance_at_optimal:.2f}"
                    )
                    print(
                        f"This would avoid {len(high_cost_months)} months of high-cost fees."
                    )


def run_analysis_from_config(config_path: str, markdown_format: bool = False):
    """Run analysis using configuration from a file."""
    config = load_config(config_path)

    regular_apr = config.get("regular_apr", 27.0)

    for i, plan_data in enumerate(config["payment_plans"], 1):
        if not markdown_format:
            print(f"\n{'=' * 50}")
            print(f"ANALYSIS #{i}")
            print(f"{'=' * 50}")
        else:
            # Add separator in markdown format
            if i > 1:  # Add separator after the first plan
                print(f"\n---\n")  # Add separator between plans in markdown

        payment_plan = PaymentPlan(**plan_data)
        result = analyze_fixed_payment_plan(payment_plan, regular_apr)
        print_analysis(result, regular_apr, markdown_format, i)


def main():
    """Main function to run the finance calculator."""
    print("Finance Calculator Utility")
    print("=" * 50)

    # Check if help is requested
    import sys

    if len(sys.argv) > 1 and sys.argv[1] in ["-h", "--help"]:
        show_help()
        return
    elif len(sys.argv) > 1 and sys.argv[1] in ["-v", "--version"]:
        print("Finance Calculator Utility v1.1")
        return
    elif len(sys.argv) > 1:
        # Check for markdown flag
        args = sys.argv[1:]
        markdown_format = False
        config_path = None

        i = 0
        while i < len(args):
            if args[i] in ["-m", "--markdown"]:
                markdown_format = True
            elif not args[i].startswith("-"):  # Not a flag, so it's the config path
                config_path = args[i]
            i += 1

        if config_path:
            if Path(config_path).exists():
                print(f"Loading configuration from {config_path}")
                if markdown_format:
                    print("Output format: Markdown")
                run_analysis_from_config(config_path, markdown_format)
            else:
                print(f"Configuration file {config_path} not found.")
                print("Use -h for help.")
        else:
            # If no config file provided but markdown flag is there, run defaults with markdown
            if markdown_format:
                print("Running with default examples in Markdown format...")

                # Example A
                plan_a = PaymentPlan(
                    purchase_amount=1196.00,
                    num_payments=18,
                    monthly_payment=80.73,
                    monthly_fee=14.28,
                )
                result_a = analyze_fixed_payment_plan(plan_a)
                print_analysis(result_a, markdown_format=True, plan_number=1)

                # Example B
                plan_b = PaymentPlan(
                    purchase_amount=2365.20,
                    num_payments=24,
                    monthly_payment=129.14,
                    monthly_fee=30.59,
                )
                result_b = analyze_fixed_payment_plan(plan_b)
                print_analysis(result_b, markdown_format=True, plan_number=2)

                # Example C
                plan_c = PaymentPlan(
                    purchase_amount=200.00,
                    num_payments=18,
                    monthly_payment=13.51,
                    monthly_fee=2.39,
                )
                result_c = analyze_fixed_payment_plan(plan_c)
                print_analysis(result_c, markdown_format=True, plan_number=3)
            else:
                show_help()
    else:
        # Example usage with the provided data
        print("Running with default examples...")

        # Example A
        plan_a = PaymentPlan(
            purchase_amount=1196.00,
            num_payments=18,
            monthly_payment=80.73,
            monthly_fee=14.28,
        )
        result_a = analyze_fixed_payment_plan(plan_a)
        print_analysis(result_a)

        # Example B
        plan_b = PaymentPlan(
            purchase_amount=2365.20,
            num_payments=24,
            monthly_payment=129.14,
            monthly_fee=30.59,
        )
        result_b = analyze_fixed_payment_plan(plan_b)
        print_analysis(result_b)

        # Example C
        plan_c = PaymentPlan(
            purchase_amount=200.00,
            num_payments=18,
            monthly_payment=13.51,
            monthly_fee=2.39,
        )
        result_c = analyze_fixed_payment_plan(plan_c)
        print_analysis(result_c)


def load_config(config_path: str) -> dict:
    """Load configuration from a JSON file."""
    with open(config_path) as f:
        return json.load(f)


def show_help():
    """Display help information."""
    help_text = """
Finance Calculator Utility - Help

Usage:
  python finance_calculator.py [OPTIONS] [CONFIG_FILE]

Options:
  -h, --help          Show this help message and exit
  -v, --version       Show version information
  -m, --markdown      Output results in Markdown format for easy copying to documents

Arguments:
  CONFIG_FILE         Path to JSON configuration file with payment plan data
                      If not provided, runs with default examples

Configuration File Format:
  {
    "regular_apr": 27.0,
    "payment_plans": [
      {
        "purchase_amount": 1196.00,
        "num_payments": 18,
        "monthly_payment": 80.73,
        "monthly_fee": 14.28
      }
    ]
  }

Examples:
  python finance_calculator.py                    # Run with default examples
  python finance_calculator.py config.json        # Run with custom config
  python finance_calculator.py -m                 # Run with default examples in Markdown format
  python finance_calculator.py -m config.json     # Run with custom config in Markdown format
  python finance_calculator.py -h                 # Show help

The utility analyzes fixed payment plans and compares them to regular interest rates,
identifies optimal payoff timing, and shows the effective APR of fixed fees.
"""
    print(help_text)


if __name__ == "__main__":
    main()
