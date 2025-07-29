## Hi there 👋

<!--
**kaneko424/kaneko424** is a ✨ _special_ ✨ repository because its `README.md`
(this file) appears on your GitHub profile.

Here are some ideas to get you started:

- 🔭 I’m currently working on ...
- 🌱 I’m currently learning ...
- 👯 I’m looking to collaborate on ...
- 🤔 I’m looking for help with ...
- 💬 Ask me about ...
- 📫 How to reach me: ...
- 😄 Pronouns: ...
- ⚡ Fun fact: ...
-->

## Web Scraper

This repository includes a simple Python script, `scraper.py`, that fetches a web page and prints the headings (``<h1>`` to ``<h3>``) found on that page.

### Requirements

- Python 3.7+
- [`requests`](https://pypi.org/project/requests/)
- [`beautifulsoup4`](https://pypi.org/project/beautifulsoup4/)

Install dependencies using:

```bash
pip install -r requirements.txt
```

### Usage

```bash
python scraper.py https://example.com
```

This will print the headings retrieved from the provided URL.

### Disclaimer

Please respect each website's terms of service when running this script. Some sites prohibit automated scraping. Always check and comply with the website's robots.txt and any other applicable policies.
