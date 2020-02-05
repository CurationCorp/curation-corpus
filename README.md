![Curation Logo](curationlogo.png)

## The Curation Corpus Dataset for Abstractive Text Summarisation
The Curation Corpus is a collection of 40,000 professionally-written summaries of news articles, with links to the articles themselves. This repository provides a scraper to access them. If you're interested in commercial use or access to the wider catalogue of Curation data, including a larger set of over 150,000 professionally-written abstracts and a scalable, on-demand content abstraction API (driven by humans or AI), please get in touch. For our thoughts on how we hope this release will help the NLP community, see our [announcement here](https://medium.com/curation-corporation/teaching-an-ai-to-abstract-a-new-dataset-for-abstractive-auto-summarisation-5227f546caa8). 

||Documents|License|Avg. summary length (words)|Avg. document length (words)|Avg. summary length (sentences)|Avg. document length (sentences)|Type|
|--- |--- |--- |--- |--- |--- |--- |--- |
|CNN|90,266|N/A|45.7|760.5|3.59|34|Implied by "summary" box|
|DailyMail|196,961|N/A|54.7|653.3|3.86|29.3|Implied by bullets below headline|
|NYT|110,540|Non-commerical|45.5|800|2.44|35.6|Abstractive summary|
|Xsum|276,711|N/A|23.3|431|1|19.7|Single sentence answering "what is this article about?"|
|Curation Base|40,000|CC-BY|82.6|527.9|4.9|27.4|Professionally written and edited standalone summary intended to be understood by itself|
|Curation Large|134,849*|Commercial|81.3|521|4.9|27|Professionally written and edited standalone summary intended to be understood by itself

### Instructions
> * Clone this repository
> * Download the urls, headlines, and summaries from here
> * Run `scraper.py`. Larger batch sizes will make it run faster but it may drop more articles due to timeouts. I recommend ~50 on a 2015 Macbook Pro. 

### Tutorials
We are still learning about this field ourselves and will publish share our tutorials here. If you use our dataset in your own research, write a tutorial, or have anything you would like to share, let us know and we will link to it here. To kick things off, here is our first attempt: 

**Finetuning the BertSumExtAbs model from [Liu and Lapata 2019](https://arxiv.org/abs/1908.08345)**
> * [Medium post](https://medium.com/curation-corporation/fine-tuning-bert-for-abstractive-summarisation-with-the-curation-dataset-79ea4b40a923)
> * [Code](), including a [notebook]() that attempts a walk though from scratch

### About Curation
[Curation](https://curationcorp.com) is a SaaS business combining machine learning & human intelligence enabling executives to effortlessly follow emerging risks, themes and client activity with a particular focus on ESG-related issues. We enable businesses to act faster, delivering significant time and cost savings.

Shield: [![CC BY 4.0][cc-by-shield]][cc-by]

This work is licensed under a [Creative Commons Attribution 4.0 International
License][cc-by].

[![CC BY 4.0][cc-by-image]][cc-by]

[cc-by]: http://creativecommons.org/licenses/by/4.0/
[cc-by-image]: https://i.creativecommons.org/l/by/4.0/88x31.png
[cc-by-shield]: https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg
