import unittest
from decimal import Decimal

from offer_math import QuoteLine, calculate_quote_line


class QuoteMathTest(unittest.TestCase):
    def test_discounts_are_sequential_and_vat_uses_discounted_net(self):
        line = calculate_quote_line(
            Decimal("3"), Decimal("12.35"), Decimal("10"), Decimal("5"), "23"
        )
        self.assertEqual(line, QuoteLine(3705, 537, 3168, 729, 3897))

    def test_exempt_line_rounds_fractional_quantity_to_cents(self):
        line = calculate_quote_line(
            Decimal("0.5"), Decimal("1.01"), Decimal("0"), Decimal("0"), "zw"
        )
        self.assertEqual(line, QuoteLine(51, 0, 51, 0, 51))
