def format_currency(amount):
    return f"₹ {amount:,.2f}"


def calculate_total(price, qty):
    return price * qty


def apply_discount(amount, percent):
    return amount - (amount * percent / 100)
