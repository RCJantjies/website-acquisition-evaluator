"""Website Acquisition Evaluator.

A command-line tool for calculating core financial metrics used when
screening a content website or other online business for acquisition.
"""


def calculate_metrics(
    monthly_revenue: float,
    monthly_expenses: float,
    asking_price: float,
    monthly_pageviews: int,
) -> dict[str, float]:
    """Calculate basic profitability and valuation metrics."""
    if monthly_revenue < 0 or monthly_expenses < 0 or asking_price < 0:
        raise ValueError("Financial inputs cannot be negative.")
    if monthly_pageviews < 0:
        raise ValueError("Monthly pageviews cannot be negative.")

    monthly_profit = monthly_revenue - monthly_expenses
    annual_profit = monthly_profit * 12
    profit_multiple = asking_price / annual_profit if annual_profit > 0 else float("inf")
    payback_months = asking_price / monthly_profit if monthly_profit > 0 else float("inf")
    revenue_per_1000_views = (
        monthly_revenue / monthly_pageviews * 1000 if monthly_pageviews > 0 else 0.0
    )

    return {
        "monthly_profit": monthly_profit,
        "annual_profit": annual_profit,
        "profit_multiple": profit_multiple,
        "payback_months": payback_months,
        "revenue_per_1000_views": revenue_per_1000_views,
    }


def get_number(prompt: str) -> float:
    """Read a non-negative number from the command line."""
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("Please enter a value of zero or greater.")
                continue
            return value
        except ValueError:
            print("Please enter a valid number.")


def main() -> None:
    """Run the interactive command-line evaluator."""
    print("Website Acquisition Evaluator")
    print("-" * 29)

    revenue = get_number("Monthly revenue: $")
    expenses = get_number("Monthly expenses: $")
    asking_price = get_number("Asking price: $")
    pageviews = int(get_number("Monthly pageviews: "))

    metrics = calculate_metrics(revenue, expenses, asking_price, pageviews)

    print("\nAcquisition Summary")
    print("-" * 19)
    print(f"Monthly profit:       ${metrics['monthly_profit']:,.2f}")
    print(f"Annualized profit:    ${metrics['annual_profit']:,.2f}")
    print(f"Profit multiple:      {metrics['profit_multiple']:.2f}x")
    print(f"Simple payback:       {metrics['payback_months']:.1f} months")
    print(f"Revenue per 1K views: ${metrics['revenue_per_1000_views']:,.2f}")


if __name__ == "__main__":
    main()
