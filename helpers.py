import requests
import pandas as pd

import scipy.stats as ss

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

def draw_odds(decksize, in_deck, draws, success):
    """
    :param decksize: assumes 30 card hearthstone deck
    :param in_deck: number of cards in the deck
    :param draws: number of draws
    :param success: how many cards are needed in hand
    :return:
    """
    N = decksize  # Total population from which to draw
    m = in_deck # Number of successes in deck
    n = draws  # Number of draws
    k = success  # Successes desired

    draw = ss.hypergeom(N, m, n)
    p = draw.cdf(k)
    return 1 - p

def draw_table(mana_curve, n):
    # Chance to draw 1 DataFrame
    container = {}
    for mana, count in mana_curve:
        ods = [draw_odds(30, count, x + 3, n) for x in range(11)]
        container[mana] = ods

    return pd.DataFrame(container)





