
import asyncio
import json
import urllib.request
import ssl
import iterm2

async def main(connection):
    component = iterm2.StatusBarComponent(
        short_description='Bitcoin Havlening Stats',
        detailed_description='Displays BTC havlening completion percentage',
        exemplar='BTC Halvening in 31,491 blocks (91.1943%)',
        update_cadence=60*5,
        identifier='schnogz.iterm-crypto-components.btc-halvening',
        knobs=[],
    )

    @iterm2.StatusBarRPC
    async def btc_halvening_coroutine(knobs):
        BLOCK_HALVENING = 210000
        stats_url = 'https://api.blockchair.com/bitcoin/stats'

        try:
            context = ssl._create_unverified_context()
            request = urllib.request.Request(
                stats_url,
                headers={},
            )
            currentBlock = json.loads(
                urllib.request.urlopen(request, context=context).read().decode()
            )['data']['blocks']
            # TODO: only works until 2024
            if currentBlock >= 630000:
                remaining_blocks = currentBlock - 840000
            else:
                remaining_blocks = currentBlock - 630000

            remaining_blocks_formatted = format(abs(remaining_blocks), ',')
            halvening_percentage = round(currentBlock % BLOCK_HALVENING / BLOCK_HALVENING * 100, 4)

        except:
            raise
        else:
            return f'BTC Halvening in {remaining_blocks_formatted} blocks ({halvening_percentage}%)'

    await component.async_register(connection, btc_halvening_coroutine)

iterm2.run_forever(main)
