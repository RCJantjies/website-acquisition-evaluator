"""Tests for the Website Acquisition Evaluator."""

import math
import unittest

from evaluator import calculate_metrics


class TestCalculateMetrics(unittest.TestCase):
    """Test the core acquisition calculations."""

    def test_standard_acquisition(self) -> None:
        metrics = calculate_metrics(450, 75, 9000, 35000)

        self.assertEqual(metrics["monthly_profit"], 375)
        self.assertEqual(metrics["annual_profit"], 4500)
        self.assertAlmostEqual(metrics["profit_multiple"], 2.0)
        self.assertAlmostEqual(metrics["payback_months"], 24.0)
        self.assertAlmostEqual(metrics["revenue_per_1000_views"], 12.8571428571)

    def test_zero_pageviews(self) -> None:
        metrics = calculate_metrics(100, 20, 1000, 0)
        self.assertEqual(metrics["revenue_per_1000_views"], 0.0)

    def test_non_profitable_site(self) -> None:
        metrics = calculate_metrics(100, 150, 1000, 5000)
        self.assertTrue(math.isinf(metrics["profit_multiple"]))
        self.assertTrue(math.isinf(metrics["payback_months"]))

    def test_negative_input_rejected(self) -> None:
        with self.assertRaises(ValueError):
            calculate_metrics(-1, 0, 0, 0)


if __name__ == "__main__":
    unittest.main()
