from aioconsole import aprint
from classes import discordgateway
import asyncio




async def main():
    tokens = open("tokens.txt").read().splitlines()
    tasks = []
    for token in tokens:
        dg = discordgateway(token)
        task = asyncio.create_task(dg.simple_connect())
        tasks.append(task)

    await asyncio.gather(*tasks, return_exceptions=True)




asyncio.run(main())
