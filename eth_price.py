import asyncio
import json
import urllib.request
import ssl
import iterm2

async def main(connection):
    component = iterm2.StatusBarComponent(
        short_description='Ethereum Price',
        detailed_description='Displays current price of Ethereum',
        exemplar='ETH $321.50',
        update_cadence=30,
        identifier='schnogz.iterm-crypto-components.eth-price',
        knobs=[],
    )

    @iterm2.StatusBarRPC
    async def ethereum_price_coroutine(knobs):
        price_url = 'https://api.blockchair.com/ethereum/stats'

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
            return f'ETH ${price}'

    await component.async_register(connection, ethereum_price_coroutine)

iterm2.run_forever(main)
