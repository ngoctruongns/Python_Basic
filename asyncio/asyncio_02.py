#!/usr/bin/env python

import asyncio
import time
from datetime import datetime

async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)

async def main():
    print(f"started at {time.strftime('%X')}")
    print(f'{datetime.now().timestamp():.0f}')

    await say_after(1, 'hello')
    await say_after(2, 'world')

    print(f"finished at {time.strftime('%X')}")

if __name__ == "__main__":
    asyncio.run(main())