import aiohttp
import asyncio
from bs4 import BeautifulSoup
import csv
from fastprogress import progress_bar
import os
import pandas as pd
from readability import Document
from sys import argv


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


def scrape(urls, batch_size, output_path):
    with open(output_path, 'w') as o:
        csvwriter = csv.writer(o)
        csvwriter.writerow(['url', 'html'])
        for i in progress_bar(range(0, len(urls), batch_size)):
            loop = asyncio.get_event_loop()
            future = asyncio.ensure_future(
                run(urls[i:i+batch_size], csvwriter))
            loop.run_until_complete(future)


def extract_content(df):
    text_list = []
    for i in progress_bar(range(df.shape[0])):
        try:
            text = BeautifulSoup(
                Document(df.iloc[i][1]).summary(), features="lxml").get_text().strip()
        except Exception:
            text = "Exception"
        text_list.append(text)
    df['article_content'] = text_list

    return df
        

def get_article_bodies(input_path, output_path, batch_size):
    if os.path.isfile(input_path) and input_path.endswith('.csv'):
        df = pd.read_csv(input_path)

    urls = list(df['url'])

    scrape(urls, batch_size, output_path)
    
    df = pd.read_csv(output_path)
    df = extract_content(df)
    df.to_csv(output_path, index=False)
    print()

   
if __name__ == "__main__":
    USAGE = """$ python web_scraper.py <input_path> <output_path> <batch_size>"""

    try:
        input_path = argv[1]
        output_path = argv[2]
        batch_size = int(argv[3])
    except IndexError:
        print(USAGE)
        exit(1)

    get_article_bodies(input_path, output_path, batch_size)
    
