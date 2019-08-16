import asyncio
import json
import urllib.request

import iterm2

async def main(connection):
    component = iterm2.StatusBarComponent(
        short_description='Litecoin Price',
        detailed_description='Displays current price of Litecoin',
        exemplar='LTC Price: $121.50',
        update_cadence=30,
        identifier='schnogz.iterm-crypto-components.ltc-price',
        knobs=[],
    )

    @iterm2.StatusBarRPC
    async def litecoin_price_coroutine(knobs):
        price_url = 'https://api.blockchair.com/litecoin/stats'

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
            return f'LTC Price: ${price}'

    await component.async_register(connection, litecoin_price_coroutine)

iterm2.run_forever(main)
