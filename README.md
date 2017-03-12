# Hearthstack
 

#### Survival function (also defined as 1 - cdf):

Chance to draw at least one card by turn 

```python
# chance to draw at least 1 card in opening hand

N = 30  # Total population from which to draw
m = 6  # Number of successes in deck
n = 5   # Number of draws
k = 0   # Successes desired

import scipy.stats as ss

hpd = ss.hypergeom(N,m,n)
p = hpd.sf(k)

print(p)

```

which yields `0.35960591133`

---

####Cumulative Distribution Function



```python
# chance to draw at least 2 card in opening hand

N = 30  # Total population from which to draw
m = 3  # Number of successes in deck
n = 4   # Number of draws
k = 1   # Successes desired

import scipy.stats as ss

hpd = ss.hypergeom(N,m,n)
p = hpd.cdf(k)
print (1-p)

```



---