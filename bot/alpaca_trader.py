from alpaca.trading.client import TradingClient
from alpaca.trading.requests import GetAssetsRequest
import settings

trading_client = TradingClient(api_key=settings.ALPACA_KEY, secret_key=settings.ALPACA_SECRET)

# Get our account information.
account = trading_client.get_account()

# Check if our account is restricted from trading.
if account.trading_blocked:
    print('Account is currently restricted from trading.')

# Check how much money we can use to open new positions.
print('${} is available as buying power.'.format(account.buying_power))

balance_change = float(account.equity) - float(account.last_equity)
print(f'Today\'s portfolio balance change: ${balance_change}')