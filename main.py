from helpers import *
from tabulate import tabulate

import click
import numpy as np

@click.command()
@click.option('--deckpath', default='example_deck.txt',
              prompt='Input path to deck txt or replace contents of', help='location of deck.txt file')
@click.option('--coin', default=1, prompt='Going 1st or 2nd')
@click.option('--mulligan', default=0, prompt='Mulligan 1, 2 or 3 cards')
@click.option('--export', default='n', prompt='export to csv y/n', help='export data to csv')

def generate_ods(**kwargs):
    try:
        card_collection = build_collection()
        deck = import_deck(kwargs['deckpath'])
        deck = add_cost(card_collection, deck)

        #Calculate Mana Curve
        mana_curve_df = (deck.groupby(['cost']).agg({'number':[np.sum]}))
        mana_curve = [tuple(x) for x in mana_curve_df.to_records(index=True)]
    except:
        pass

    if kwargs['coin'] == 1:
        one_copy = draw_table(mana_curve, 0, 4+kwargs['mulligan'])
        if kwargs['export'] == 'Y':
            one_copy.to_csv('export1.csv')

        # convert to percentage for pretty printing
        one_copy = one_copy.applymap(lambda x: '{:,.2%}'.format(x))

        two_copy = draw_table(mana_curve,1, 4+kwargs['mulligan'])
        if kwargs['export'] == 'Y':
            two_copy.to_csv('export2.csv')

        # convert to percentage for pretty printing
        two_copy = two_copy.applymap(lambda x: '{:,.2%}'.format(x))

        #column name counts
        columns = [str(mana_curve_df['number']['sum'].loc[x]) + 'x ' + str(x) + ' Mana Cards' for x in two_copy.columns.values]
    else:
        one_copy = draw_table(mana_curve, 0, 5+kwargs['mulligan'])
        if kwargs['export'] == 'Y':
            one_copy.to_csv('export1.csv')
        # convert to percentage for pretty printing
        one_copy = one_copy.applymap(lambda x: '{:,.2%}'.format(x))

        two_copy = draw_table(mana_curve,1, 5+kwargs['mulligan'])
        if kwargs['export'] == 'Y':
            two_copy.to_csv('export1.csv')
        # convert to percentage for pretty printing
        two_copy = two_copy.applymap(lambda x: '{:,.2%}'.format(x))

        #column name counts
        columns = [str(mana_curve_df['number']['sum'].loc[x]) + 'x ' + str(x) + ' Mana Cards' for x in two_copy.columns.values]


    print('Odds to draw 1 going %sst after %s card mulligan'% (kwargs['coin'],kwargs['mulligan']))
    print(tabulate(one_copy, columns))
    print('\n')

    print('Odds to draw 2 Going %sst' % kwargs['coin'])
    print(tabulate(two_copy, columns))

if __name__ == '__main__':
    generate_ods()