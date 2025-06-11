from pathlib import Path

import requests
from bs4 import BeautifulSoup
from html2text import HTML2Text

MADEINABYSS_WIKIPEDIA_URL = "https://ja.wikipedia.org/wiki/メイドインアビス"

if __name__ == "__main__":
    response = requests.get(MADEINABYSS_WIKIPEDIA_URL)

    soup = BeautifulSoup(response.text, "html.parser")
    mw_body = str(soup.find(class_="mw-body-content"))

    text_maker = HTML2Text()
    text_maker.ignore_links = True
    text_maker.ignore_images = True

    content = text_maker.handle(mw_body)
    Path("assets", "madeinabyss-document.md").write_text(content)
