import requests
from bs4 import BeautifulSoup
from typing import List


def fetch_titles(url: str) -> List[str]:
    """Fetch headings (h1-h3) from the given URL.

    Parameters
    ----------
    url : str
        Web page URL to scrape.

    Returns
    -------
    list of str
        List of heading texts found on the page.
    """
    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, 'html.parser')
    headings = []
    for tag in soup.find_all(['h1', 'h2', 'h3']):
        text = tag.get_text(strip=True)
        if text:
            headings.append(text)
    return headings


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: python scraper.py <URL>")
        sys.exit(1)

    url = sys.argv[1]
    try:
        titles = fetch_titles(url)
        for title in titles:
            print(title)
    except Exception as exc:
        print(f"Error fetching {url}: {exc}")
        sys.exit(1)

