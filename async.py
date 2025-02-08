import asyncio
import requests
import time
import aiohttp


"""
async def test():
    print("start 1")
    await asyncio.sleep(2)
    print("WE DID IT (1)")


async def test2():
    print("start 2")
    await asyncio.sleep(3)
    print("WE DID IT (2)")


async def test3():
    print("start 3")
    await asyncio.sleep(1)
    print("WE DID IT (3)")
"""

"""
async def fetch_async(url, session):
    async with session.get(url) as response:
        return await response.text()

async def main():
    async with aiohttp.ClientSession() as session:
        page1 = asyncio.create_task(fetch_async("http://google.com", session))
        page2 = asyncio.create_task(fetch_async("http://youtube.com", session))
        await asyncio.gather(page1, page2)


start_time = time.time()
asyncio.run(main())
print(f"ASYNC TIME: {time.time() - start_time}")





def fetch(url):
    return requests.get(url).text

start_time = time.time()
page1 = fetch("http://google.com")
page2 = fetch("http://youtube.com")
print(f"STINKY TIME: {time.time() - start_time}")
"""


"""
async def main():
    print("damn I'm good")
    L = await asyncio.gather(test(), test2(), test3())
    print("It's so over")
"""

#asyncio.run(main())


