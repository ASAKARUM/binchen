from scholarly import scholarly
import json
from datetime import datetime
import os

author: dict = scholarly.search_author_id('3XvSeK0AAAAJ')
scholarly.fill(author, sections=['publications'])
name = author['name']
author['updated'] = str(datetime.now())
author['publications'] = {v['author_pub_id']:v for v in author['publications']}
print(json.dumps(author, indent=2))
os.makedirs('results', exist_ok=True)
with open(f'scholar.json', 'w') as outfile:
    json.dump(author, outfile, ensure_ascii=False)