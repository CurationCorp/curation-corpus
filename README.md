<p align="center">
    <br>
    <a href="https://curationcorp.com" target="_blank">
    <img src="curationlogo.png"/>
    </a>
    <br>
</p>

<h1 align="center">Curation Corpus for Abstractive Text Summarisation</h1>

The Curation Corpus is a collection of 40,000 professionally-written summaries of news articles, with links to the articles themselves. This repository provides a scraper to access them. If you're interested in commercial use or access to the wider catalogue of Curation data, including a larger set of over 150,000 professionally-written abstracts and a scalable, on-demand content abstraction API (driven by humans or AI), please get in touch. For our thoughts on how we hope this release will help the NLP community, see our [post introducing the dataset](https://medium.com/curation-corporation/teaching-an-ai-to-abstract-a-new-dataset-for-abstractive-auto-summarisation-5227f546caa8).

|                | Documents  | License        | Avg. summary length (words) | Avg. document length (words) | Avg. summary length (sentences) | Avg. document length (sentences) | Type                                                                                     |
| -------------- | ---------- | -------------- | --------------------------- | ---------------------------- | ------------------------------- | -------------------------------- | ---------------------------------------------------------------------------------------- |
| CNN            | 90,266     | N/A            | 45.7                        | 760.5                        | 3.59                            | 34                               | Implied by "summary" box                                                                 |
| DailyMail      | 196,961    | N/A            | 54.7                        | 653.3                        | 3.86                            | 29.3                             | Implied by bullets below headline                                                        |
| NYT            | 110,540    | Non-commerical | 45.5                        | 800                          | 2.44                            | 35.6                             | Abstractive summary                                                                      |
| Xsum           | 276,711    | N/A            | 23.3                        | 431                          | 1                               | 19.7                             | Single sentence answering "what is this article about?"                                  |
| Curation Base  | 40,000     | CC-BY          | 82.6                        | 527.9                        | 4.9                             | 27.4                             | Professionally written and edited standalone summary intended to be understood by itself |
| Curation Large | ~150,000\* | Commercial     | 81.3                        | 521                          | 4.9                             | 27                               | Professionally written and edited standalone summary intended to be understood by itself |

### Instructions

- Clone this repository

```shell
git clone git@github.com:CurationCorp/curation-corpus.git && cd curation-corpus
```

- Download the article titles, summaries, urls, and dates

```shell
wget https://curation-datasets.s3-eu-west-1.amazonaws.com/curation-corpus-base.csv
```

- Download the article content

```shell
python web_scraper.py [FILE_WITHOUT_ARTICLE_CONTENT] [FILE_WITH_ARTICLE_CONTENT]
```

Some urls will return messy results due to content changing over time, paywalls, etc. We've tried to remove the worst offenders from this release. There is probably still scope though for improving the scraper though.

### Tutorials

We are still learning about this field ourselves and will share our tutorials in the [examples folder](https://github.com/CurationCorp/curation-corpus/tree/master/examples). If you use our dataset in your own research, write a tutorial, or have anything you would like to share, let us know and we will link to it from here!

### About Curation

[Curation](https://curationcorp.com) is a SaaS business combining machine learning & human intelligence enabling executives to effortlessly follow emerging risks, themes and client activity with a particular focus on ESG-related issues. We enable businesses to act faster, delivering significant time and cost savings.

### Citation

```
@misc{curationcorpusbase:2020,
  title={Curation Corpus Base},
  author={Curation},
  year={2020}
}
```

### License

Please remember to attribute any derivative works in accordance with the terms of the CC-BY license.

This work is licensed under a [Creative Commons Attribution 4.0 International
License][cc-by].

[![CC BY 4.0][cc-by-image]][cc-by]

[cc-by]: http://creativecommons.org/licenses/by/4.0/
[cc-by-image]: https://i.creativecommons.org/l/by/4.0/88x31.png
[cc-by-shield]: https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg
