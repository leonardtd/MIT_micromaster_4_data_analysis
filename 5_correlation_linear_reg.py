import numpy as np

Xs = np.array([0.0339, 0.0423, 0.213, 0.257, 0.273, 0.273, 0.450, 0.503, 0.503, \
0.637, 0.805, 0.904, 0.904, 0.910, 0.910, 1.02, 1.11, 1.11, 1.41, \
1.72, 2.03, 2.02, 2.02, 2.02])

Ys = np.array([-19.3, 30.4, 38.7, 5.52, -33.1, -77.3, 398.0, 406.0, 436.0, 320.0, 373.0, \
93.9, 210.0, 423.0, 594.0, 829.0, 718.0, 561.0, 608.0, 1.04E3, 1.10E3, \
840.0, 801.0, 519.0])

N = 24


print(f"mean X: {np.mean(Xs):.3f}")
print(f"mean Y: {np.mean(Ys):.3f}")
print(f"std X: {np.std(Xs, ddof=1):.3f}")
print(f"std Y: {np.std(Ys, ddof=1):.3f}")

### cov
print(f"covariance: {np.cov(Xs, Ys, ddof=1).flatten()[1]:.3f}")

### corr
print(f"correlation: {np.corrcoef(Xs, Ys).flatten()[1]:.3f}")

### linear_reg
sample_std_x = np.std(Xs, ddof=1)
sample_std_y = np.std(Ys, ddof=1)

corr_x_y = np.corrcoef(Xs, Ys).flatten()[1]

#b_1 = r*(sx/sy)
beta_1 = corr_x_y*(sample_std_y/sample_std_x)
print(f"beta_1: {beta_1:.3f}")

#b_0
sample_mean_x = np.mean(Xs)
sample_mean_y = np.mean(Ys)

beta_0 = sample_mean_y - beta_1 * sample_mean_x
print(f"beta_0: {beta_0:.3f} km/s")
