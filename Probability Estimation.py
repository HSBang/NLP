import numpy as np
import matplotlib.pyplot as plt
from math import exp, pi


#np.random.seed(2)
e = np.random.normal(30, 3, 100)
F = np.random.normal(1000, e) #draw random samples with a mean of 1000 assuming Gaussian error
F_bar = np.mean(F)

#Computing Maximum Likelihood Distribution based on Frequentist Approach
likelihood_dist = np.empty(len(F))
for f in range(len(F)):
    likelihood_F = 1
    for i in range(len(F)):
        pdf = np.empty(len(F))
        pdf[i] = ((2*pi*(e[i]**2))**-0.5)*exp(-(F[i]-F[f])**2/(2*(e[i]**2)))
    for val in pdf:
        likelihood_F = likelihood_F*val
    likelihood_dist[f] = likelihood_F

result = list(zip(F, likelihood_dist))
#Plot the Result
plt.plot(F, likelihood_dist, marker='.', linestyle='none', color='blue')
plt.axvline(F_bar, linestyle='solid', color='red')

plt.xlabel("Value of F")
plt.ylabel("Likelihood")
plt.show()

w = 1/e**2
F_hat = np.sum(w*F)/np.sum(w)
sigma_F = w.sum()**(-0.5)
print("mean of F: ", F_bar)
print("F_hat: ", F_hat)
