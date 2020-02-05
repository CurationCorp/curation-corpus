import pandas as pd
import asyncio
import aiohttp
from fastprogress import progress_bar
import os
import csv
from sys import argv

USAGE = """$ python async_scraper.py <batch_size> <path_without_bodies> <path_with_bodies>"""

try:
    batch_size = int(argv[1])
    without_bodies = argv[2]
    with_bodies = argv[3]
except IndexError:
    print(USAGE)
    exit(1)

urls = list(pd.read_csv(without_bodies)['url'])

html = []

async def fetch(url, session):
    try:
        async with session.get(url) as response:
            assert response.status == 200
            return await response.text()
    except Exception:
        try:
            async with session.get(url.replace("http", "https")) as response:
                assert response.status == 200
                return await response.text()
        except Exception:
            try:
                async with session.get(f'https://web.archive.org/web/{url}') as response:
                    assert response.status == 200
                    return await response.text()
            except Exception:
                return "Exception"


async def run(urls, csvwriter):
    tasks = []
    async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(total=5)) as session:
        for url in urls:
            task = asyncio.ensure_future(fetch(url, session))
            tasks.append(task)
        responses = await asyncio.gather(*tasks)

        csvwriter.writerows(zip(urls, responses))
        

with open(with_bodies, 'w') as o:
    csvwriter = csv.writer(o)
    for i in progress_bar(range(0, len(urls), batch_size)):    
        loop = asyncio.get_event_loop()
        future = asyncio.ensure_future(run(urls[i:i+batch_size], csvwriter))
        loop.run_until_complete(future)
