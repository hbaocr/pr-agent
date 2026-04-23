import asyncio
import sys

async def dummy():
    await asyncio.sleep(10)

async def main():
    asyncio.create_task(dummy())
    tasks = [t for t in asyncio.all_tasks() if t is not asyncio.current_task()]
    for t in tasks:
        t.cancel()

asyncio.run(main())
