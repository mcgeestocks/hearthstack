N = 60  # Total population from which to draw
m = 24  # Number of successes in deck
n = 7   # Number of draws
k_low = 2   # lower bound of successes desired
k_high = 4  # upper bound of successes desired

import scipy.stats as ss

p_low = ss.hypergeom(N,m,n).cdf(k_low)
p_high = ss.hypergeom(N,m,n).cdf(k_high)
p = ss.hypergeom(N,m,n).pmf(k_low)


print (p_high - p_low + p)



