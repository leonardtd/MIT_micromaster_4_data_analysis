from scipy.stats import fisher_exact
import scipy
from scipy import stats
from scipy import special
import math

k = 39
M = 62000
N = 102
n = 31000

"""
The hypergeometric distribution models drawing objects from a bin. 
M is the total number of objects, n is total number of Type I objects.
The random variate represents the number of Type I objects in N drawn 
without replacement from the total population.
"""

# Hypergeometric distribution
print(stats.hypergeom.cdf(k, M, n, N))

p_value = 0
for i in range(k+1):  # up to k=39
    p_value += (math.comb(n, i) * math.comb(M-n, N-i))/math.comb(M, N)
print(p_value)


# Fisher Exact Test
print('Fisher exact test (hypergeom)')
table = [[39, 63], [30961, 30937]]

res = fisher_exact(table, alternative='less')
print(f"p-value {res[1]:.4f}")
