# Hearthstack
 To Do: 
 - Clean up Readme
 - Graph Pandas
##Cumulative Distribution Function

What is the chance to draw at least `2 buffs` from a deck containing `4 buffs` after `turn 2` after `going first`.

```python
N = 30  # Total population from which to draw
m = 4  # Number of successes in deck
n = 5   # Number of draws
k = 1   # Successes desired

import scipy.stats as ss

hpd = ss.hypergeom(N,m,n)
p = hpd.cdf(k)
print (1-p)

```
The approach above yields `11.877%` chance to draw after `turn 2`


## Survival function (also defined as 1 - cdf):

What is the chance to draw at least `1 6-Drop` from a deck containing `3 6-Drops` after `turn 5` after `going first`.

```python
# chance to draw at least 1 card in opening hand

N = 30  # Total population from which to draw
m = 3  # Number of successes in deck
n = 7   # Number of draws
k = 0   # Successes desired

import scipy.stats as ss

hpd = ss.hypergeom(N,m,n)
p = hpd.sf(k)

print(p)
```
The approach above yields `56.38%` chance to draw after `turn 5`