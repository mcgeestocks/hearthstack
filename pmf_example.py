N = 30  # Total population from which to draw
m = 4  # Number of successes in deck
n = 3   # Number of draws
k = 1   # Successes desired

import scipy.stats as ss
hpd = ss.hypergeom(N,m,n)
p = hpd.pmf(k)

print(p)


