import asyncio
import json
import urllib.request

import iterm2

async def main(connection):
    component = iterm2.StatusBarComponent(
        short_description='Bitcoin Price',
        detailed_description='Displays current price of Bitcoin',
        exemplar='₿ Price: $9,921.50',
        update_cadence=15,
        identifier='schnogz.iterm-btc-components.btc-price',
        knobs=[],
    )

    @iterm2.StatusBarRPC
    async def bitcoin_price_coroutine(knobs):
        price_url = 'https://api.blockchair.com/bitcoin/stats'

        try:
            request = urllib.request.Request(
                price_url,
                headers={},
            )
            price = format(json.loads(
                urllib.request.urlopen(request).read().decode()
            )['data']['market_price_usd'], ',')
        except:
            raise
        else:
            return f'₿ Price: ${price}'

    await component.async_register(connection, bitcoin_price_coroutine)

iterm2.run_forever(main)
