# Hearthstack
 

#### Probability Mass Fuction Example:

Assume we have `30 card deck` with exactly `4 two-drops` and we want to determine how many 
opening hands of `3 cards` will have at `least 1 present`.

```python
import scipy.stats as ss

N = 30  # Total population from which to draw
m = 4  # Number of successes in deck
n = 3   # Number of draws
k = 1   # Successes desired

hpd = ss.hypergeom(N,m,n)
p = hpd.pmf(k)
```

which yields `0.320197044335`

---

####Cumulative Distribution Function
Assume we have a `60 cards deck` with exactly `24 lands` and we want to determine the probability
our a opening hand of `7 cards` will have between `2 to 4 lands`

because `ss.hypergeom.cdf(M, n, N)` yields the probability `<= k` we take `k=4` (all hands with four or fewer lands)
then subtract `k=1` (all hands with zero or one land)  then add `hypergeom.pmf(k=2)`

```python
N = 60  # Total population from which to draw
m = 24  # Number of successes in deck
n = 7   # Number of draws
k_low = 2   # lower bound of successes desired
k_high = 4  # upper bound of successes desired

import scipy.stats as ss

p_low = ss.hypergeom(N,m,n).cdf(k_low)
p_high = ss.hypergeom(N,m,n).cdf(k_high)
p = ss.hypergeom(N,m,n).pmf(k_low)

```

which yields `0.774567042973`

---