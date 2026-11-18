from dataclasses import dataclass
from decimal import Decimal, ROUND_HALF_UP


@dataclass(frozen=True)
class QuoteLine:
    subtotal_cents: int
    discount_cents: int
    net_cents: int
    vat_cents: int
    gross_cents: int


def rounded_cents(value: Decimal) -> int:
    return int(value.quantize(Decimal("1"), rounding=ROUND_HALF_UP))


def calculate_quote_line(
    quantity: Decimal,
    unit_price: Decimal,
    line_discount_pct: Decimal,
    offer_discount_pct: Decimal,
    vat_rate: str,
) -> QuoteLine:
    """Calculate one validated quote line using the CRM's rounding order."""
    subtotal = rounded_cents(quantity * unit_price * 100)
    after_line_discount = rounded_cents(Decimal(subtotal) * (1 - line_discount_pct / 100))
    net = rounded_cents(Decimal(after_line_discount) * (1 - offer_discount_pct / 100))
    vat = rounded_cents(Decimal(net) * Decimal(vat_rate) / 100) if vat_rate != "zw" else 0
    return QuoteLine(subtotal, subtotal - net, net, vat, net + vat)
