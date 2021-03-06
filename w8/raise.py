import asyncio

async def boom(n):
    return 1/n

asyncio.ensure_future(boom(1))
asyncio.ensure_future(boom(0))

try:
    asyncio.get_event_loop().run_forever()
except KeyboardInterrupt:
    print('bye')
