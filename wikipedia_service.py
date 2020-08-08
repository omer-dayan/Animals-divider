import wikitables
import wikipedia
import requests
import os
import json
import time
from multiprocessing.pool import ThreadPool
import sys


# The best way to request the image of a wikipedia page is by request in this specific format
WIKI_REQUEST = 'http://en.wikipedia.org/w/api.php?action=query&prop=pageimages&format=json&piprop=original&titles='


#
# Method to extract tables from wikipedia page. A page may contains multiple tables
# So the table index indicate which one to return. If the table does not exists, it
# returns null
#
def get_wikipedia_table(wikipedia_page, table_index):
    page_tables = wikitables.import_tables(wikipedia_page)
    if len(page_tables) <= table_index:
        return None
    return page_tables[table_index]


#
# Fetch wikipedia page main image.
# The enrty argument contains the wikipedia page and the locl path to download to
# As follow ( wikipedia page , Local path to download to )
#
def fetch_main_wiki_image(entry):
    page, path = entry
    try:
        result = wikipedia.search(page, results = 1)
        wikipedia.set_lang('en')
        wikipedia_page = wikipedia.WikipediaPage(title = result[0])
        response = requests.get(WIKI_REQUEST + wikipedia_page.title)
        json_data = json.loads(response.text)
        img_url = list(json_data['query']['pages'].values())[0]['original']['source'] # Gets the *main* page image

        if not os.path.exists(path):
            r = requests.get(img_url, stream=True)
            count = 1
            while r.status_code != 200 and count <= 15:
                time.sleep(2.5)
                r = requests.get(img_url, stream=True)
                count += 1
            if r.status_code == 200:
                with open(path, 'wb') as f:
                    for chunk in r:
                        f.write(chunk)
    except Exception as ex:
        sys.stderr.write('Could not download ' + page + ' image. Exception: ' + ex)
        return 0


#
# Method to download simultanously multiple wikipedia pages main image
# Please notice to adjust the threads_count to an adequate value to your
# current specs
#
def download_multiple_wikipedia_main_images(pages, dst_path, threads_count):
    urls = []
    for page in pages:
        urls.append((page, os.path.join(dst_path, page + '.jpg')))
    rs = ThreadPool(threads_count).imap_unordered(fetch_main_wiki_image, urls)

    while True:
        completed = rs._index
        if completed == len(urls):
            break
        pre = str(int((completed / len(urls)) * 100))
        print('Finished ' + pre + '% of work')
        time.sleep(2)
