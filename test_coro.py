import asyncio
import sys

async def dummy():
    await asyncio.sleep(1)

async def main():
    dummy() # never awaited

asyncio.run(main())
