import argparse
from client import BinanceFuturesClient
from logger import setup_logger

def main():
    parser = argparse.ArgumentParser(description="Binance Futures Testnet Trading Bot")
    parser.add_argument("--symbol", required=True, help="Trading pair, e.g. BTCUSDT")
    parser.add_argument("--side", required=True, choices=["BUY", "SELL"], help="Order side")
    parser.add_argument("--type", required=True, choices=["MARKET", "LIMIT"], help="Order type")
    parser.add_argument("--quantity", required=True, type=float, help="Order quantity")
    parser.add_argument("--price", type=float, help="Order price (required for LIMIT)")
    args = parser.parse_args()

    logger = setup_logger()
    client = BinanceFuturesClient(
        api_key="YOUR_API_KEY",
        api_secret="YOUR_API_SECRET",
        base_url="https://testnet.binancefuture.com",
        logger=logger
    )

    if args.type == "LIMIT" and not args.price:
        parser.error("--price is required for LIMIT orders")

    try:
        order = client.place_order(args.symbol, args.side, args.type, args.quantity, args.price)
        print("✅ Order placed successfully!")
        print(f"Order ID: {order['orderId']}")
        print(f"Status: {order['status']}")
        print(f"Executed Qty: {order.get('executedQty')}")
        print(f"Avg Price: {order.get('avgPrice')}")
    except Exception as e:
        print(f"❌ Failed to place order: {e}")

if __name__ == "__main__":
    main()
