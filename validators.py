def validate_inputs(order_type, price):
    if order_type == "LIMIT" and price is None:
        raise ValueError("LIMIT order requires --price")

    if order_type == "MARKET" and price is not None:
        raise ValueError("MARKET order must not include --price")
