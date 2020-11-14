from multiprocessing.dummy import Pool as ThreadPool
from pathlib import Path

from newspaper import Article
from pandas import read_csv
from typer import Typer, progressbar

app = Typer()


def extract_content(url):
    article = Article(url)
    article.download()
    try:
        article.parse()
        txt = article.text
        return txt
    except:
        return ""


@app.command()
def scrape(
    input_path: Path, output_path: Path, step_size: int = 80, num_threads: int = 8
):
    df = read_csv(input_path)
    urls = list(df["url"])
    text_list = []
    with progressbar(range(0, len(urls), step_size)) as progress:
        for i in progress:
            subset = urls[i : i + step_size]
            pool = ThreadPool(num_threads)
            text_list += pool.map(extract_content, subset)
            pool.close()
            pool.join()
    df["article_content"] = text_list
    df = df.drop_duplicates(subset="article_content")
    df.to_csv(output_path, index=False)


if __name__ == "__main__":
    app()