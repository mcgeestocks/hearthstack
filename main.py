from helpers import *
from tabulate import tabulate

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

card_collection = build_collection()
deck = import_deck()
deck = add_cost(card_collection, deck)

#Calculate Mana Curve

mana_curve_df = (deck.groupby(['cost']).agg({'number':[np.sum]}))
mana_curve = [tuple(x) for x in mana_curve_df.to_records(index=True)]

one_copy = draw_table(mana_curve,0)
one_copy = one_copy.applymap(lambda x: '{:,.2%}'.format(x))
two_copy = draw_table(mana_curve,1)
# convert to percentage for pretty printing
two_copy = two_copy.applymap(lambda x: '{:,.2%}'.format(x))

columns = [str(mana_curve_df['number']['sum'].loc[x]) + 'x ' + str(x) + ' Mana Cards' for x in two_copy.columns.values]


print('\n')
print('no coin all keep')
print('Odds to draw 1 by turn: ')
print(tabulate(one_copy, columns))
print('\n')

print('no coin all keep')
print('Odds to draw 2 by turn: ')
print(tabulate(two_copy, columns))


