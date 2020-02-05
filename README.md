## The Curation Corpus Dataset for Abstractive Text Summarisation
The Curation Corpus is a collection of 40,000 professionally-written summaries of news articles, with links to the articles themselves. This repository provides a scraper to access them. If you're interested in commercial use or access to the wider catalogue of Curation data, including a larger set of over 150,000 professionally-written abstracts and a scalable, on-demand content abstraction API (driven by humans or AI), please get in touch. For our thoughts on how we hope this release will help the NLP community, see our [announcement here](https://medium.com/curation-corporation/teaching-an-ai-to-abstract-a-new-dataset-for-abstractive-auto-summarisation-5227f546caa8). 

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
Curation Corp is an emerging and peripheral risks monitoring service, providing next generation intelligence to time-challenged professionals. We provide a scalable solution combining machine learning with human curators and experts to log, summarise and catalogue insights in a searchable archive. Curation’s ESG tracker can help clients stay effortlessly informed  on the development of environmental, social and governance related themes and trends.
