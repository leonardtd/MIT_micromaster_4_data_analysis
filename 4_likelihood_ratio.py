import scipy
from scipy import stats
from scipy import special
import math
import numpy as np

pi_sample = 102/62000
pi_treatment = 39/31000
pi_control = 63/31000

# Lamda: TEST STATISTIC
numerator = stats.binom.pmf(39, 31000, pi_sample) * \
    stats.binom.pmf(63, 31000, pi_sample)
denominator = stats.binom.pmf(
    39, 31000, pi_treatment)*stats.binom.pmf(63, 31000, pi_control)
lambda_value = -2*np.log(numerator/denominator)
print(f"lambda: {lambda_value:.3f}")

print('\n P-value for Chi^2 df:1')
p_value = stats.chi2.sf(lambda_value, df=1)
print(f"p-value: {p_value:.3f}")
