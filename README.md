# Hearthstack
 ####To Do: 
 - error handling
 - invalid cards names
 - integrate setuptools
 - more math

##Cumulative Distribution Function
Most of this toolkit relies on math like this:
> What is the chance to draw at least `2 buffs` from a deck containing `4 buffs` after `turn 2` after `going first`.

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


#####Suggested Reading:
http://www.gatheringmagic.com/chrismascioli-100512-of-math-and-magic-part-1-the-hypergeometric-distribution/
