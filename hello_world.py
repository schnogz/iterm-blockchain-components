import asyncio
import iterm2
import random

GREETINGS = [
    'Hello, world!',
    '¡Hola mundo!',
    'Salamu, dunia!',
    'শুভেচ্ছা, বিশ্ব!',
    '问候，世界！',
    'Chào thế giới!',
    'Բարեւ աշխարհ!',
]

async def main(connection):
    component = iterm2.StatusBarComponent(
        short_description='hello-world',
        detailed_description='Displays random welcome greeting',
        exemplar='Hello, world!',
        update_cadence=10,
        identifier='schnogz.iterm-btc-components.hello-world',
        knobs=[],
    )

    @iterm2.StatusBarRPC
    async def hello_world_coroutine(knobs):
        return random.choice(GREETINGS)

    await component.async_register(connection, hello_world_coroutine)

iterm2.run_forever(main)
