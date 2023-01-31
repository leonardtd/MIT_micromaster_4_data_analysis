import scipy
from scipy import stats
from scipy import special
import math
import numpy as np


# 1. z_test calculation
z = (39/31000 - 63/31000)/(math.sqrt((63/31000)*(1-63/31000))/math.sqrt(31000))


z_test_stat = -3.0268
print(f"p-value: {stats.norm.cdf(z):.4f}")

# 2. p-value t-test
print("\n ##### T-TEST #####")
data = np.array([0.9, -0.9, 4.3, 2.9, 1.2, 3.0, 2.7, 0.6, 3.6, -0.5])

estimated_variance = (1/(len(data)-1))*np.sum((data - np.mean(data))**2)
estimated_sd = math.sqrt(estimated_variance)
t = np.mean(data)/(estimated_sd/np.sqrt(len(data)))


print(f'p-value: {stats.t.sf(t, df=9):.5f}')
