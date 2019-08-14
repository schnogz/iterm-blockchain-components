import asyncio
import json
import urllib.request

import iterm2

async def main(connection):
    component = iterm2.StatusBarComponent(
        short_description='Bitcoin Mempool Stats',
        detailed_description='Displays BTC mempool size and unconfirmed transactions count',
        exemplar='BTC Mempool: 4,239 unconfirmed txs @ 1.03 MB',
        update_cadence=60,
        identifier='schnogz.iterm-crypto-components.btc-mempool',
        knobs=[],
    )

    @iterm2.StatusBarRPC
    async def btc_mempool_coroutine(knobs):
        stats_url = 'https://api.blockchair.com/bitcoin/stats'

        try:
            request = urllib.request.Request(
                stats_url,
                headers={},
            )
            stats = json.loads(
                urllib.request.urlopen(request).read().decode()
            )
            unconfirmed_tx_count = format(stats['data']['mempool_transactions'], ',')
            mempool_size = round(stats['data']['mempool_size']/1000000, 2)
        except:
            raise
        else:
            return f'BTC Mempool: {unconfirmed_tx_count} unconfirmed txs @ {mempool_size} MB'

    await component.async_register(connection, btc_mempool_coroutine)

iterm2.run_forever(main)
