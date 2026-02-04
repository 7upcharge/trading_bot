import logging
from .validators import validate_inputs


logger = logging.getLogger(__name__)

def place_order(
    client,
    symbol: str,
    side: str,
    order_type: str,
    quantity: float,
    price: float = None,
):
    validate_inputs(order_type, price)

    order = {
        "symbol": symbol,
        "side": side,
        "type": order_type,
        "quantity": quantity,
    }

    if order_type == "LIMIT":
        order["price"] = price
        order["timeInForce"] = "GTC"

    return client.place_order(**order)

