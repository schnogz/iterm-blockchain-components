import asyncio
import json
import urllib.request

import iterm2

async def main(connection):
    component = iterm2.StatusBarComponent(
        short_description='Bitcoin Cash Price',
        detailed_description='Displays current price of Bitcoin Cash',
        exemplar='BCH Price: $321.50',
        update_cadence=30,
        identifier='schnogz.iterm-crypto-components.bch-price',
        knobs=[],
    )

    @iterm2.StatusBarRPC
    async def bitcoin_cash_price_coroutine(knobs):
        price_url = 'https://api.blockchair.com/bitcoin-cash/stats'

        try:
            request = urllib.request.Request(
                price_url,
                headers={},
            )
            price = format(round(json.loads(
                urllib.request.urlopen(request).read().decode()
            )['data']['market_price_usd'], 2), ',')
        except:
            raise
        else:
            return f'BCH Price: ${price}'

    await component.async_register(connection, bitcoin_cash_price_coroutine)

iterm2.run_forever(main)
