# Estimated Number Of Random Sampling 'n' = 100000
# Estimated Area = ?  (Print out)

# import numpy.random as rd
# import numpy as np
# import matplotlib.pyplot as plt
#
#
# def pi_sample(n):
#     count = 0
#     for i in range(n):
#         sample = rd.uniform(-1, 1, size=2)
#         if np.linalg.norm(sample) <= 1:
#             count += 1
#     return np.array([count / (1.0 * n), np.sqrt(1.0 * count) / n])
#
#
# res = np.array([pi_sample(pow(10, i)) for i in range(1, 7)])
# [y, err] = res.transpose()
#
# plt.figure()
#
# plt.errorbar(np.array(range(1, 7)), y, yerr=err, fmt='o')


# Method - 2:
# import inline as inline
# import integral as integral
# import matplotlib
#
# # %matplotlib inline
# from scipy import random
# import numpy as np
# import matplotlib.pyplot as plt
#
# a = 0
# b = np.pi  # Limits of integration
# N = 100000


# def func(x):
#     return np.sin(x)
#
#
# answer = (b - a) / float(N) * integral
#
# areas = []
#
# for i in range(N):
#     xrand = np.zeros(N)
#
#     for i in range(len(xrand)):
#         xrand[i] = random.uniform(a, b)
#         integral = 0.0
#
#     for i in range(N):
#         integral += func(xrand[i])
#
#     answer = (b - a) / float(N) * integral
#
#     areas.append(answer)
#
# plt.title("Distribution Of Areas Calculated")
#
# plt.hist(areas, bins=30, ec='blue')
#
# plt.xlabel("Areas")


# Method-3
import numpy as np
import matplotlib.pyplot as plt

# Limits
a = 0  # lower
b = np.pi  # upper
# Number of iterations (for 10K ≈ 2 sec, for 100K it takes 10*10 more time ≈ 3 minutes on my PC)
N = 10_0000
# var to store the results
areas = []

# This one is slighlty faster and recalls the LateX formula above; it takes about 2 seconds for 10_000
for _ in range(N):
    # Apply the approximation formula
    answer = (b - a) / N * np.sin(np.random.uniform(a, b, N)).sum()
    areas.append(answer)

fig, ax = plt.subplots(figsize=(10,8))
# fig, ax = plt.subplots(figsize=(2, 2))

mu = np.array(areas).mean()
sigma = np.array(areas).std()
textstr = '\n'.join((
    f'$\mu=${mu:.2f}',
    f'$\sigma=${sigma:.2f}'))

ax.hist(areas, bins=31, ec='b')
# these are matplotlib.patch.Patch properties
props = dict(boxstyle='round', facecolor='blue', alpha=0.1)

# place a text box in upper left in axes cords
ax.text(0.05, 0.95, textstr, transform=ax.transAxes, fontsize=14,
        verticalalignment='top', bbox=props)
plt.title("Distribution of calculated areas")
plt.xlabel("Areas")

plt.show()
