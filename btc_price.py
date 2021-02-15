import asyncio
import json
import urllib.request
import ssl
import iterm2

async def main(connection):
    component = iterm2.StatusBarComponent(
        short_description='Bitcoin Price',
        detailed_description='Displays current price of Bitcoin',
        exemplar='BTC $9,921.50',
        update_cadence=30,
        identifier='schnogz.iterm-crypto-components.btc-price',
        knobs=[],
    )

    @iterm2.StatusBarRPC
    async def bitcoin_price_coroutine(knobs):
        price_url = 'https://api.blockchair.com/bitcoin/stats'

        try:
            context = ssl._create_unverified_context()
            request = urllib.request.Request(
                price_url,
                headers={},
            )
            price = format(round(json.loads(
                urllib.request.urlopen(request, context=context).read().decode()
            )['data']['market_price_usd'], 2), ',')
        except:
            raise
        else:
            return f'BTC ${price}'

    await component.async_register(connection, bitcoin_price_coroutine)

iterm2.run_forever(main)
