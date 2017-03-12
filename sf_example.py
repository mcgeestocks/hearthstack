# chance to draw at least 1 card in opening hand

N = 30  # Total population from which to draw
m = 3  # Number of successes in deck
n = 7   # Number of draws
k = 0   # Successes desired

import scipy.stats as ss

hpd = ss.hypergeom(N,m,n)
p = hpd.sf(k)

print(p)