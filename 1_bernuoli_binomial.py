import scipy
from scipy import stats
from scipy import special


def binomial_pmf(n, p, k):
    comb = special.comb(n, k)

    probability = comb*(p**k)*((1-p)**(n-k))
    return probability


n = 31000
p = 63/31000
k = float(63)

# probabilidad de que mueran 63 personas de las 31k del grupo control
#
#print(f'{binomial_pmf(n, p, k):.4f}')

###
#print(stats.binom.ppf(0.05, 31000, 0.00203))
# print(stats.binom.cdf(39, 31000, 0.002))  # p-value calc
"""
https://discovery.cs.illinois.edu/learn/Polling-Confidence-Intervals-and-Hypothesis-Testing/Python-Functions-for-Random-Distributions/
PPF: Probability Point Function
The Probability Point Function or PPF is the inverse of the CDF. Specifically, the PPF returns the exact point where the probability of everything to the left is equal to y. This can be thought of as the percentile function since the PPF tells us the value of a given percentile of the data.

COIN.ppf(0.2) asks "what is the 20%-tile of heads?
COIN.ppf(0.6) asks "what is the 60%-tile of heads?
COIN.ppf(0.99) asks "what is the 99%-tile of heads?
"""
