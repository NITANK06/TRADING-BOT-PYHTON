from binance.client import Client
from binance.enums import *

class BinanceFuturesClient:
    def __init__(self, api_key, api_secret, base_url, logger):
        self.client = Client(api_key, api_secret, testnet=True)
        self.client.API_URL = base_url
        self.logger = logger

    def place_order(self, symbol, side, order_type, quantity, price=None):
        try:
            self.logger.info(f"Placing order: {symbol}, {side}, {order_type}, qty={quantity}, price={price}")
            if order_type == "MARKET":
                order = self.client.futures_create_order(
                    symbol=symbol,
                    side=SIDE_BUY if side == "BUY" else SIDE_SELL,
                    type=ORDER_TYPE_MARKET,
                    quantity=quantity
                )
            elif order_type == "LIMIT":
                order = self.client.futures_create_order(
                    symbol=symbol,
                    side=SIDE_BUY if side == "BUY" else SIDE_SELL,
                    type=ORDER_TYPE_LIMIT,
                    timeInForce=TIME_IN_FORCE_GTC,
                    quantity=quantity,
                    price=price
                )
            else:
                raise ValueError("Invalid order type")

            self.logger.info(f"Order response: {order}")
            return order
        except Exception as e:
            self.logger.error(f"Error placing order: {e}")
            raise
