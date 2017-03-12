import requests
import pandas as pd

url = 'https://api.hearthstonejson.com/v1/17994/enUS/cards.collectible.json'
r = requests.get(url)
jsn = r.json()

print(jsn[1])

collection = {}

for item in jsn:
    collection[item.get('name', 'null')] = item.get('cost', 'null')

df = pd.DataFrame.from_dict(collection, orient='index')
print(df)



