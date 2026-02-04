import argparse
import os
import logging
from dotenv import load_dotenv

from bot.client import BinanceFuturesClient
from bot.orders import place_order
from bot.logging_config import setup_logging

def main():
    setup_logging()
    logger = logging.getLogger(__name__)
    load_dotenv()

    parser = argparse.ArgumentParser(
        description="Binance Futures Testnet Trading Bot"
    )

    parser.add_argument("--symbol", required=True, help="e.g. BTCUSDT")
    parser.add_argument("--side", required=True, choices=["BUY", "SELL"])
    parser.add_argument("--type", required=True, choices=["MARKET", "LIMIT"])
    parser.add_argument("--quantity", required=True, type=float)
    parser.add_argument("--price", type=float)

    args = parser.parse_args()

    print("\n📌 ORDER REQUEST")
    print("----------------")
    print(f"Symbol   : {args.symbol}")
    print(f"Side     : {args.side}")
    print(f"Type     : {args.type}")
    print(f"Quantity : {args.quantity}")
    print(f"Price    : {args.price}")

    client = BinanceFuturesClient(
        api_key=os.getenv("BINANCE_API_KEY"),
        api_secret=os.getenv("BINANCE_API_SECRET"),
    )

    try:
        response = place_order(
            client=client,
            symbol=args.symbol,
            side=args.side,
            order_type=args.type,
            quantity=args.quantity,
            price=args.price,
        )

        print("\n✅ ORDER SUCCESS")
        print("----------------")
        print(f"Order ID     : {response.get('orderId')}")
        print(f"Status       : {response.get('status')}")
        print(f"Executed Qty : {response.get('executedQty')}")
        print(f"Avg Price    : {response.get('avgPrice', 'N/A')}")

    except Exception as e:
        logger.error(str(e))
        print("\n❌ ORDER FAILED")
        print(str(e))

if __name__ == "__main__":
    main()
