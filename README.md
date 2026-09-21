# Website Acquisition Evaluator

A small Python command-line tool for evaluating the basic profitability and valuation of content websites and other online businesses.

## Purpose

Online-business listings often provide headline figures such as monthly revenue, expenses, asking price, and traffic. This project converts those inputs into a consistent set of screening metrics that can support an initial acquisition review.

It is intended as a **screening tool, not investment advice or a substitute for due diligence**.

## Metrics

The evaluator calculates:

- Monthly profit
- Annualized profit
- Asking-price-to-annual-profit multiple
- Simple payback period in months
- Revenue per 1,000 pageviews

## Example

Given:

- Monthly revenue: $450
- Monthly expenses: $75
- Asking price: $9,000
- Monthly pageviews: 35,000

The evaluator returns approximately:

```text
Monthly profit:       $375.00
Annualized profit:    $4,500.00
Profit multiple:      2.00x
Simple payback:       24.0 months
Revenue per 1K views: $12.86
```

## Requirements

- Python 3.9 or later
- No third-party packages

## Run

Clone the repository and run:

```bash
python evaluator.py
```

Then enter the requested financial and traffic figures.

## Tests

The project uses Python's built-in `unittest` framework:

```bash
python -m unittest discover -s tests
```

The tests cover a standard profitable acquisition, zero traffic, a non-profitable site, and invalid negative inputs.

## Project status

**Version 0.1 — initial portfolio release**

Future iterations may add CSV analysis, additional valuation measures, risk factors, and a user interface.

## License

Released under the MIT License.
