import logging
from binance.client import Client
from binance.exceptions import BinanceAPIException

logger = logging.getLogger(__name__)

TESTNET_URL = "https://testnet.binancefuture.com"

class BinanceFuturesClient:
    def __init__(self, api_key: str, api_secret: str):
        self.client = Client(api_key, api_secret)
        self.client.FUTURES_URL = TESTNET_URL

    def place_order(self, **order_params):
        try:
            logger.info(f"API Request: {order_params}")
            response = self.client.futures_create_order(**order_params)
            logger.info(f"API Response: {response}")
            return response
        except BinanceAPIException as e:
            logger.error(f"Binance API Error: {e.message}")
            raise
        except Exception as e:
            logger.exception("Unexpected error")
            raise
