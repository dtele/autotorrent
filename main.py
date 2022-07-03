import argparse
import webbrowser
from typing import List
from urllib.parse import quote_plus

from selenium import webdriver
from selenium.webdriver.common.by import By


class Torrent:
    def __init__(self, href: str, name: str, seeders: str, leechers: str, size: str):
        self.href = href
        self.name = name.split('\n')[0].encode('ascii', errors='ignore').decode('utf-8')
        self.seeders = seeders
        self.leechers = leechers
        self.size = size

    def is_alive(self) -> bool:
        return self.seeders != 0

    def get_magnet(self) -> str | None:
        driver.get(self.href)
        links = driver.find_elements(By.TAG_NAME, 'a')

        for link in links:
            if link.text.casefold() == 'magnet download':
                return link.get_attribute('href')

        return None


def torrent_search(search_term: str, rows: int = 10) -> List[Torrent]:
    search_term = quote_plus(search_term)
    final_results = []
    page = 1

    while len(final_results) < rows:
        driver.get(fr'https://1337x.to/search/{search_term}/{page}/')
        page_results = driver.find_elements(By.TAG_NAME, 'tr')[1:]
        page += 1

        if len(page_results) == 0:
            break

        for result in page_results:
            href = result.find_elements(By.TAG_NAME, 'a')[1].get_attribute('href')
            details = [i.text for i in result.find_elements(By.TAG_NAME, 'td') if i.text]

            final_results.append(Torrent(*[href, *details]))

    return final_results[:rows]


parser = argparse.ArgumentParser()
parser.add_argument('search_term', action='store')
parser.add_argument('rows', action='store', type=int)
args = parser.parse_args()

options = webdriver.ChromeOptions()
options.headless = True
options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Chrome(options=options)

results = torrent_search(args.search_term, args.rows)

# TODO: fix this shit later lol
parsed_results = [['sno'] + [str(row + 1) for row in range(args.rows)]] + [[parameter] + [torrent.__getattribute__(parameter) for torrent in results] for parameter in ['name', 'seeders', 'leechers', 'size']]
max_lens = [max(map(len, col)) for col in parsed_results]

for row in range(args.rows + 1):
    for pos, col in enumerate(parsed_results):
        space_balance = ' ' * (max_lens[pos] - len(col[row]) + 4)
        print(col[row] + space_balance, end='')
    print()

download = int(input('Download\n>> '))
magnet = results[download - 1].get_magnet()
webbrowser.open(magnet)

driver.quit()
