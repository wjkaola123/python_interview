import asyncio
from aiohttp import ClientSession


async def fetch(url, session):
    async with session.get(url) as response:
        return await response.read()


async def run(r=10):
    url = 'http://httpbin.org/get'
    tasks = []

    async with ClientSession() as session:
        for i in range(r):
            task = asyncio.ensure_future(fetch(url, session))
            tasks.append(task)

        responses = await asyncio.gather(*tasks)
        for resp_body in responses:
            print(len(resp_body))


loop = asyncio.get_event_loop()
future = asyncio.ensure_future(run())
loop.run_until_complete(future)
