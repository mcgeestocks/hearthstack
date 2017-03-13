import requests
import pandas as pd

def build_collection(url='https://api.hearthstonejson.com/v1/17994/enUS/cards.collectible.json'):
    '''
    :param url: address of hearthstone json card collection
    :return:
    '''
    r = requests.get(url)
    jsn = r.json()

    collection = {}

    for item in jsn:
        collection[item.get('name', 'null')] = item.get('cost', 'null')

    #create dataframe
    df = pd.DataFrame.from_dict(collection, orient='index')

    # set index name
    df.index.rename('card_name',inplace=True)
    # rename column 0 -> cost
    df = df.rename(columns={0:"cost"})

    return df

def import_deck(file='example_names.txt'):
    '''

    expected format look like
    card name x 2
    second name x 2
    ect...

    :param file: path to file

    :return:
    '''

    file = open(file).read()
    file = file.split('\n')

    deck = []
    for item in file:
        deck.append(item.split(' x '))

    deck_df = pd.DataFrame(deck)
    deck_df.fillna(value=1, inplace=True)
    deck_df = deck_df.rename(columns={0:"card_name", 1:"number"})
    deck_df.set_index('card_name',inplace=True)
    deck_df['number'] = deck_df['number'].astype(int)

    return deck_df


def add_cost(collection_df,deck_df):
    df = pd.merge(deck_df, collection_df, right_index=True, left_index=True)
    return df