import asyncio
import json
import urllib.request

import iterm2

async def main(connection):
    component = iterm2.StatusBarComponent(
        short_description='Market Prices',
        detailed_description='Displays current prices of BTC, ETH, BCH and LTC',
        exemplar='BTC $10,321.50, ETH $321.42, BCH $471.03, LTC $104.53',
        update_cadence=15,
        identifier='schnogz.iterm-crypto-components.bch-price',
        knobs=[],
    )

    @iterm2.StatusBarRPC
    async def market_prices_coroutine(knobs):
        price_url = 'https://api.blockchair.com/stats'

        try:
            request = urllib.request.Request(
                price_url,
                headers={},
            )
            resp = json.loads(
                urllib.request.urlopen(request).read().decode()
            )['data']
            btc_price = format(round(resp['bitcoin']['data']['market_price_usd'], 2), ',')
            eth_price = format(round(resp['ethereum']['data']['market_price_usd'], 2), ',')
            bch_price = format(round(resp['bitcoin-cash']['data']['market_price_usd'], 2), ',')
            ltc_price = format(round(resp['litecoin']['data']['market_price_usd'], 2), ',')
        except:
            raise
        else:
            return f'BTC ${btc_price}  ETH ${eth_price} BCH ${bch_price}  LTC ${ltc_price}'

    await component.async_register(connection, market_prices_coroutine)

iterm2.run_forever(main)
