import numpy as np
from helpers import *

card_collection = build_collection()
deck = import_deck()
deck = add_cost(card_collection, deck)

#Calculate Mana Curve

mana_curve = (deck.groupby(['cost']).agg({'number':[np.sum]}))

mana_curve = [tuple(x) for x in mana_curve.to_records(index=True)]
print(mana_curve)

