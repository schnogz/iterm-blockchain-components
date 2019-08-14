import asyncio
import json
import urllib.request

import iterm2

async def main(connection):
    github_repo = None

    component = iterm2.StatusBarComponent(
        short_description='Bitcoin Price',
        detailed_description='Displays current price of Bitcoin',
        exemplar='₿ $9,921.50',
        update_cadence=30,
        identifier='schnogz.iterm-btc-components.btc-price',
        knobs=[],
    )

    @iterm2.StatusBarRPC
    async def bitcoin_price_coroutine(knobs):
        price_url = 'https://api.blockchain.info/stats'

        try:
            request = urllib.request.Request(
                price_url,
                headers={},
            )
            price = json.loads(
                urllib.request.urlopen(request).read().decode()
            )['market_price_usd']
            formatted_price = format(price, ',')
        except:
            raise
        else:
            return f'₿ ${formatted_price}'

    await component.async_register(connection, bitcoin_price_coroutine)

iterm2.run_forever(main)
